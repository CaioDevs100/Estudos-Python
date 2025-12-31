
# Função para ler cidades de um arquivo texto
def ler_cidades():
    # Lista para armazenar as cidades lidas
    cidades = []
    # Abre o arquivo cidades.txt em modo de leitura
    for linha in open('cidades.txt', 'r'):
        # Adiciona cada cidade à lista, removendo espaços em branco .strip() e convertendo para minúsculas .lower()
        cidades.append(linha.strip().lower())
    # Retorna a lista de cidades lidas
    return cidades