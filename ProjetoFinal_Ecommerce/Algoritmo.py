from Class import *  # Importa todas as classes do módulo "Class"

import os

admin = Administrador()  # Cria uma instância da classe "Administrador"
clientee= Cliente()  # Cria uma instância da classe "Cliente"
Loja = E_commerce("Augusto's E_commerce", "Rua 1", "123456789")  #? Cria uma instância da classe "E_commerce" (composição)
produtos = Produtos(30, "Produtos", "R$ 0,00", 30)  #? Cria uma instância da classe "Produtos" (composição)
countID = 1
countID_adm = 1
countID_produto = 7

# A função "menu_inicial" lida com a interação inicial do usuário.

def menu_inicial(): # Menu inicial
    try:        
        print("|______________MENU______________|")
        print(f"      {Loja.getNome()}          ")
        print('|1- logar como administrador     |')
        print('|2- logar como cliente           |')
        print('|3- Sair                         |')
        print("|________________________________|")

        op = int(input(">> "))
        # Verifica a opção escolhida pelo usuário
        try:
            # Verifica a opção escolhida pelo usuário
            match op:
                # Caso a opção seja 1, o usuário será redirecionado para o menu do administrador
                case 1:
                    os.system('cls')
                    id_adm = int(input('Insira o ID do administrador >> '))
                    senha_admin = int(input('Insira a senha >> '))
                    # Verifica se o id e senha do administrador estão corretos
                    if admin.login_admin(id_adm, senha_admin):  #* Usa a instância "admin" para realizar login (associação)
                        print("Login bem-sucedido!")
                        os.system("pause")
                        os.system('cls')
                        mani()
                    
                    # Caso esteja incorreto retorna False
                    else:
                        print("Login falhou. Verifique o ID e a senha.")
                        os.system("pause")
                        os.system('cls')
                        menu_inicial()

                # Caso a opção seja 2, o usuário será redirecionado para o menu do cliente
                case 2:
                    os.system('cls')
                    id = int(input('Insira o ID de cliente >> '))
                    senha = int(input('Insira a senha >> '))
                    # Verifica se o id e senha do cliente estão corretos
                    if clientee.login_cliente(id, senha):  #* Usa a instância "Loja" para realizar login (associação)
                        print("Login bem-sucedido!")
                        os.system("pause")
                        os.system('cls')
                        menu_cli()
                    
                    # Caso esteja incorreto retorna False
                    else:
                        print("Login falhou. Verifique o ID e a senha.")
                        os.system("pause")
                        os.system('cls')
                        menu_inicial()
                
                # Caso a opção seja 3, o programa será encerrado
                case 3:
                    print("Saindo...")
                    exit()

                case _:
                    print("Opção Invalida")
                    menu_inicial()
        
        except ValueError as erro:
            # Tratamento de erro
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            menu_inicial()

    except ValueError as erro:
        # Tratamento de erro
        print("Valor Invalido")
        print(f"erro: {erro.__class__.__name__}")
        menu_inicial()


# A função "menu_cli" lida com as interações do cliente.

