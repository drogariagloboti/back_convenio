def alteraStatusConv(status, cd_cliente, cd_conv):
    update = f""" update RC_CLI_CONV_RC_CLI
                        set
                        STS_CRED = {status},
                        STS_ATIVO = {status}
                        WHERE CD_EMP = 1
                        AND CD_CLI = {cd_cliente}
                        AND CD_CONV = {cd_conv};

                  update RC_CLI
                        set 
                        STS_CLI = {status},
                        STS_CRED = {status}
                        where CD_CLI = {cd_cliente}; """

    return update


def retornaUsuarioPostgres(id):
    select = f""" select 
                        primeiro_nome,
                        cd_conv,
                        cd_cli
                        from conv_cli
                        where id_cli = '{id}' """

    return select


def retornaUsuarioSQLServer(cd_conv, cpf):  # Consulta no 10.10.0.5 - Possivel segunda API.

    select = f""" select 
                        cli.CD_CLI
                        from RC_CLI_CONV_RC_CLI conv
                        inner join RC_CLI cli on conv.CD_EMP = cli.CD_EMP
                              and conv.CD_CLI = cli.CD_CLI
                        where conv.CD_EMP = 1 
                        and conv.CD_CONV = {cd_conv}
                        and cli.CGC_CPF = '{cpf}' """

    return select


def retornaUsuario_retaguarda(cpf):
    select = f""" select 
                        RC_CLI.CD_CLI,
                        RC_CLI.RZ_CLI,
                        REPLACE(REPLACE(RC_CLI.CGC_CPF, '.', ''), '-', '') as CPF,
                        RC_CLI.DDD_TEL,
                        RC_CLI.TEL
                        from RC_CLI
                        inner join RC_CLI_CONV_RC_CLI on RC_CLI_CONV_RC_CLI.CD_EMP = RC_CLI.CD_EMP
                              and RC_CLI_CONV_RC_CLI.CD_CLI = RC_CLI.CD_CLI
                        where RC_CLI.CD_EMP = 1
                        and RC_CLI.CGC_CPF = '{cpf}'
                        and RC_CLI_CONV_RC_CLI.CD_CONV = 399 """

    return select


def insert_tabela_token(row0, row1, row2, row3, row4):
    insert = f""" INSERT INTO public.conv_token(
	cd_cli, cd_conv, token, hora_cria_token, sts_token)
	VALUES ({row0}, {row1}, '{row2}', '{row3}', {row4}); """

    return insert


def select_tabela_token(cd_cli, cd_conv):
    select = f""" select token, hora_cria_token from conv_token where cd_cli = {cd_cli} and cd_conv = {cd_conv} and sts_token = 0 """

    return select


def update_ativa_cliente(cd_cli, cd_conv):
    update = f""" update RC_CLI_CONV_RC_CLI
                        set
                        STS_CRED = 0,
                        STS_ATIVO = 0
                        WHERE CD_EMP = 1
                        AND CD_CLI = {cd_cli}
                        AND CD_CONV = {cd_conv};

                  update RC_CLI
                        set 
                        STS_CLI = 0,
                        STS_CRED = 0
                        where CD_EMP = 1
                        and CD_CLI = {cd_cli}; """

    return update


def select_tabela_token_pelo_token(token):
    select = f""" select token, cd_cli, cd_conv from conv_token where sts_token = 0 and token = '{token}' """

    return select


def select_usuario_lideranca(cd_usu):
    select = f""" select top 1
                        GLB_USU_GRP.CD_USU,
                        GLB_USU.NM_USU,
                        GLB_USU_FILIAL.CD_FILIAL
                        from GLB_USU_GRP
                        inner join GLB_GRP_USU on GLB_USU_GRP.CD_GRP = GLB_GRP_USU.CD_GRP
                        inner join GLB_USU on GLB_USU_GRP.CD_USU = GLB_USU.CD_USU
                        inner join GLB_USU_FILIAL on GLB_USU_GRP.CD_USU = GLB_USU_FILIAL.CD_USU
                        where GLB_USU_GRP.CD_USU = {cd_usu}
                        and GLB_GRP_USU.CD_GRP in (1,3,7,9,64)
                        -- 1    -  TI
                        -- 3	-  GERENCIA REGIONAL
                        -- 7	-  GERENTE DE LOJA
                        -- 9	-  DIRETORIA
                        -- 64   -  SUPERVISOR DE LOJA """

    return select


def select_senha_conv(key):
    select = f""" select cd_conv, create_cli from conv_key_conv where key = '{key}' """

    return select


def insert_conv_cli_postgres(id_cli, cd_conv, cd_cli, cgc, telefone, primeiro_nome, nome, envio_sms, envio_email,
                             aceite_lgpd, data_aceite_lgpd, email, ip):
    insert = f""" INSERT INTO public.conv_cli(
	id_cli, cd_conv, cd_cli, cgc, telefone, primeiro_nome, nome, envio_sms, envio_email, aceite_lgpd, data_aceite_lgpd, email, cadastro_via_email, senha, data_cadastro, cadastro_completo, ip)
	VALUES ({id_cli}, {cd_conv}, {cd_cli}, {cgc}, {telefone}, {primeiro_nome}, {nome}, {envio_sms}, {envio_email}, {aceite_lgpd}, {data_aceite_lgpd}, {email}, null, null, current_date, 1, {ip}); """

    return insert


def select_usuario(key):
    select = f"""
      select
      cd_conv,
      cd_cli,
      cgc as cpf,
      nome,
      telefone,
      email
      from 
      conv_cli
      where
      id_cli = '{key}'
      """
    return select


def insert_token(usuario, token):
    insert = f"""INSERT
      INTO
      public.conv_token_cli(
            cd_conv, cd_cli, cpf, nome, telefone, email, token, data_hora)
      VALUES({usuario['cd_conv']}, '{usuario['cd_cli']}', '{usuario['cpf']}', '{usuario['nome']}', '{usuario['telefone']}', '{usuario['email']}', '{token}', NOW());"""
    return insert
