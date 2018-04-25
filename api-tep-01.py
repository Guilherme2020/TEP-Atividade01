import requests
import json

def api_maps():

    chave = 'AIzaSyD5-yvGW_vwld9XnUzJvcQJn9awnYUG5T0'
    localizacao = 'Avenida Homero Castelo Branco'

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (localizacao, chave)


    response = requests.get(url).json()

    #print(json.dump(response,sort_keys=True,fp=))

    print(response)

def github_positions():
    url = 'http://jobs.github.com/positions.json'


    response = requests.get(url).json()
    print(response)

def github_positions_by():
    url = 'https://jobs.github.com/positions.json?description=python'


    response = requests.get(url).json()
    print(response)

#github_positions()

def  call_function():


    opcoes = int(input("Escolha qual funcao executar \n 1-MAPS \n 2- GitHub Jobs \n 3- Github position by \n"))

    if opcoes == 1:
        api_maps()
    elif opcoes == 2:
        github_positions()
    elif opcoes == 3:
        github_positions_by()



call_function()