def menu_cli():
    try:
        # Menu do cliente
        os.system('cls')
        print("_________________MENU___________________")
        print(f"           {Loja.getNome()}           ")
        print('|1- Listar produtos                    |')
        print('|2- Adicionar produto ao carrinho      |')
        print('|3- Listar carrinho                    |')
        print('|4- Excluir produto do carrinho        |')
        print('|5- Finalizar compra                   |')
        print('|6- Sair                               | ')
        print("|______________________________________|")
        op = int(input(">> "))
        try:
            # Verifica a opção escolhida pelo usuário
            match op:
                # Caso a opção seja 1, o usuário será redirecionado para a lista de produtos
                case 1:
                    os.system('cls')
                    print('Lista de produtos')
                    produtos.listarprodutos()  #* Usa a instância "produtos" para listar produtos (associação)
                    os.system('pause')
                    menu_cli()

                # Caso a opção seja 2, o usuário será redirecionado para o carrinho
                case 2:
                    os.system('cls')
                    try:
                        produtos.listarprodutos()
                        id_produto = int(input('Insira o ID do produto >> '))   # Usuário insere o ID do produto
                        nome_produto = produtos.produtos[id_produto][0]     # A variável "nome_produto" recebe o nome do produto
                        valor_produto = produtos.produtos[id_produto][1]    # A variável "valor_produto" recebe o valor do produto
                        quantidade = int(input('Insira a quantidade >> '))  # Usuário insere a quantidade do produto

                        produtos.adicionar_carrinho(id_produto, nome_produto, valor_produto, quantidade)  #* Usa a instância "produtos" para adicionar ao carrinho (associação)

                        # Verifica se a quantidade do produto é menor ou igual a quantidade disponível
                        if quantidade <= produtos.produtos[id_produto][2]:
                            # Diminui a quantidade do produto
                            produtos.produtos[id_produto][2] -= quantidade
                            print('Produto adicionado ao carrinho com sucesso!')
                        
                        # Caso a quantidade seja maior que a quantidade disponível
                        else:
                            print('Quantidade indisponível')
                        os.system('pause')
                        menu_cli()
                    except KeyError:
                        print('ID inválido')
                        os.system('pause')
                        menu_cli()

                # Caso a opção seja 3, o usuário será redirecionado para a lista de produtos no carrinho
                case 3:
                    os.system('cls')
                    print('Lista de produtos no carrinho')
                    produtos.listarCarrinho()  #* Usa a instância "produtos" para listar o carrinho (associação)
                    os.system('pause')
                    menu_cli()

                # Caso a opção seja 4, o usuário será redirecionado para a lista de produtos no carrinho
                case 4:
                    os.system('cls')
                    print('Lista de produtos no carrinho')
                    try:
                        produtos.listarCarrinho()  #* Usa a instância "produtos" para listar o carrinho (associação)
                        id_produto = int(input('Insira o ID do produto >> '))   # Usuário insere o ID do produto
                        produtos.excluir_produto_carrinho(id_produto)           #* Usa a instância "produtos" para excluir do carrinho (associação)
                        print('Produto excluído do carrinho com sucesso!')
                        os.system('pause')
                        menu_cli()
                    except KeyError:
                        print('ID inválido')
                        os.system('pause')
                        menu_cli()

                # Caso a opção seja 5, o usuário será redirecionado para a lista de produtos no carrinho
                case 5:
                    os.system('cls')
                    print('Finalizar compra')
                    print('Lista de produtos no carrinho')
                    try:
                        produtos.listarCarrinho()
                        print('-----------------------------------')
                        id = int(input('Insira o ID do cliente >> '))   # Usuário insere o ID do cliente
                        clientee.cliente[id][4] = produtos.carrinho  #* Usa a instância "cliente" para armazenar o carrinho (associação)
                        print('Compra finalizada com sucesso!')
                        os.system('pause')
                        produtos.carrinho = {}  # Limpa o carrinho
                        menu_cli()
                    except KeyError:
                        print('ID inválido')
                        os.system('pause')
                        menu_cli()

                # Caso a opção seja 6, o programa será encerrado
                case 6:
                    print("Saindo...")
                    menu_inicial()
                
                case _:
                    print("Opção Invalida")

        except ValueError as erro:
            # Tratamento de erro
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            menu_cli()

    except ValueError as erro:
        # Tratamento de erro
        print("Valor Invalido")
        print(f"erro: {erro.__class__.__name__}")
        menu_cli()


# A função "mani" lida com as interações do administrador.

