# TON Price Notifier Bot

This repository contains the Python code for a Telegram bot that provides real-time price updates for TON coin from CoinMarketCap. The bot sends updates both on request and at regular intervals.

## Features

- **Real-time price fetching**: Retrieves the current price of TON coin from CoinMarketCap.
- **Scheduled updates**: Automatically sends the current TON price to a specified chat every 3 minutes.
- **Command responsive**: Reacts to a `/start` command by providing the current price instantly.

## Prerequisites

Before running the bot, you need to install certain Python packages. Make sure Python 3 is already installed on your system, then install the necessary libraries using pip:

```bash
pip3 install requests telebot beautifulsoup4
```

##Configuration
To use the bot, you need to replace the placeholders in the script with your actual Telegram Bot Token and Chat ID:

TOKEN should be set to the token you receive from BotFather when you create your bot on Telegram.
CHAT_ID should be set to the ID of the chat where you want to send the messages.
Running the Bot
Once configured, you can run the bot by executing the script:
```bash
python3 main.py
```
The bot will start in a separate thread for command handling and simultaneously run the timed message function.

##Disclaimer
This bot is for educational purposes only. Always verify financial data through official platforms before making investment decisions.
