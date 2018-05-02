import requests


def create_paste():

    url = 'https://pastebin.com/api/api_post.php'
    api_key = 'a68fad772adb50ba21bb0b6b308787dd'
    is_private = 0
    type = 'JSON'

    content = '{"descricao": "Eu sou o conteudo do post"}'
    title = 'exemplo.json'

    payload = {
        'api_option': 'paste',
        'api_paste_private': is_private,
        'api_paste_name': title,
        'api_paste_format': type,
        'api_dev_key': api_key,
        'api_paste_code': content
    }

    response = requests.post(url, data=payload)
    print(response.text)


def get_user_pastes():
    pass
    #TODO


def call_function():

    opcao = int(input("Escolha uma opção \n 1 - Criar Paste \n 2 - Listar Pastes do usuário \n"))

    if opcao == 1:
        create_paste()

    elif opcao == 2:
        get_user_pastes()


call_function()