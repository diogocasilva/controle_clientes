import sqlite3

db = 'promissoria.db'



def novo_cliente(cpf, nome, sexo,telefone,cidade,estado,endereco,cep,conta):
    with sqlite3.connect(db) as conexao:
        sql = f'insert into promissoria (cpf, nome, sexo,telefone,cidade,estado,endereco,cep,conta)'\
              f' values ("{cpf}", "{nome}", "{sexo}", "{telefone}", "{cidade}", "{estado}", "{endereco}", "{cep}", "{conta}")'
        # Cria a conexao
        conexao.execute(sql)
        conexao.commit()


def buscar_cliente_por_cpf(cpf):
    with sqlite3.connect(db) as conexao:
        sql = f"select * from promissoria where cpf='{cpf}'"
        cursor_cliente = conexao.execute(sql)
        # conexao.close()
        return cursor_cliente.fetchone()

def buscar_cliente_por_nome(nome):
    with sqlite3.connect(db) as conexao:
        sql = f"select * from promissoria where nome='{nome}'"
        cursor_cliente = conexao.execute(sql)
        # conexao.close()
        return cursor_cliente.fetchone()


def mostrar_todos():
    with sqlite3.connect(db) as conexao:
        sql = f'select * from promissoria'
        cursor_cliente = conexao.execute(sql)
        return cursor_cliente.fetchall()


def alterar_cliente(nome, sexo,telefone,cidade,estado,endereco,cep,conta, cpf_busca):
    with sqlite3.connect(db) as conexao:
        sql = f"update promissoria set nome='{nome}'," \
              f"sexo='{sexo}',telefone={telefone}," \
              f"cidade='{cidade}',estado='{estado}',endereco='{endereco}',cep={cep},conta={conta}" \
              f"={telefone} where cpf={cpf_busca}"
        conexao.execute(sql)
        conexao.commit()



def excluir_cliente(cpf):
    with sqlite3.connect(db) as conexao:
        sql = f'delete from promissoria where cpf={cpf}'
        conexao.execute(sql)
        conexao.commit()





