import time
import subprocess
import os
import requests




def enviaIPServer(ip):#envia o ip para o servidor

    requests.get("http://ip.mundotela.net?ip="+ip)
    # resposta = r.json()
    #
    # for usuario in resposta:
    #
    #     _nome = usuario['nome']
    #     _codigo = usuario['codigo']
    #     print('Cod : %s -- Nome: %s' % (_codigo, _nome))


def pegaIP():
    resposta = subprocess.getoutput("curl http://icanhazip.com")
    meu_ip = resposta.split()
    return meu_ip[-1]




def tempo(t):
    # ip_atual = pegaIP()
    countTimer = 0
    sleepTime = t
    print('IP enviado  => ' + pegaIP())
    enviaIPServer(pegaIP())
    # os.system("reload_meu_ip.sh")
    while True:
        time.sleep(sleepTime)
        countTimer += sleepTime

        # if ip_atual != pegaIP():
        #     print('ip_atual ->' + ip_atual)
        #     print('pegaIp ->' + pegaIP())
        #     enviaIPServer(pegaIP())
        #     os.system("kill -9 $(lsof -t -i:9091)")# da um kill nesta porta
        #     os.system("reload_meu_ip.sh")
        #     ip_atual = pegaIP()
        #     print("O ip foi trocado =>" + ip_atual)
        # else:
        print('Seviço on line por  {} secs'.format(countTimer))
        print('IP Atual  => ' + pegaIP())


tempo(60)

