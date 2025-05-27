from constants import (
    BEDROCK_SERVER_MANAGER,
    M_WRAPPER_STARTED,
    M_WRAPPER_STOPPED,
    WRAPPER_LOG_PATH,
)
from server import BedrockServer
from monitor import Monitor
from os import getenv
import asyncio
import logging

logging.basicConfig(
    filename=WRAPPER_LOG_PATH,
    filemode="w",
    format="[%(levelname)s] %(message)s",
    level=getenv("LOG_LEVEL", logging.INFO),
)


async def main():
    try:
        logger: logging.Logger = logging.getLogger(name=BEDROCK_SERVER_MANAGER)
        logger.info(M_WRAPPER_STARTED)
        server: BedrockServer = BedrockServer(logger)
        monitor: Monitor = Monitor(logger, server)
        await monitor.poll_players_count(),
        logger.info(M_WRAPPER_STOPPED)
    except Exception as e:
        logger.error(e)
        raise e

    # except asyncio.CancelledError:
    #     server.clean_up()
    # except KeyboardInterrupt:
    #     server.clean_up()


if __name__ == "__main__":
    asyncio.run(main())
