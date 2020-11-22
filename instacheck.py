from telethon import TelegramClient, events
from instagramy import InstagramUser

BOT_TOKEN = ''
API_ID = 
API_HASH = ''

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Привет! Я бот-сталкер, покажу тебе информацию о пользователе инстаграм по имени)')
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def inst(event):
    user = InstagramUser(event.text)
    await event.respond(f'Подписчиков: {user.number_of_followers}, Подписок: {user.number_of_followings}, Публикаций: {user.number_of_posts}')

def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