def mani():
    try:
        # Menu do administrador
        os.system('cls')
        print("_______________MENU_______________")
        print(f"       {Loja.getNome()}        ")
        print("|1- Cadastrar cliente            |")
        print("|2- Cadastrar produto            |")
        print("|3- Excluir produto              |")
        print("|4- Excluir cliente              |")
        print("|5- Listar produtos              |")
        print("|6- Listar clientes              |")
        print("|7- Cadastrar administrador      |")
        print("|8- Excluir administrador        |")
        print("|9- Listar administradores       |")
        print("|10- Histórico de compras/Cliente|")
        print("|11- Histórico de compras/Loja   |")
        print("|12- Alterar funções da loja     |")
        print("|0- Sair                         |")
        print("|________________________________|")
        op = int(input(">> "))
        try:
            # Verifica a opção escolhida pelo usuário
            match op:
                # Caso a opção seja 1, o usuário será redirecionado para o cadastro de clientes
                case 1:
                    os.system('cls')
                    print('Cadastro de clientes')
                    print('Informe os dados do cliente')
                    global countID
                    countID += 1
                    id = countID
                    nome = input("Nome >> ")
                    senha = int(input('Insira a senha >> '))
                    cpf = int(input("CPF >> "))
                    tel = int(input("Telefone >> "))
                    clientee.cadastrarCliente(id, nome, senha, cpf, tel)  #* Usa a instância "Loja" para cadastrar cliente (associação)
                    print('Cliente cadastrado com sucesso')
                    os.system('pause')
                    mani()

                # Caso a opção seja 2, o usuário será redirecionado para o cadastro de produtos
                case 2:
                    os.system('cls')
                    print('Cadastro de produtos')
                    print('Informe os dados do produto')
                    # Cadastra o produto
                    global countID_produto      # Variável global para armazenar o ID do produto
                    countID_produto += 1        # Incrementa o ID do produto
                    id_produto = countID_produto    # A variável "id_produto" recebe o ID do produto
                    nome_produto = input("Nome >> ")    # A variável "nome_produto" recebe o nome do produto
                    valor_produto = float(input("Valor >> "))   # A variável "valor_produto" recebe o valor do produto
                    quantidade = int(input("Quantidade >> "))       # A variável "quantidade" recebe a quantidade do produto

                    produtos.cadastrarProduto(id_produto, nome_produto, valor_produto, quantidade)  #* Usa a instância "produtos" para cadastrar produto (associação)
                    print('Produto cadastrado com sucesso')
                    os.system('pause')
                    mani()

                case 3:
                    os.system('cls')
                    print('Lista de produtos')
                    produtos.listarprodutos()  #* Usa a instância "produtos" para listar produtos (associação)
                    id_produto = int(input('Insira o ID do produto >> '))   # Usuário insere o ID do produto
                    produtos.excluir_produto(id_produto)    #* Usa a instância "produtos" para excluir produto (associação)
                    print('Produto excluído com sucesso!')
                    os.system('pause')
                    mani()

                case 4:
                    os.system('cls')
                    print('Lista de clientes')
                    clientee.listarClientes()  #* Usa a instância "Loja" para listar clientes (associação)
                    id = int(input('Insira o ID do cliente >> '))   # Usuário insere o ID do cliente
                    clientee.exclui_cliente(id) #* Usa a instância "Loja" para excluir cliente (associação)
                    print('Cliente excluído com sucesso!')
                    os.system('pause')
                    mani()

                case 5:
                    os.system('cls')
                    print('Lista de produtos')
                    produtos.listarprodutos()  #* Usa a instância "produtos" para listar produtos (associação)
                    os.system('pause')
                    mani()

                case 6:
                    os.system('cls')
                    print('Lista de clientes')
                    clientee.listarClientes()  #* Usa a instância "Loja" para listar clientes (associação)
                    os.system('pause')
                    mani()

                # Caso a opção seja 7, o usuário será redirecionado para o cadastro de administradores
                case 7:
                    os.system('cls')
                    print('Cadastro de administradores')
                    print('Informe os dados do administrador')
                    global countID_adm
                    countID_adm += 1
                    id_adm = countID_adm
                    nome_adm = input('Insira o nome do administrador >> ')
                    senha_admin = int(input('Insira a senha >> '))
                    cpf_adm = int(input('Insira o cpf do administrador >> '))
                    tel_adm = int(input('Insira o telefone do administrador >> '))

                    admin.cadastrar_admin(id_adm, nome_adm, senha_admin, cpf_adm, tel_adm)  #* Usa a instância "admin" para cadastrar administrador (associação)
                    print('Cadastrador de administrador realizado com sucesso!')
                    os.system('pause')
                    mani()

                case 8:
                    os.system('cls')
                    print('Lista de administradores')
                    admin.listar_administradores()  #* Usa a instância "admin" para listar administradores (associação)
                    id_adm = int(input('Insira o ID do administrador >> '))   # Usuário insere o ID do administrador
                    admin.excluir_admin(id_adm) #* Usa a instância "admin" para excluir administrador (associação)
                    print('Administrador excluído com sucesso!')
                    os.system('pause')
                    mani()

                case 9:
                    os.system('cls')
                    print('Lista de administradores')
                    admin.listar_administradores()  #* Usa a instância "admin" para listar administradores (associação)
                    os.system('pause')
                    mani()

                case 10:
                    os.system('cls')
                    print(f'Histórico de compras dos clientes')
                    clientee.listar_compras_clietne()  #* Usa a instância "Loja" para listar compras dos clientes (associação)
                    os.system('pause')
                    mani()

                case 11:
                    os.system('cls')
                    print(f'Histórico de compras da loja')
                    clientee.listar_compras_loja()  #* Usa a instância "Loja" para listar compras da loja (associação)
                    os.system('pause')
                    mani()


                case 12:
                    os.system('cls')
                    funcoes_loja()  #* Usa a instância "Loja" para alterar funções da loja (associação)
                    print("Abrir funções da loja")
                    os.system('pause')
                    
                case 0:
                    print("Saindo...")
                    menu_inicial()
                
                 
                case _:
                    print("Opção Invalida")
                    mani()
        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            mani()

    except ValueError as erro:
        print("Valor Invalido")
        print(f"erro: {erro.__class__.__name__}")
        mani()

