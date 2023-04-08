from ouvidoria import *

conexao= abrirBancoDados('localhost', 'root', 'sucesso1803#', 'ouvidoria2')

opcao = 8
while opcao != 5:

    opcao = menu()

    if opcao == 1:
        listaDeReclamacao(conexao)

    if opcao == 2:
        pesquisarPeloCodigo(conexao)

    if opcao == 3:
        inserirNovaReclamacao(conexao)

    if opcao == 4:
        excluirReclamacao(conexao)

    else:
        print('Digite uma opção válida')

encerrarBancoDados(conexao)
