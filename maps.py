import requests


def get_address():

    chave = 'AIzaSyD5-yvGW_vwld9XnUzJvcQJn9awnYUG5T0'
    localizacao = 'Avenida Homero Castelo Branco'

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (localizacao, chave)

    response = requests.get(url).json()
    print(response)



if __name__ == '__main__':
    get_address()
