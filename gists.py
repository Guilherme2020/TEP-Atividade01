import requests
from requests.auth import HTTPBasicAuth


def get_user_pastes():
    url = 'https://api.github.com/users/brunoserra/gists'

    response = requests.get(url).json()

    print(response)


def create_gist():
    url = 'https://api.github.com/gists'

    payload = {
          "description": "Gist para aula de TEP",
          "public": True,
          "files": {
            "tep.txt": {
              "content": "topicos especiais de programação"
            }
          }
        }

    response = requests.post(url, json=payload, auth=HTTPBasicAuth('user', 'password')).json()
    print(response)


def call_function():

    opcao = int(input("Escolha uma opção \n 1 - Criar Paste \n 2 - Listar Pastes do usuário \n"))

    if opcao == 1:
        create_gist()

    elif opcao == 2:
        get_user_pastes()


if __name__ == '__main__':
    call_function()