def funcoes_loja():
        os.system('cls')
        print("_________________MENU___________________")
        print(f"       {Loja.getNome()}               ")
        print("|1- Listar informações da loja         |")
        print('|2- Alterar nome da Loja               |')
        print('|3- Alterar endereço                   |')
        print('|4- Alterar o CNPJ                     |')
        print('|5- Sair                               |')
        print("|______________________________________|")
        op = int(input(">> "))
        try:
            match op:
                case 1:
                    os.system('cls')
                    Loja.listar_loja()  #* Usa a instância "Loja" para listar informações da loja (associação)
                    os.system('pause')
                    funcoes_loja()
                case 2:
                    os.system('cls')
                    nome = input("Insira o novo nome da loja >> ")
                    Loja.alterar_nome(nome)  #* Usa a instância "Loja" para alterar nome (associação)
                    print('Nome alterado com sucesso!')
                    os.system('pause')
                    funcoes_loja()
                
                case 3:
                    os.system('cls')
                    endereco = input("Insira o novo endereço da loja >> ")
                    Loja.alterar_endereco(endereco)  #* Usa a instância "Loja" para alterar endereço (associação)
                    print('Endereço alterado com sucesso!')
                    os.system('pause')
                    funcoes_loja()

                case 4:
                    os.system('cls')
                    cnpj = input("Insira o novo CNPJ da loja >> ")
                    Loja.alterar_cnpj(cnpj)  #* Usa a instância "Loja" para alterar CNPJ (associação)
                    print('CNPJ alterado com sucesso!')
                    os.system('pause')
                    funcoes_loja()

                case 5:
                    print("Saindo...")
                    mani()

                case _:
                    print("Opção Invalida")
                    funcoes_loja()
        
        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            funcoes_loja()
