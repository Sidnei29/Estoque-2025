from decimal import Decimal

from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from app_categorias import selecionar_categoria
from models import Produto, Categoria
from decimal import *

def listar(engine: Engine):
    with Session(engine) as session:
        stmt = select(Produto).order_by(Produto.nome)
        produtos = session.execute(stmt).scalars()
        registros = session.execute(stmt).scalars()
        print(" Nome, Preco, estoque.ativo, nome da categoria, Data de cadastro, Data de modificao")
        for produto in produtos:
            print(f"{produto.nome}, {produto.preco}, {produto.estoque},"
            f"{"Ativo" if produto.ativo else "Inativo"}, {produto.categoria.nome}, "
            f"{produto.dta_cadastro}, {produto.dta_atualizacao}")


def remover_produtos(engine: Engine):
    with Session(engine) as session:
        sentenca = select(Produto).order_by(Produto.nome)
        produtos = session.execute(sentenca).scalars()
        dicionario = dict()
        contador = 1
        for p in produtos:
            print(f"{contador}. {p.nome}")
            dicionario[contador] = p.id
            contador += 1
        id = int(input("Digite o numero do produto que deve ser removido:"))
        produto = session.get_one(Produto, dicionario[id])
        session.delete(produto)
        try:
            session.commit()
        except:
            print("Erro na remocao")
        else:
            print("Produto removido com sucesso")


def adicionar_produto(engine: Engine):
    """Função adicional para adicionar produtos"""
    with Session(engine) as session:
        # Obter dados do produto
        p = Produto()
        p.nome = input("Nome do produto: ")
        p.preco = Decimal(input("Preco do produto: "))
        p.estoque = int(input("Qual o estoque inicial do produto?"))
        x = input("O produto esta ativo (S/N)? ").lower()
        p.ativo = True if x [0] == "s" else False
        print("Selecione a categoria do produto")
        p.categoria = selecionar_categoria(session)
        session.add(p)

        try:
            session.commit()
        except ValueError:
            print("Erro na insercao do produto")

        else:
            print("Produto incluido com sucesso")