#lendo arquivo de coleta

from Post_Produtos import pegaCodigo, pegaCodColetor, pegaDadosColeta, inserirRegistro
import os

coleta = {'vercod': '666999666', 'data': '2017-24-12', 'cod_supermercado': '0', 'cod_coleta': '0', 'cod_usuario': '0'}

def inicio_do_sistema():


    coletor = input('Digite parte do nome do coletor -> ')# pego o nome digitado
    os.system('clear')#limpa tela
    print('Verificando usuário, aguarde...')
    print()
    pegaCodColetor(coletor)# mostra uma lista de nomes encontrardos
    print()
    codigo_escolhido = input('Digite o codigo do coletor -> ')# escolhe um codigo mostrados na lsta anterior
    coleta['cod_usuario'] = codigo_escolhido# salva no Dicionário coleta o codigo do usuario
    print('O código escolhido foi : ', coleta['cod_usuario'])
    os.system('clear')#limpa tela
    print('Encontrando a coleta, aguarde...')
    retorno_coleta = pegaDadosColeta(codigo_escolhido)# verifica no WS a coleta referente ao codigo do usuario e retorna os dados
    if retorno_coleta[0] != '-1':# salva os dados da coleta no Dicionáro caso existam
        coleta['cod_coleta'] = retorno_coleta[0]
        coleta['cod_supermercado'] = retorno_coleta[1]
        coleta['cod_usuario'] = codigo_escolhido
        print('Coleta encontrada no sistema.')
        print()


    else:
        print('Este usuario não possui uma mensagem no sistema, verifique no banco de dados!\nE tente novamente.')
        return False


    data = input('Digite da data da coleta - ex: 2017-24-12 -> ')# digita a data que a coleta foi feita
    coleta['data'] = data # salva a data no Dicionário
    print('A data digitada foi  : ', coleta['data'])
    print('Dados da coleta:', str(coleta))
    print()

    return True

if not inicio_do_sistema():
    inicio_do_sistema()
else:
    arquivo = input('Digite o nome do arquivo -> (ex: coleta.csv ): => ')
    os.system('clear')
    print()
    print('Verificando dados aguarde...')

    #definição das variaveis
    dados = [] # uma lista dos dados vindos do arquivo lido

    produto = [] # lista de produtos encontrados
    cod_produto = [] # codigo dos produtos encontrados
    marca = [] # marca dos produtos encontrados
    valor = [] # valor dos produtos encontrados

    produto_pendente = []
    cod_produto_pendente = []
    marca_pendente = []
    valor_pendente = []



    with open(arquivo, 'r', encoding= 'latin-1') as arq:# abre o arquivo para leitura
        lista = arq.read().splitlines()# Cria uma lista, cada linha do arq é um item da lista

    for linha in lista:# lendo os itens da lista
        dados = linha.split(';')# Separando os dados pelo marcador ';'
        print(dados)
        if dados[1] != '' and dados[4] != '':# se o nome do produto e preço forem diferentes de vazio
            _produto = dados[1].upper()# salvando nome do produto todo em letra maiuscula
            _marca = dados[2].upper()# salvando marca do produto todo em letra masiuscula
            _valor = dados[4] # salvando o preço do produto
            _codigo = pegaCodigo(_produto, _marca)# chama a função para pegar o codigo do produto comparando nome e marca

            if str(_codigo).upper() != 'NONE':# produtos encontrados
                print('OK')
                print()
                produto.append(_produto)
                marca.append(_marca)
                valor.append(_valor)
                cod_produto.append(_codigo)
            else:# produtos não encontrados
                print('Pendente')
                print()
                produto_pendente.append(_produto)
                cod_produto_pendente.append(_codigo)
                marca_pendente.append(_marca)
                valor_pendente.append(_valor)
        else:# linhas com dados nulos
            print('Nulo')
            print()

    def lista_produtos():#Lista todos os produtos encontados no WS
        os.system('clear')
        print('Total de produtos encontrados : %d ' % len(produto))
        print()

        for x in range(0, len(produto)):

            print('Codigo : %s\nProduto : %s\nMarca : %s\nValor : %s' % (cod_produto[x], produto[x], marca[x], valor[x]))
            print()


    def salva_lista_produtos():#Salvando os produtos da lista

        print('Total de produtos encontrados : %d ' % len(produto))
        print()

        qtde = len(produto)


        for x in range(0, qtde):

            print('Codigo : %s\nProduto : %s\nMarca : %s\nValor : %s' % (cod_produto[x], produto[x], marca[x], valor[x]))


            inserir = input('Gravar registro (s) sim ou (n) não ?\n -->>  ')

            if inserir == 's':
                resp = inserirRegistro(cod_produto[x],
                                coleta['vercod'],
                                coleta['data'],
                                valor[x],
                                coleta['cod_supermercado'],
                                coleta['cod_coleta'],
                                coleta['cod_usuario'])


                # print(resp)

                if resp == True:
                    print('Salvo com sucesso')
                    print('\n\n')
                    # cod_produto.pop(x)
                    # produto.pop(x)
                    # valor.pop(x)
                    # marca.pop(x)

                elif resp == 'existe':
                    print('Registro existente')
                    print('\n\n')
                    # cod_produto.pop(x)
                    # produto.pop(x)
                    # valor.pop(x)
                    # marca.pop(x)

                elif resp == False:
                    print('Problemas na inserção')
                    print('\n\n')
                    #enviando para lista de pendencias
                    # cod_produto_pendente.append(cod_produto[x])
                    # produto_pendente.append(produto[x])
                    # valor_pendente.append(valor[x])
                    # marca_pendente.append(marca[x])
                    #
                    # cod_produto.pop(x)
                    # produto.pop(x)
                    # valor.pop(x)
                    # marca.pop(x)


    def lista_produtos_pendente():#Lista todos os produtos que não foram encontados no WS
        os.system('clear')
        print()
        print('Total de produtos não encontrados  : %d ' % len(produto_pendente))

        for x in range(0, len(produto_pendente)):

            print('Codigo : %s\nProduto : %s\nMarca : %s\nValor : %s' % (
            cod_produto_pendente[x], produto_pendente[x], marca_pendente[x], valor_pendente[x]))
            print()


    while True:#Menu da aplicação
        print()
        print("Faça a escolha : ")
        resp = input("(1) - Mostrar produtos encontrados\n"
                     "(2) - Mostrar produtos não encontrados\n"
                     "(3) - Criar novos produtos\n"
                     "(4) - Salvar no Sistema\n\n"
                     "Digite a escolha => ")
        if resp == '1':
            lista_produtos()
        elif resp == '2':
            lista_produtos_pendente()
        elif resp == '4':
            salva_lista_produtos()
        else:
            break

