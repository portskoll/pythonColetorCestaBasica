from bottle import Bottle, ServerAdapter
import subprocess


def pega_ip():
    resposta = subprocess.getoutput("curl http://icanhazip.com")
    meu_ip = resposta.split()
    return meu_ip[-1]


@Bottle.route('/')
def home_page():
    titulo = 'Painel de Controle'
    ip_atual = pega_ip()
    return Bottle.template('html', {'titulo':titulo, 'ip_atual':ip_atual})

class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # self.server.server_close() <--- alternative but causes bad fd exception
        self.server.shutdown()

app = Bottle()
server = MyWSGIRefServer(host='192.168.2.123', port='9091')
try:
    app.run(server=server)
except Exception as ex:
    print(ex)
