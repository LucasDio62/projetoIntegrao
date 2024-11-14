from datetime import datetime

# Classe Produto
class Produto:
    def _init_(self, id_produto, nome, preco, quantidade, categoria):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
    def atualizar_estoque(self, quantidade):
        self.quantidade += quantidade


# Classe Categoria
class Categoria:
    def _init_(self, id_categoria, nome):
        self.id_categoria = id_categoria
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)


# Classe Movimentação
class Movimentacao:
    def _init_(self, produto, tipo, quantidade, data=None):
        self.produto = produto
        self.tipo = tipo # 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data = data if data else datetime.now()


# Classe Sistema de Gerenciamento
class SistemaGerenciamento:
    def _init_(self):
        self.produtos = {}
        self.categorias = {}
        self.movimentacoes = []

    # Cadastrar Produto
    def cadastrar_produto(self, id_produto, nome, preco, quantidade, id_categoria):
        if id_categoria in self.categorias:
            categoria = self.categorias[id_categoria]
            produto = Produto(id_produto, nome, preco, quantidade, categoria)
            self.produtos[id_produto] = produto
            categoria.adicionar_produto(produto)
            print(f"Produto '{nome}' cadastrado com sucesso!")
        else:
            print("Categoria não encontrada")

    # Cadastrar Categoria
    def cadastrar_categoria(self, id_categoria, nome):
        if id_categoria not in self.categorias:
            categoria = Categoria(id_categoria, nome)
            self.categorias[id_categoria] = categoria
            print(f"Categoria '{nome}' cadastrada com sucesso!")
        else:
            print("Categoria já existe")

    # Registrar Movimentação de Entrada ou Saída
    def registrar_movimentacao(self, id_produto, tipo, quantidade):
        if id_produto in self.produtos:
            produto = self.produtos[id_produto]
            if tipo == 'saida' and produto.quantidade < quantidade:
                print("Quantidade insuficiente no estoque")
            else:
                produto.atualizar_estoque(quantidade if tipo == 'entrada' else -quantidade)
                movimentacao = Movimentacao(produto, tipo, quantidade)
                self.movimentacoes.append(movimentacao)
                print(f"Movimentação de {tipo} registrada para o produto {produto.nome}")
        else:
            print("Produto não encontrado")

    # Consultar Produto
    def consultar_produto(self, id_produto):
        produto = self.produtos.get(id_produto)
        if produto:
            info = {
                "ID": produto.id_produto,
                "Nome": produto.nome,
                "Preço": produto.preco,
                "Quantidade": produto.quantidade,
                "Categoria": produto.categoria.nome
            }
            return info
        else:
            print("Produto não encontrado")
            return None

    # Consultar Estoque Geral
    def consultar_estoque(self):
        estoque = {id_produto: produto.quantidade for id_produto, produto in self.produtos.items()}
        return estoque

    # Gerar Relatório de Movimentações
    def gerar_relatorio_movimentacoes(self):
        relatorio = []
        for mov in self.movimentacoes:
            info = {
                "Produto": mov.produto.nome,
                "Tipo": mov.tipo,
                "Quantidade": mov.quantidade,
                "Data": mov.data.strftime("%Y-%m-%d %H:%M:%S")
            }
            relatorio.append(info)
        return relatorio

    # Consultar Histórico de Movimentações de um Produto
    def consultar_historico_produto(self, id_produto):
        historico = []
        for mov in self.movimentacoes:
            if mov.produto.id_produto == id_produto:
                info = {
                    "Tipo": mov.tipo,
                    "Quantidade": mov.quantidade,
                    "Data": mov.data.strftime("%Y-%m-%d %H:%M:%S")
                }
                historico.append(info)
        if not historico:
            print("Nenhuma movimentação encontrada para o produto")
        return historico