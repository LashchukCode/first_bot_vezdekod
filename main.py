from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import config
import strings

bot = SimpleLongPollBot(tokens=config.TOKEN, group_id=config.PUBLIC_ID)


@bot.message_handler()
async def first(event: SimpleBotEvent) -> str:
    if event.object.object.message.text in ['Привет', 'Hello']:
        await event.answer(strings.msg_privet_otv)

if __name__ == '__main__':
    bot.run_forever()
