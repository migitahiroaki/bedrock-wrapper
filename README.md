# bedrock-wrapper

## Introduction

This is a command wrapper for the Minecraft Bedrock server.

It launches the server as a subprocess.  
Every 5 minutes, it checks the number of connected players.  
If there are no players online, it shuts down the server safely.

## Installation

1. Clone this repository.
2. Download the Bedrock server binary from the [official site](https://www.minecraft.net/download/server/bedrock).
3. Unzip the downloaded server into the project directory and name the folder `bedrock-server`.

> ⚠️ Note: The server binary is **not** included in this repository.

## Notes

- Automatic updates are **not** implemented.  
  Please update the server binary manually when needed.
- If you are running this on AWS (e.g., EC2), it is recommended to monitor the files under the `logs/` directory using **CloudWatch Agent** for centralized logging.
- 📝 For issues or contact: Please feel free to write in **Japanese**. 日本語でおｋ
