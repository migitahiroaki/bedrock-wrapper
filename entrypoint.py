from constants import BEDROCK_SERVER_MANAGER
from server import BedrockServer
from monitor import Monitor
import asyncio
from logging import Logger


async def main():
    logger: Logger = Logger(name=BEDROCK_SERVER_MANAGER)
    server: BedrockServer = BedrockServer(logger)
    monitor: Monitor = Monitor(logger, server)
    await monitor.poll_players_count(),

    # except asyncio.CancelledError:
    #     server.clean_up()
    # except KeyboardInterrupt:
    #     server.clean_up()


if __name__ == "__main__":
    asyncio.run(main())
