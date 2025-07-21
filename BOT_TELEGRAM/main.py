import os, sys, requests, platform, time
from chave_bot import API_TOKEN  # Importa corretamente o token

# Usa o token importado
strURLBase = f'https://api.telegram.org/bot{API_TOKEN}'
strURLGetUpdates = f'{strURLBase}/getUpdates'
strURLSendMessage = f'{strURLBase}/sendMessage'

# Limpa a tela
os.system('cls' if platform.system() == 'Windows' else 'clear')

print('\nBOT TELEGRAM - Aguardando mensagens...')


intIDUltimaMensagem = 0

while True:
    # Obtém as mensagens com offset
    params = {'offset': intIDUltimaMensagem + 1}
    reqURL = requests.get(strURLGetUpdates, params=params)

    if reqURL.status_code != 200:
        sys.exit('\nERRO: Erro ao obter mensagens...\nCÓDIGO DE RETORNO: ' + str(reqURL.status_code))

    jsonRetorno = reqURL.json()

    if not jsonRetorno['result']:
        time.sleep(1)
        continue

    for mensagem in jsonRetorno['result']:
        intIDUltimaMensagem = mensagem['update_id']
        if 'message' not in mensagem:
            continue

        strComando = mensagem['message'].get('text', '')
        intIDChat = mensagem['message']['chat']['id']

        if strComando == '/?':
            strMensagemRetorno = f'BOT: Texto de Ajuda...\nUsuário:{intIDChat}'
        elif strComando == '/start':
            strMensagemRetorno = f'BOT: Bem-vindo ao BOT do Estudante David Douglas...\nUsuário:{intIDChat}'
        else:
            strMensagemRetorno = f'BOT: Comando não reconhecido, por favor tente novamente ...\nUsuário:{intIDChat}'

        dictDados = {'chat_id': intIDChat, 'text': strMensagemRetorno}
        respEnvio = requests.post(strURLSendMessage, data=dictDados)

        if respEnvio.status_code != 200:
            print('\nERRO ao enviar mensagem...\nCÓDIGO:', respEnvio.status_code)

    time.sleep(1)
