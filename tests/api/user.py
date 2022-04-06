import pytest       # motor / engine
import requests     # biblioteca para comunicar com A

base_url = 'https://petstore.swagger.io/v2'  # endereço da API
headers = {'Content-Type': 'application/json'}

def testar_incluir_usuario():
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '212786'


# Executa
    resultado_obtido = requests.post(url=base_url + '/user',
                  data=open('C:\\Users\\ricar\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
                  headers=headers
                  )


# Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(f'{corpo_da_resposta}')
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_consultar_usuario():
    user_name = 'ricardo.lopes1980'

    # Resultados Esperados
    status_code_esperado = 200
    user_id = 212786
    firstname = 'Ricardo'
    lastname = 'Lopes'


    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + user_name,
        headers=headers
        )

    #Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['username'] == user_name
    assert corpo_da_resposta['id'] == user_id
    assert corpo_da_resposta['firstName'] == firstname
    assert corpo_da_resposta['lastName'] == lastname

def testar_alterar_usuario():
    user_name = 'ricardo.lopes1980'

    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '212786'

    # Executa
    resultado_obtido = requests.put(
        url=base_url + '/user/' + user_name,
        data=open('C:\\Users\\ricar\\PycharmProjects\\133pets\\vendors\\json\\user2.json', 'rb'),
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

def testar_deletar_usuario():
    user_name = 'ricardo.lopes1980'

    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = 'ricardo.lopes1980'

    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/user/' + user_name,
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