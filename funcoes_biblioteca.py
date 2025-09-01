import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = 0
        self.genero = ""

biblioteca = []

def cadastrar_livro(titulo, autor, ano, genero="", quantidade=1):
    novo_livro = Livro(titulo, autor, ano)
    novo_livro.genero = genero
    novo_livro.quantidade = quantidade
    biblioteca.append(novo_livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')

def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
        return
    for livro in biblioteca:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")

def buscar_livro_por_titulo(titulo_busca):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_busca.lower():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")
            return
    print("Livro não encontrado.")

def grafico_livro():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
        return

    contador_generos = {}
    for livro in biblioteca:
        if livro.genero in contador_generos:
            contador_generos[livro.genero] += livro.quantidade
        else:
            contador_generos[livro.genero] = livro.quantidade

    generos = list(contador_generos.keys())
    quantidades = list(contador_generos.values())

    plt.figure(figsize=(8,5))
    plt.bar(generos, quantidades, color='skyblue')
    plt.title('Quantidade de livros por gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.show()

# Teste do sistema
cadastrar_livro("Dom Quixote", "Miguel de Cervantes", "1605", "Clássico", 3)
cadastrar_livro("1984", "George Orwell", "1949", "Distopia", 5)
cadastrar_livro("O Hobbit", "J.R.R. Tolkien", "1937", "Fantasia", 4)
cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "1954", "Fantasia", 2)

listar_livros()
buscar_livro_por_titulo("1984")
grafico_livro()
