from flask import Flask
from flask import request
from flask import jsonify
from flask import abort, request
from flask_cors import CORS
import time
import main

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


trusted_ips = ['10.11.1.50', '144.22.145.204']

@app.before_request
def limit_remote_addr():
    if request.remote_addr not in trusted_ips:
        abort(404)  # Not Found


@app.route('/libera_loja_cpf', methods=['GET'])
def fun_libera_loja_cpf():

    cpf_cli = request.headers.get('valida')
    cli = main.valida_usuario(cpf_cli)

    if(cli != None):

        return jsonify({'user': cli, 'conv': cli['CONV']})

    return {'status': 'error', 'msg': 'cpf informado não é um cpf valido'}


@app.route('/valida', methods=['GET']) #exposta
def fun_valida():

    cpf_cli = request.headers.get('valida')
    cli = main.valida_usuario(cpf_cli) #exposta

    if(cli != None):

        return jsonify({'user': cli, 'conv': cli['CONV']})

    return {'status': 'error', 'msg': 'Agradecemos o seu interesse pelo convênio médico globo, contudo o seu C.P.F ainda não faz parte dos nossos convêniados'}, 406


@app.route('/valida_senha_conv/<key>', methods=['GET']) #exposta
def fun_valida_senha_conv(key):
    return main.valida_senha_conv(key)

@app.route('/valida_id/<key>', methods=['GET']) #protegida
def fun_valida_id(key):
    return main.valida_id_postgres(key)

@app.route('/valida_cpf/<conv>&<cpf>', methods=['GET']) #exposta
def fun_valida_cpf(conv,cpf):
    return main.valida_cpf_sqlserver(conv,cpf)

@app.route('/grava_cli', methods=['POST']) #exposta
def fun_grava_cli():
    req = request.json
    aceite_lgpd = req['aceite_lgpd']
    cpf = req['cpf']
    dt_aceite_lgpd = req['dt_aceite_lgpd']
    email = req['email']
    envio_email = req['envio_email']
    envio_sms = req['envio_sms']
    frist_name = req['frist_name']
    id = req['id']
    name = req['name']
    tel = req['tel']
    conv = req['conv']
    cli = req['cli']
    ip = req['ip']

    res = main.grava_cli_postgres(id,conv,cli,cpf,tel,frist_name,name,envio_sms,envio_email,aceite_lgpd,dt_aceite_lgpd,email,ip)
    if(res['status'] != 'ok'):
        return jsonify({"status": "error"})
    return jsonify({"user": {"id": id, "name": name, "cdCli": cli, "conv": conv}}), 201

@app.route('/ativa', methods=['GET'])
def fun_ativa():

    token = request.headers.get('token')
    res = main.ativa_cliente(token)

    return res

@app.route('/usulideraca', methods=['POST'])
def fun_usulideranca():
    content = request.json
    cd_usu = content['cd_usu']
    senha = content['senha']
    user = main.valida_usu_lideranca(cd_usu,senha)
    teste = user.get('status')
    if(teste == None):
        return jsonify({'user': user['NM_USU'], 'filial': user['CD_FILIAL']})
    else:
        return user


@app.route('/grava-token-validado', methods=['POST'])
def gravar_token():
    try:
        key, token = request.json['key'], request.json['token']
        returner = main.gravar_token(key=key)
        main.insert_token(usuario=returner, token=token)
        return '', 200
    except:
        return '', 400

if(__name__ == '__main__'):
    #from waitress import serve
    #serve(app, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)