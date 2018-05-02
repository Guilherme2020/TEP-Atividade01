import requests

def get_positions():
    url = 'http://jobs.github.com/positions.json'


    response = requests.get(url).json()
    print(response)


def get_positions_by():
    url = 'https://jobs.github.com/positions.json?description=python'


    response = requests.get(url).json()
    print(response)


def call_function():

    opcoes = int(input("Escolha uma opção \n 1 - Cargos \n 2 - Cargos com Filtro \n"))

    if opcoes == 1:
        get_positions()

    elif opcoes == 2:
        get_positions_by()

if __name__ == '__main__':
    call_function()
