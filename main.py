import exec
import string
import secrets
import getData
import requisicoes
import psycopg2

def altera_status_conv(status,cd_cliente):
    exec.exec_altera_status_conv_loja(status,cd_cliente)
    exec.exec_altera_status_conv_server(status,cd_cliente)

def valida_usuario(cpf):
    cli = exec.exec_retornaUsuario(cpf)
    if(cli == None):
        return None
    return cli

def cria_token(cd_cli,cd_conv):

    valida_token_gerado = exec.exec_select_tabela_token(cd_cli,cd_conv)

    if(valida_token_gerado == None):

        def gera_token():
            alphabet = string.ascii_letters + string.digits
            token = (''.join(secrets.choice(alphabet) for i in range(5))).upper()

            return token

        token = gera_token()
        teste_token = exec.exec_select_tabela_token_pelo_token(token)

        while(teste_token != None):
            token = gera_token()
            teste_token = exec.exec_select_tabela_token_pelo_token(token)

        data_hora = getData.data_hora_agora()

        exec.exec_insert_tabela_token(cd_cli,cd_conv,token,data_hora,0)

        return {'access_token': token, 'dt_hora_token': data_hora}
            
    else:
        return {'access_token': valida_token_gerado['TOKEN'], 'dt_hora_token': str(valida_token_gerado['DT_CRIA_TOKEN'])}


def ativa_cliente(token_cli):
    
    valida_token_gerado = exec.exec_select_tabela_token_pelo_token(token_cli)

    if(valida_token_gerado == None):
        return {'status': 'error', 'msg': 'Não existe token gerado para esse cliente'}
    else:
        result = secrets.compare_digest(valida_token_gerado['TOKEN'],token_cli)
        if(result == True):
            try:
                exec.exec_ativa_cliente_retaguarda(valida_token_gerado['CD_CLI'],valida_token_gerado['CD_CONV'])
                return {'msg': 'cliente ativado'}
            except:
                return {'status': 'error', 'msg': 'não foi possivel ativar o cliente, por favor solicitar ativação no balção'}
        else:
            return {'status': 'error', 'msg': 'token informado não corresponde ao token do cliente'}

def valida_usu_lideranca(cd_usu,senha):

    usu_valido = requisicoes.api_login_itec(cd_usu,senha)

    if(usu_valido == None):
        return {'status': 'error', 'msg': 'Usuario e ou senha incorretos'}
    else:
        usu_lideranca = exec.exec_select_usuario_lideranca(usu_valido['cd_usu'])
        if(usu_lideranca == None):
            return {'status': 'error', 'msg': 'Usuario não tem permissão para liberar cliente, solicite a liberação para o gerente'}
        else:
            return usu_lideranca

def valida_senha_conv(key): #novo
    conv_valida = exec.exec_select_senha_conv(key)
    if(conv_valida == None):
        return {'status': 'error', 'msg': 'A senha informada não é uma senha valida'}
    return {'conv': conv_valida['CD_CONV'],'create': conv_valida['CREATE_CLI']}

def valida_cpf_sqlserver(cd_conv,cpf): #novo
    res = exec.exec_retornaUsuarioSQLSERVER(cd_conv,cpf)
    if(res == None):
        return {'status': 'error', 'msg': 'Usuario não cadastrado.'}
    return {'cd_cli': res['cd_cli']}

def valida_id_postgres(id): #novo
    res = exec.exec_retornaUsuarioPostgres(id)
    if(res == None):
        return {'status': 'error', 'msg': 'Usuario não cadastrado.'}
    return {'primeiro_nome': res['primeiro_nome'], 'cd_conv': res['cd_conv'], 'cd_cli': res['cd_cli']} 

def grava_cli_postgres(id_cli,cd_conv,cd_cli,cgc,telefone,primeiro_nome,nome,envio_sms,envio_email,aceite_lgpd,data_aceite_lgpd,email,ip): #novo
    try:
        exec.exec_insert_conv_cli_postgres(id_cli,cd_conv,cd_cli,cgc,telefone,primeiro_nome,nome,envio_sms,envio_email,aceite_lgpd,data_aceite_lgpd,email,ip)
        return {"status": "ok"}
    except psycopg2.errors.UniqueViolation:
        return {"status": "error"}


def gravar_token(key):
    res = exec.exec_busca_usuario(key=key)
    if res is None:
        return {'status': 'error', 'msg': 'Usuario não cadastrado.'}
    else:
        return res

def insert_token(usuario,token):
    try:
        exec.exec_insert_token(usuario=usuario,token=token)
        return {"status": "ok"}
    except:
        return {"status": "error"}


#print(valida_senha_conv('Globo@2022'))
#print(valida_usu_lideranca(2941,'797226'))
#print(ativa_cliente(634918,399,'SNTFSN'))
#print(cria_token(634918, 399))
#altera_status_conv(1,634918)
#print(valida_usuario('77144411357'))