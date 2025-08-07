import cmd

from sqlalchemy import create_engine

import app_categorias
from config import read_config


if __name__ == '__main__':
    config = read_config()
    engine = create_engine(url=config.url_bd, echo=False)

    while True:
        print("MENU")
        print("=================")
        print("1. Listar categorias")
        print("0. Finalizar")
        print("2. Adicionar categoria")
        print("3. Modificar categoria")
        print("4. Remover categoria")

        print("0. Finalizar")
        opcao = input("Digite a opcao desejada:")
        match opcao:
            case "1":
                app_categorias.listar(engine)
            case "2":
                app_categorias.adicionar(engine)
            case "3":
                app_categorias.modificar(engine)
            case "4":
                app_categorias.remover(engine)

            case "0":
                exit()



