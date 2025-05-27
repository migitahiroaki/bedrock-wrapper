from logging import Logger
from constants import (
    M_FAILED_TO_PARSE_PLAYERS_COUNT,
    R_PLAYERS_COUNT,
    SERVER_LOG_PATH,
    T_MONITOR_INTERVAL,
    T_MONITOR_MAX_RETRY,
)
from server import BedrockServer
import asyncio
import re


class Monitor:
    def __init__(
        self,
        logger: Logger,
        server: BedrockServer,
        log_path: str = SERVER_LOG_PATH,
        monitor_max_retry: int = T_MONITOR_MAX_RETRY,
        monitor_interval: int = T_MONITOR_INTERVAL,
    ):
        self.logger: Logger = logger
        self.server: BedrockServer = server
        self.log_path: str = log_path
        # Decrement on error
        self.monitor_error_counter: int = monitor_max_retry
        self.monitor_interval = monitor_interval
        self.monitor_timer: float = (0.0,)

    async def poll_players_count(self):
        while self.monitor_error_counter > 0:
            await asyncio.sleep(self.monitor_interval)
            text = self.server.list()
            try:
                # parse log message with regex
                match: re.Match | None = re.search(R_PLAYERS_COUNT, text)
                if match:
                    player_count: int = int(match.group(1))
                    if player_count <= 0:
                        break
                else:
                    self.logger.warning(
                        M_FAILED_TO_PARSE_PLAYERS_COUNT.format(text=text)
                    )
            # when known error occured, just decrement error counter.
            except (TimeoutError, IndexError, ValueError) as e:
                self.logger.error(e)
                self.list_error_counter -= 1
            except Exception as e:
                self.logger.error(e)
                break
