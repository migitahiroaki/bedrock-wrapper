from logging import Logger
import os
import subprocess
import time
import atexit
from constants import (
    C_STOP,
    C_LIST,
    M_ALREADY_STOPPED,
    M_ALREADY_STOPPED_WITH,
    M_TIMED_OUT_AFTER,
    T_POLL_LOG_INTERVAL,
    SERVER_DIRECTORY,
    SERVER_BINARY,
    SERVER_LOG_PATH,
)


class BedrockServer:

    def __init__(
        self,
        logger: Logger,
        server_directory_path: str = SERVER_DIRECTORY,
        log_path: str = SERVER_LOG_PATH,
    ):
        self.logger: Logger = logger
        atexit.register(self.clean_up)
        self.log_path: str = log_path
        # Don't forget close()
        self.log_file = open(log_path, "w", buffering=1)
        # Don't forget terminate()
        self.server_process: subprocess.Popen = subprocess.Popen(
            [SERVER_BINARY],
            cwd=server_directory_path,
            stdin=subprocess.PIPE,
            stdout=self.log_file,
            stderr=self.log_file,
        )

    def stop(self, timeout: float = 10.0, wait_after_command: float = 10.0):
        ret = self._send_command(C_STOP, timeout)
        time.sleep(wait_after_command)
        return ret

    def list(self, timeout: float = 3.0):
        return self._send_command(C_LIST, timeout)

    def _send_command(self, command: str, timeout: float = 3.0) -> str:
        command_n: str = f"{command}\n"
        if not self.server_process:
            return M_ALREADY_STOPPED
        if isinstance(code := self.server_process.poll(), int):
            return M_ALREADY_STOPPED_WITH.format(code=code)

        # Write command as log
        self.log_file.write(command_n)
        # Read offset
        offset: int = os.path.getsize(self.log_path)
        # Absolute time of timeout
        deadline: float = time.time() + timeout

        self.server_process.stdin.write(command_n.encode())
        self.server_process.stdin.flush()

        if timeout <= 0.0:
            return "command sent"

        interval: float = T_POLL_LOG_INTERVAL
        with open(self.log_path, "r") as f:
            while time.time() < deadline:
                time.sleep(interval)
                f.seek(offset)
                lines = f.readlines()
                if lines:
                    return "\n".join(lines).strip()
                # backoff
                interval *= 2

        raise TimeoutError(M_TIMED_OUT_AFTER.format(timeout=timeout))

    def clean_up(self):
        if self.server_process and self.server_process.poll() is None:
            self.stop()
            self.server_process.terminate()
            self.server_process.wait(60)
        self.log_file.close()
