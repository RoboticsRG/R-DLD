import csv
import os
import requests



def baixar_arquivo(arquivo_csv, diretorio_destino):
    # Abre o arquivo CSV para leitura
    # print(arquivo_csv)
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')
        # Itera sobre as linhas e imprime a quarta coluna
        for linha in leitor:
            if len(linha) >= 4:  # Verifica se a linha tem pelo menos 4 colunas
                # print(linha[3])
                nome = linha[3].split("/")[-1]
                app_path = os.path.join(diretorio_destino, nome)
                request_url(linha[3], app_path)


def baixar_arquivos_csv(origem, destino):
    # Verifica se a pasta de destino existe, caso contrário, cria
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Lista todos os arquivos na pasta de origem
    for nome_arquivo in os.listdir(origem):
        arquivo_csv = os.path.join(origem, nome_arquivo)

        # Verifica se é um arquivo
        if os.path.isfile(arquivo_csv):
            # Nome do diretório será o nome do arquivo (sem extensão)
            nome_diretorio = os.path.splitext(nome_arquivo)[0]
            diretorio_destino = os.path.join(destino, nome_diretorio)

            # Cria o diretório
            if not os.path.exists(diretorio_destino):
                os.makedirs(diretorio_destino)
            # print('sss'+arquivo_csv)
            baixar_arquivo(arquivo_csv, diretorio_destino)


def request_url(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
        print("Download finalizado {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    # Defina o caminho para a pasta de origem e destino
    pasta_origem_csv = '/home/davi/projetos_git/experimento_dld/excluir/'
    pasta_destino_apks = '/home/davi/projetos_git/experimento_dld/excluir/teste'

    baixar_arquivos_csv(pasta_origem_csv, pasta_destino_apks)




# if __name__ == "__main__":
#     # Substitua 'dados.csv' pelo caminho para o seu arquivo CSV
#     arquivo_csv = '/home/davi/projetos_git/experimento_dld/files2024/connectivity.csv'
#     imprimir_quarta_coluna(arquivo_csv)
