import telebot
import sqlite3

# Замените TOKEN на токен вашего бота
TOKEN = '7201322190:AAHaZrBlXbyWu3AXqBjS9dpXWxTjTQYAiEA'
bot = telebot.TeleBot(TOKEN)

# Вопросы и ответы
questions = [
    {"question": "Как зовут нашего кота?", "answer": "Маня"},
    {"question": "Когда у нас годовщина?", "answer": "27 сентября"},
]

user_answers = {}
SECRET_KEY = "secret123"  # Ключ для логина
SITE_URL = "http://127.0.0.1:5000/"  # Адрес сайта для логина


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_answers[chat_id] = []
    bot.send_message(chat_id, "Привет! Я задам тебе пару вопросов.")

    # Первый вопрос
    ask_question(chat_id, 0)

# Задаём вопрос
def ask_question(chat_id, question_index):
    if question_index < len(questions):
        question = questions[question_index]["question"]
        bot.send_message(chat_id, question)
        bot.register_next_step_handler_by_chat_id(chat_id, lambda msg: check_answer(msg, question_index))
    else:
        # Проверяем все ответы
        check_all_answers(chat_id)

# Проверяем ответ на конкретный вопрос
def check_answer(message, question_index):
    chat_id = message.chat.id
    answer = message.text

    if answer.lower() == questions[question_index]["answer"].lower():
        user_answers[chat_id].append(True)
    else:
        user_answers[chat_id].append(False)

    # Задаём следующий вопрос или проверяем результаты
    ask_question(chat_id, question_index + 1)

# Проверяем все ответы и выдаём ключ
def check_all_answers(chat_id):
    if all(user_answers[chat_id]):
        bot.send_message(chat_id, 
            f"Поздравляю! Вот твой ключ: {SECRET_KEY}\n"
            f"Перейди на {SITE_URL} и введи его, чтобы войти."
        )
    else:
        bot.send_message(chat_id, "Увы, что-то пошло не так. Попробуй снова.")

# Запуск бота
if __name__ == "__main__":
    bot.polling()
