import contextlib
import asyncio 
from aiogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import link
from aiogram import Bot, Dispatcher, F
import logging



BOT_TOKEN = '5782607808:AAG6LpY2BUj25r1UeeWcBGNP8q7wOmZFVLQ' 
CHANNEL_ID =  -1001712236318
ADMIN_ID = 1889004772
async def approve_request (chat_join: ChatJoinRequest, bot: Bot):
   text = link('https://t.me/globalprofit', 'https://t.me/+YigHdJ6h1ck3YmQy')
   msg= f"Дорогой друг, поздравляем тебя с приобретением подписки на закрытое сообщество PROFIT.\n\nВы можете войти в канал: {text}"
   button = InlineKeyboardButton(text='ВСТУПИТЬ', url='https://t.me/+eWU1DCA0sEdhYjk6', disable_web_page_preview=True)   
   markup = InlineKeyboardMarkup(inline_keyboard=[[button]])



   await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)
 

async def start():
    logging.basicConfig(level=logging.DEBUG,
                           format="%(asctime)s - [%(levelname)s] - %(name)s -"
                           "(%(filename)s.%(funcName)s(%(lineo)d) - %(message)s"
                        )
    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher ()
    dp.chat_join_request.register (approve_request, F.chat.id ==CHANNEL_ID)

    try:
     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
     logging.error( exc_info=True)
    finally:
     await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
