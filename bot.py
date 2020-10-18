import config
import telebot
from rate_get import FilmRate, AnimeRate


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)  # делаем стартовую клаву
keyboard1.row('Фильм', 'Аниме')
sm = 'Ну что, начнём? Выбери, что ты хочешь посмотреть'  # стартовое сообщение

film_name = ''
anime_name = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, sm, reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def fora(message):
    if message.text.lower() == 'фильм':
        bot.send_message(message.chat.id, 'Напиши название фильма')
        # фиксируем следующее сообщение пользователя и переходим к функции get_film_rate
        bot.register_next_step_handler(message, get_film_rate)

    elif message.text.lower() == 'аниме':
        bot.send_message(message.chat.id, 'Напиши название аниме')
        # фиксируем следующее сообщение пользователя и переходим к функции get_anime_rate
        bot.register_next_step_handler(message, get_anime_rate)

    else:
        bot.send_message(message.chat.id, 'С такими сообщениями тебе к другим ботам :Р')


def get_film_rate(message):
    global film_name
    film_name = message.text.lower()
    film = FilmRate(film_name)
    try:
       kai = film.gfr_KpIm()
       #mc = film.gfr_MC()
       #rt = film.gfr_RT()
    except:
        bot.send_message(message.chat.id, "Запрос не прошёл, походу ошибка в названии")
    #rt1 = rt.replace('%', '')
    #wsum = (float(kai[0]) + float(kai[1]) + ((float(rt1)/10) + float(mc)))/4
    wsum = (float(kai[0]) + float(kai[1]))/2
    #all = f'Рэйтинг Кинопоиска: {kai[0]}\nРэйтинг IMBD: {kai[1]}\nРэйтинг Rotten Tomatoes: {rt}\n\
#Рэйтинг MetaCritic: {mc}\nОбщий рэйтинг: {wsum:.2f}'
    coment = ''
    if wsum < 5:
        coment = 'Чел, очень не советую, ты скорее всего потратишь своё время'
    elif 5 < wsum < 7:
        coment = 'Неплохой фильмец, с попкорном покатит'
    else:
        coment = 'Отличный выбор, ты точно не потратишь своё время'
    all = f'Рэйтинг [Кинопоиска](https://www.kinopoisk.ru/film/{kai[2]}/): {kai[0]}\nРэйтинг IMBD: {kai[1]}\nОбщий рэйтинг: {wsum:.2f}\n{coment}'
    bot.send_message(message.chat.id, all, parse_mode='Markdown')


def get_anime_rate(message):
    global anime_name
    anime_name = message.text.lower()
    anime = AnimeRate(anime_name)
    try:
        ar = anime.get_anime_rate()
    except:
        bot.send_message(message.chat.id, "Запрос не прошёл, походу ошибка в названии")
    if float(ar[0]) < 5:
        coment = 'Воу, а ты любитель отборного говнеца!'
    elif 5 < float(ar[0]) < 8:
        coment = 'Это конечно не студия Гибли, но тоже хороший выбор'
    else:
        coment = 'Миядзаки плакал, когда пересметривал это аниме в 100 раз'
    bot.send_message(message.chat.id, f'Рэйтинг с\
 [самого лучшего аниме сайта](https://yummyanime.club/catalog/item/{ar[1]}): {ar[0]}\n{coment}', parse_mode='Markdown')


if __name__ == '__main__':
    bot.infinity_polling()

