# Este modulo tem a funçao e buscar os dados no WS(web service na internet) com retorno Json

import requests

def pegaCodigo(p, m):#Retorna do WS o codigo, nome e marca do produto verifica nome e marca e retorna o codigo do produto


    r = requests.post('http://ifspcoletor.mundotela.net/app/json_busca_produto.php')
    resposta = r.json()

    p = p[0:10]
    m = m[0:5]

    for produto in resposta:
        _uperProduto = str(produto['produto']).upper()
        _uperMarca = str(produto['marca']).upper()

        if p in _uperProduto and m in _uperMarca:
            return str(produto['codigo'])
        elif p in _uperProduto and m == '0':
            return str(produto['codigo'])


def pegaCodColetor(nome):#retrona os usuarios cadastrados com a pesquisa por nome

    r = requests.get("http://ifspcoletor.mundotela.net/app/json_busca_cod_do_coletor.php?nome="+nome)
    resposta = r.json()

    for usuario in resposta:

        _nome = usuario['nome']
        _codigo = usuario['codigo']
        print('Cod : %s -- Nome: %s' % (_codigo, _nome))


def pegaDadosColeta(userCod):# busca a coleta referente ao usuario pesquisado, retornando os dados da coleta

    r = requests.get("http://ifspcoletor.mundotela.net/app/json_busca_dados_coleta.php?codUser=" + userCod)
    resposta = r.json()

    for coleta in resposta:
        _nomeSuper = coleta['nomeSuper']
        _nomeColeta = coleta['nomeColeta']
        _nomeCidade = coleta['nomeCidade']
        _codSuper = coleta['codSuper']
        _codColeta = coleta['codColeta']
        if _codColeta != '-1':
            print()
            print('Supermercado : %s' % _nomeSuper)
            print('Referencia da coleta : %s' % _nomeColeta)
            print('Cidade : %s' % _nomeCidade)
            print()
            return [_codColeta, _codSuper, _nomeCidade]

        return ['-1', '-1', '-1']


def inserirRegistro(codProduto, verCod, data, valor, codSmercado, codColeta, codUser):
    _valor = valor.replace(',', '.')
    _resp = ''
    r = requests.get("http://ifspcoletor.mundotela.net/app/cad_coleta_p.php?chave=30be91"
                     +"&codProduto="+codProduto
                     +"&verCod="+verCod
                     +"&data="+data
                     +"&valor="+_valor
                     +"&codSmercado="+codSmercado
                     +"&codColeta="+codColeta
                     +"&codUser="+codUser)

    for d in r.json():
        _resp = d['resposta']

    return _resp

