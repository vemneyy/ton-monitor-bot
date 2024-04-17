import time

import requests
import telebot
from bs4 import BeautifulSoup

# Токен, полученный от BotFather
TOKEN = '6639135222:AAG7lRs-ksrRXd1mVDRXtnNQBscoJMFZvHg'
CHAT_ID = '-1002105190494'

bot = telebot.TeleBot(TOKEN)


def fetch_ton_price():
    url = 'https://coinmarketcap.com/currencies/toncoin/'
    headers = {'User-Agent': 'Mozilla/5.0'}  # Указываем User-Agent для имитации запроса от браузера
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_block = soup.find('span', class_='sc-f70bb44c-0 jxpCgO base-text')
    if price_block:
        return price_block.text  # Возвращаем текстовое содержимое элемента, содержащего цену
    return "Parse error"


@bot.message_handler(commands=['start'])
def send_price(message):
    price = fetch_ton_price()
    bot.send_message(CHAT_ID, f"{price}")


def timed_message():
    while True:
        price = fetch_ton_price()
        bot.send_message(CHAT_ID, f"{price}")
        time.sleep(180)  # Пауза 3 минуты


if __name__ == '__main__':
    # Запуск бота в отдельном потоке для обработки команд
    import threading

    thread = threading.Thread(target=bot.polling, args=(True,))
    thread.start()
    # Запуск функции регулярной отправки сообщений
    timed_message()
