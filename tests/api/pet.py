import csv

import pytest       # motor / engine
import requests     # biblioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2' # endereço da API
headers = {'Content-Type': 'application/json'}


def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\ricar\\PycharmProjects\\133pets\\vendors\\csv\\pets_positivo.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


def testar_incluir_pet():
# Configura
    # Dados de entrada: virão do pet1.json
    # Resultado esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Kate'
    tag_esperada = 'Vacinada'


# Executa
    resultado_obtido = requests.post(url=base_url + '/pet',
                  data=open('C:\\Users\\ricar\\PycharmProjects\\133pets\\vendors\\json\\pet1.json', 'rb'),
                  headers=headers
                  )


# Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(f'{corpo_da_resposta}')
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada

def testar_consultar_pet():
    # Configura
    # Dados de entrada
    pet_id = '219641'

    # Resultados Esperados
    status_code_esperado = 200
    nome_pet_esperado = 'Kate'
    tag_esperada = 'Vacinada'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/pet/' + pet_id,
        headers=headers
        )

    #Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada

def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Kate'
    status_esperado = 'solded'

    # Executa
    resultado_obtido = requests.put(
        url=f'{base_url}/pet/',
        data=open('C:\\Users\\ricar\\PycharmProjects\\133pets\\vendors\\json\\pet2.json', 'rb'),
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['status'] == status_esperado

def testar_deletar_pet():
    pet_id = '219641'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '219641'

    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada

@pytest.mark.parametrize('pet_id,categoria_id,category_name,name,tags_id,tags_name,status,status_code', ler_dados_csv())
def testar_incluir_pet_json_dinamico(pet_id,categoria_id,category_name,name,tags_id,tags_name,status,status_code):
    # 1 - Configura
    # 1.1 - Dados de Entrada
    # Utilizará o arquivo pets_positivo.csv


    # 1.2 - Resultados Esperados
    # Utilizará o arquivo pets_positivo.csv

    # 1.3 - Extra - Montar o json dinamicamente a partir do dsv
    #

    # 2 - Executa


    # 3 - Valida





