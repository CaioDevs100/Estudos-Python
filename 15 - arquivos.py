
# Função para ler um arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r") # Abre o arquivo no modo leitura
    conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
    print(conteudo) 
    arquivo.close() # Fecha o arquivo após a leitura
    print(f"Lendo o arquivo: {nome_arquivo}") # Imprime o nome do arquivo lido, f identificador de formato
    print (conteudo)

# Função para escrever em um arquivo
def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "w") # Abre o arquivo no modo escrita
    arquivo.write(conteudo) # Escreve o conteúdo no arquivo, write serve para criar ou sobrescrever
    arquivo.close() # Fecha o arquivo após a escrita
    print(f"Escrevendo no arquivo: {nome_arquivo}") 
    print (conteudo)

# Função para adicionar conteúdo a um arquivo existente
def adicionar_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "a") # Abre o arquivo no modo append (adicionar) usnado "a" 
    arquivo.write(conteudo)  # Adiciona o conteúdo ao final do arquivo
    arquivo.close() # Fecha o arquivo após adicionar o conteúdo

# Função para ler um arquivo linha a linha
def ler_linha_arquivo(nome_arquivo):
    print(f"Lendo o arquivo linha a linha: {nome_arquivo}")
    for linha in open(nome_arquivo, "r"): # Abre o arquivo no modo leitura
        # Lê cada linha, strip remove espaços em branco e capitalize deixa a primeira letra maiúscula
        print(f"=>{linha.strip().capitalize()}") 

# Testando as funções criadas
# Lendo o arquivo
ler_arquivo("cidades.txt")
# Escrevendo no arquivo
escrever_arquivo("cidades.txt", "carapicuiba\n")
# Lendo o arquivo após escrever
ler_arquivo("cidades.txt")
# Adicionando uma cidade
adicionar_arquivo("cidades.txt", "sobral\n")
# Adicionando mais uma cidade
adicionar_arquivo("cidades.txt", "juazeiro do norte\n")
# Lendo o arquivo completo novamente
ler_arquivo("cidades.txt")
# Lendo linha a linha
ler_linha_arquivo("cidades.txt")

