import re

BEDROCK_SERVER_MANAGER = "BedrockServerManager"
SERVER_DIRECTORY = "bedrock-server"
SERVER_BINARY = "./bedrock_server"
SERVER_LOG_PATH = "logs/server.log"
WRAPPER_LOG_PATH = "logs/wrapper.log"

T_MONITOR_MAX_RETRY = 2
T_MONITOR_INTERVAL = 300.0
T_POLL_LOG_INTERVAL = 0.01

R_PLAYERS_COUNT = re.compile(r"There are (\d+)/\d+ players online")

C_STOP = "stop"
C_LIST = "list"

M_COMMAND_TIMED_OUT = "Command timed out!"
M_SENT = "#SENT"
M_WRAPPER_STARTED = "Wrapper script started."
M_WRAPPER_STOPPED = "Wrapper script stopped."
M_SERVER_STARTED = "Sever started."
M_SERVER_STOPPED = "Sever stopped."
M_SERVER_CLEANUP = "Cleaning up server."
M_FAILED_TO_PARSE_PLAYERS_COUNT = "Failed to parse player count: {text}"
M_ALREADY_STOPPED = "Already stopped."
M_ALREADY_STOPPED_WITH = "Already stopped with return code: {code}"
M_TIMED_OUT_AFTER = "Timed out after: {timeout}"
