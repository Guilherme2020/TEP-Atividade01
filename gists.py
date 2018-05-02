import requests

#api_key = 'my-pastebin-key'



def get_user_pastes():
    url = 'https://api.github.com/users/brunoserra/gists'


    response = requests.get(url).json()


    print(response)


def call_function():

    opcao = int(input("Escolha uma opção \n 1 - Criar Paste \n 2 - Listar Pastes do usuário \n"))

    if opcao == 1:
        #create_paste()
        pass
    elif opcao == 2:
        get_user_pastes()



if __name__ == '__main__':
    call_function()
