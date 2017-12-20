import bottle
from bottle import route, run, template, BaseTemplate, static_file
import subprocess

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url  # reference to function

def pega_ip():
    resposta = subprocess.getoutput("curl http://icanhazip.com")
    meu_ip = resposta.split()
    return meu_ip[-1]


@route('/')
def home_page():
    titulo = 'Painel de Controle'
    ip_atual = pega_ip()
    return template('html', {'titulo':titulo, 'ip_atual':ip_atual})

@route('/aprender')
def page_aprender():
    titulo = 'Material de apoio'
    ip_atual = pega_ip()
    return template('html_aprender', {'titulo':titulo, 'ip_atual':ip_atual})

@route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')



bottle.debug(True)
run(host='192.168.2.123', port=9091)


