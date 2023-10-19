from datetime import date
import connect
import models


def verificaNull(data):
    if (data == None):
        return 'null'
    return f"'{data}'"


# Altera o status do conveniado na loja
def exec_altera_status_conv_loja(status, cd_cliente):
    con = connect.connect_loja()
    cursor = con.cursor()
    update = models.alteraStatusConv(status, cd_cliente)

    cursor.execute(update)

    con.commit()
    con.close()


# altera o statud do conveniado no Sql Server
def exec_altera_status_conv_server(status, cd_cliente):
    con = connect.sqlServer()
    cursor = con.cursor()
    update = models.alteraStatusConv(status, cd_cliente)

    cursor.execute(update)

    con.commit()
    con.close()


# Retorna o usuario cadastrado no postgres
def exec_retornaUsuarioPostgres(id):
    con_pg = connect.connect_pg()
    cursor = con_pg.cursor()
    select = models.retornaUsuarioPostgres(id)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'primeiro_nome': row[0],
            'cd_conv': row[1],
            'cd_cli': row[2]
        }
        row = cursor.fetchone()

    con_pg.commit()
    con_pg.close()

    return DIC


# Retorna o usuario cadastrado no SQLSERVER
def exec_retornaUsuarioSQLSERVER(cd_conv, cpf):
    con = connect.sqlServer()
    cursor = con.cursor()
    select = models.retornaUsuarioSQLServer(cd_conv, cpf)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'cd_cli': row[0]
        }
        row = cursor.fetchone()

    con.commit()
    con.close()

    return DIC


# grava o token novo na tabela de tokens
def exec_insert_tabela_token(cd_cli, cd_conv, token, hora_cria_token, sts_token):
    con = connect.connect_pg()
    cursor = con.cursor()
    insert = models.insert_tabela_token(cd_cli, cd_conv, token, hora_cria_token, sts_token)

    cursor.execute(insert)

    con.commit()
    con.close()


def exec_select_tabela_token(cd_cli, cd_conv):
    con = connect.connect_pg()
    cursor = con.cursor()
    select = models.select_tabela_token(cd_cli, cd_conv)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'TOKEN': row[0],
            'DT_CRIA_TOKEN': row[1]
        }
        row = cursor.fetchone()

    con.commit()
    con.close()

    return DIC


# Ativa conveniado em loja
def exec_ativa_cliente_loja(cd_cli, cd_conv):
    con = connect.connect_teste()  # alterar para conexão de loja
    cursor = con.cursor()
    update = models.update_ativa_cliente(cd_cli, cd_conv)

    cursor.execute(update)

    con.commit()
    con.close()


# ativa conveniado no banco retaguarda
def exec_ativa_cliente_retaguarda(cd_cli, cd_conv):
    con = connect.sqlServer()  # alterar para conexão de loja
    cursor = con.cursor()
    update = models.update_ativa_cliente(cd_cli, cd_conv)

    cursor.execute(update)

    con.commit()
    con.close()


# retorar token caso exista um igual ativo
def exec_select_tabela_token_pelo_token(token):
    con = connect.connect_heroku()
    cursor = con.cursor()
    select = models.select_tabela_token_pelo_token(token)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'TOKEN': row[0],
            'CD_CLI': row[1],
            'CD_CONV': row[2]
        }
        row = cursor.fetchone()

    con.commit()
    con.close()

    return DIC


def exec_select_usuario_lideranca(cd_usu):
    con = connect.sqlServer()
    cursor = con.cursor()
    select = models.select_usuario_lideranca(cd_usu)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'CD_USU': row[0],
            'NM_USU': row[1].capitalize(),
            'CD_FILIAL': row[2]
        }
        row = cursor.fetchone()

    con.commit()
    con.close()

    return DIC


def exec_select_senha_conv(key):
    con = connect.connect_pg()
    cursor = con.cursor()
    select = models.select_senha_conv(key)

    cursor.execute(select)
    row = cursor.fetchone()
    if (row == None):
        return None
    while row:
        DIC = {
            'CD_CONV': row[0],
            'CREATE_CLI': row[1]
        }
        row = cursor.fetchone()

    con.commit()
    con.close()

    return DIC


def exec_insert_conv_cli_postgres(id_cli, cd_conv, cd_cli, cgc, telefone, primeiro_nome, nome, envio_sms, envio_email,
                                  aceite_lgpd, data_aceite_lgpd, email, ip):
    con = connect.connect_pg()
    cursor = con.cursor()
    select = models.insert_conv_cli_postgres(verificaNull(id_cli), verificaNull(cd_conv), verificaNull(cd_cli),
                                             verificaNull(cgc), verificaNull(telefone), verificaNull(primeiro_nome),
                                             verificaNull(nome), verificaNull(envio_sms), verificaNull(envio_email),
                                             verificaNull(aceite_lgpd), verificaNull(data_aceite_lgpd),
                                             verificaNull(email), verificaNull(ip))

    cursor.execute(select)

    con.commit()
    con.close()


def exec_busca_usuario(key):
    con = connect.connect_pg()
    cursor = con.cursor()
    select = models.select_usuario(key=key)
    cursor.execute(select)
    row = cursor.fetchone()
    if row is None:
        con.commit()
        con.close()
        return None
    else:
        con.commit()
        con.close()
        return {
            "cd_conv": row[0],
            "cd_cli": row[1],
            "cpf": row[2],
            "nome": row[3],
            "telefone": row[4],
            "email": row[5]
        }


def exec_insert_token(usuario, token):
    con = connect.connect_pg()
    cursor = con.cursor()
    insert = models.insert_token(usuario=usuario, token=token)
    cursor.execute(insert)
    con.commit()
    con.close()
