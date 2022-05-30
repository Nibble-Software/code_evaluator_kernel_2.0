import subprocess
from subprocess import PIPE, TimeoutExpired, Popen
from src.exceptions.FailedProcessError import FailedProcessError
from src.exceptions.CodeTimeoutError import CodeTimeoutError


def run_process(process_name: str, args: [str]):
    process = subprocess.Popen([process_name] + args)
    return_code = process.wait()
    if return_code != 0:
        raise FailedProcessError()


def run_code(process_name: str, args: [str], inputs: [str]) -> [str]:
    process = Popen([process_name] + args, stdout=PIPE, stdin=PIPE, stderr=PIPE) if args is not None \
        else Popen([process_name], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    if inputs is None:
        outputs = no_input_execution(process)

        return outputs

    else:
        outputs = input_execution(process, inputs)

        return outputs


def no_input_execution(process: Popen) -> [str]:
    try:
        data, error = process.communicate(timeout=10)

        data = data.decode('latin1').split('\n')

        data = [item for item in data if item != '']

        process.stdin.close()

        process.stdout.close()

        process.stderr.close()

        return data

    except TimeoutExpired as timeout:

        process.terminate()

        process.communicate()

        raise CodeTimeoutError()


def input_execution(process: Popen, inputs: [str]) -> [str]:
    try:
        input_string = ''.join(input_data + '\n' for input_data in inputs)

        process.stdin.write(input_string.encode('UTF-8'))

        data, err = process.communicate(timeout=10)

        data = data.decode('latin1').split('\n')

        data = [item.replace('\r', '') for item in data if item != '']

        process.stdout.close()

        process.stdin.close()

        process.stderr.close()

        process.terminate()

        print(data)

        return data

    except TimeoutExpired as timeout_error:

        process.terminate()

        process.communicate()

        raise CodeTimeoutError()
