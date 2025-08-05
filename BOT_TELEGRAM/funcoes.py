import requests

def setor_x(chat_id, API_TOKEN, texto_usuario):
    url_send = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'

    # Se o usuário só enviou a mensagem inicial ou mensagem vazia, envia o teclado
    if texto_usuario not in [
        "Falar sobre problema no aplicativo do banco",
        "Falar sobre problema no aplicativo do ponto",
        "Falar sobre outra situação"
    ]:
        apresentacao_x = "Em que posso ajudar? Selecione um dos atendimentos abaixo:"
        
        teclado = {
            "keyboard": [
                ["Falar sobre problema no aplicativo do banco"],
                ["Falar sobre problema no aplicativo do ponto"],
                ["Falar sobre outra situação"]
            ],
            "one_time_keyboard": True,
            "resize_keyboard": True
        }

        dados = {
            "chat_id": chat_id,
            "text": apresentacao_x,
            "reply_markup": teclado
        }
        try:
            response = requests.post(url_send, json=dados)
            if response.status_code != 200:
                print("Erro ao enviar teclado:", response.text)
        except requests.RequestException as e:
            print("Erro na requisição:", e)

    else:
        # Resposta específica conforme a escolha do usuário
        if texto_usuario == "Falar sobre problema no aplicativo do banco":
            resposta = "Você escolheu falar sobre problema no aplicativo do banco. Aguarde que em breve irei ajudar, peço que já encaminhe o extrato da conta."
        elif texto_usuario == "Falar sobre problema no aplicativo do ponto":
            resposta = "Problema no aplicativo do ponto. Já informe seu nome completo, e o email que você utiliza"
        elif texto_usuario == "Falar sobre outra situação":
            resposta = " Por favor, detalhe sua situação."

        dados = {
            "chat_id": chat_id,
            "text": resposta,
            "reply_markup": {"remove_keyboard": True}  # Remove o teclado após a escolha
        }
        try:
            response = requests.post(url_send, json=dados)
            if response.status_code != 200:
                print("Erro ao enviar resposta:", response.text)
        except requests.RequestException as e:
            print("Erro na requisição:", e)

    return "Setor X"
