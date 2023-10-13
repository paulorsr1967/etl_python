# Importar as bibliotecas
import pandas as pd
import requests

# Definir uma função para consultar a API do ViaCep e retornar o endereço completo
def obter_endereco(cep):
    # Remover caracteres especiais do CEP
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")
    # Verificar se o CEP tem 8 dígitos
    if len(cep) == 8:
        # Montar o link da API Via CEP com o CEP desejado
        link = f"https://viacep.com.br/ws/{cep}/json/"
        # Fazer a requisição à API e obter os dados em formato JSON
        requisicao = requests.get(link)
        dados = requisicao.json()
        # Extrair as informações de interesse do JSON
        if requisicao.status_code == 200:
            uf = dados["uf"]
            cidade = dados["localidade"]
            bairro = dados["bairro"]
            logradouro = dados["logradouro"]
            # Montar o endereço completo como uma string
            endereco = f"{logradouro}, {bairro}, {cidade} - {uf}"
        else:
            # define mensagem de erro para CEP não encontrado
            endereco = "CEP não encontrado"
    else:
        # define mensagem de erro para CEP incompleto
        endereco = "CEP inválido"
    return endereco

# Ler o arquivo clientes.csv e armazenar em um DataFrame
df = pd.read_csv("c:/users/dilly/OneDrive/Paulo/python/clientes.csv")
# Aplicar a função na coluna CEP do DataFrame e criar/atualizar a coluna endereco
df["endereco"] = df["cep"].apply(obter_endereco)
# Gravar o DataFrame modificado em um novo arquivo CSV
df.to_csv("clientes.csv", index=False)
