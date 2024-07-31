import json
import numpy as np
import os
from datetime import datetime

fileName = '/home/jpedro/empresa/respostasFormulario.json'


def write_json(new_data, filename= fileName):
    """
    Atualiza ou cria um arquivo JSON com os dados fornecidos.

    Esta função verifica se o arquivo JSON especificado existe. Se não existir, cria um arquivo JSON vazio. 
    Em seguida, carrega os dados existentes no arquivo, atualiza esses dados com os novos dados fornecidos, 
    e grava os dados atualizados de volta no arquivo JSON.

    Parâmetros:
    new_data (dict): Um dicionário contendo os novos dados a serem adicionados ou atualizados no arquivo JSON.
    filename (str, opcional): O caminho para o arquivo JSON. O padrão é o valor da variável global `fileName`.

    Comportamento:
    - Se o arquivo JSON não existir, ele será criado como um JSON vazio.
    - O arquivo JSON existente será carregado e atualizado com os dados fornecidos.
    - O arquivo será sobrescrito com os dados atualizados, e seu conteúdo antigo será removido.
    """

    if not os.path.isfile(filename):
        # Se o arquivo não existir, cria um novo arquivo vazio
        with open(filename, 'w') as file:
            json.dump({}, file)  # Cria um JSON vazio no arquivo


    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)


def not_empty(prompt):
    """
    Solicita uma entrada do usuário e garante que não seja deixada em branco.

    Esta função exibe um prompt ao usuário e solicita que ele insira uma resposta. A função continua solicitando 
    a entrada até que o usuário forneça uma resposta não vazia.

    Parâmetros:
    prompt (str): A mensagem a ser exibida ao usuário para solicitar a entrada.

    Retorna:
    str: A entrada do usuário, garantida para não ser vazia.

    Comportamento:
    - Se a entrada do usuário estiver vazia, exibe uma mensagem de erro e solicita a entrada novamente.
    """

    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Esta pergunta não pode ser deixada em branco. Por favor, tente novamente.")



date = str(datetime.now())
date = date[0:16]


dictTemp = {}

dictTemp[date]= { 
    "pergunta1": not_empty('Pergunta 1:'),
    "pergunta2": not_empty('Pergunta 2:'), 
    "pergunta3": not_empty('Pergunta 3:'),
    "pergunta4": not_empty('Pergunta 4:'),
    "pergunta5": not_empty('Pergunta 5:'),
    "pergunta6": not_empty('Pergunta 6:')
    }

write_json(dictTemp)
