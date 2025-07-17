import telebot

CHAVE_API = ""

bot = telebot.TeleBot(CHAVE_API)  

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)  
def responder_saudacao(mensagem):
    opções = """ Escolha um opção para seu atendimento( Clique no Item):
    """
    bot.reply_to(mensagem, "Olá! Seja bem-vindo ao BOT Operacional. Estou sendo desenvolvido pelo estudante David Douglas.")

bot.polling()
