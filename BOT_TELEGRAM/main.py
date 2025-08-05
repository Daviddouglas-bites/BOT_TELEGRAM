import os, sys, requests, platform, time
from chave_bot import API_TOKEN
from funcoes import setor_x  # ✅ Novo import

# URLs do bot
strURLBase = f'https://api.telegram.org/bot{API_TOKEN}'
strURLGetUpdates = f'{strURLBase}/getUpdates'

# Limpa a tela
os.system('cls' if platform.system() == 'Windows' else 'clear')
print('\nBem vindo em que posso ajudar? - Aguardando mensagens...')

intIDUltimaMensagem = 0

while True:
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

        # ✅ Chama a função externa
        setor_x(intIDChat, API_TOKEN)

    time.sleep(1)
