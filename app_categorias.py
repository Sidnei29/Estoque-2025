from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from models import Categoria
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from models import Categoria

def listar(engine: Engine):
    with Session(engine) as session:
        sentences = select(Categoria)
        registros = session.execute(sentences).scalars()
        print("ID, Nome, #produtos")
        for categoria in registros:
            print(f"{categoria.id}, {categoria.nome}, {len(categoria.lista_de_produtos)}")


def adicionar(engine: Engine):
    with Session(engine) as session:
        nome = input("Nome da categoria: ")
        categoria = Categoria()
        categoria.nome = nome
        session.add(categoria)
        try:
            session.commit()
        except:
            print("Erro na insercao")
        else:
            print("Categoria adicionada ")
def selecionar_categoria (session: Session) -> Categoria:
    sentenca = select(Categoria).order_by(Categoria.nome)
    categorias = session.execute(sentenca).scalars()
    dicionario = dict()
    contador = 1
    for c in categorias:
        print(f"{contador} - {c.nome}")
        dicionario[contador] = c.id
        contador += 1
    id = int(input("Digite o numero da categoria que deve ser alterada"))
    categoria = session.get_one(Categoria, dicionario[id])
    return categoria


def modificar(engine: Engine):
    with Session(engine) as session:
        categoria = selecionar_categoria(session)
        nome = input("Digite o nome da categoria: ")
        categoria.nome = nome
        try:
            session.commit()
        except:
            print("Erro na atualizacao")

        else:
            print("Categoria removida com sucesso")


def remover(engine: Engine):
    with Session(engine) as session:
        categoria = selecionar_categoria(session)
        session.delete(categoria)
        try:
            session.commit()

        except:
            print("Erro na remocao")

        else:
            print("Categoria removida com sucesso")
