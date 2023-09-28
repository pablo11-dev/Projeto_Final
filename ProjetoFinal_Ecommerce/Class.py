class Cliente:
    def __init__(self):
        self.cliente = {}
        self.cadastrarCliente(1, "Thiago", 123, 123, 123)

    def login_cliente(self, id, senha):
        # Verifica se o id e senha do cliente estão corretos
        if id in self.cliente and self.cliente[id][1] == senha:
            return True
            # Caso esteja correto retorna True
        return False
        # Caso esteja incorreto retorna False


    # Método para cadastrar clientes
    def cadastrarCliente(self, id, nome, senha, cpf, tel, carrinho_cli = {}):
        #! Armazena informações dos clientes no dicionário (Agregação)
        self.cliente[id] = [nome, senha, cpf, tel, carrinho_cli]
        

    # Método para listar clientes
    def listarClientes(self):
        # Lista os clientes cadastrados
        for chave, valor in self.cliente.items():
             print(f'ID: {chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}')
            # Imprime as informações do cliente


    # Método para excluir clientes
    def listar_compras_clietne(self):
        cont = 1        # Contador para listar as compras
        for chave, valor in self.cliente.items():   # Percorre o dicionário
            for chave2, valor2 in valor[4].items(): # Percorre o dicionário
                print(f'ID: {chave} - Nome: {valor[0]} - Compras do cliente | Produto: {valor2[0]} - Valor: {valor2[1]} - Quantidade: {valor2[2]}')
                # Imprime as informações do cliente
            cont += 1   
            # Incrementa o contador
           
    # Método para excluir clientes
    def listar_compras_loja(self):
        contt = 1       # Contador para listar as compras
        for chave, valor in self.cliente.items():
            # Percorre o dicionário
            for chave1, valor1 in valor[4].items(): 
                print(f'Produto: {valor1[0]} - Valor: {valor1[1]} - Quantidade: {valor1[2]}')
                # Imprime as informações do cliente
            
            contt += 1
            # Incrementa o contador
        
    def exclui_cliente(self, id):
        # Exclui o cliente
        del self.cliente[id]

class Administrador:
    def __init__(self):
        self.admin = {}  #? Dicionário para armazenar administradores (Composição)
        self.cadastrar_admin(1, "Carlos", 123, 123, 123)

    def cadastrar_admin(self, id_adm, nome_adm, senha_admin, cpf_adm, tel_adm):
        #? Armazena informações do administrador no dicionário (Composição)
        self.admin[id_adm] = [nome_adm, senha_admin, cpf_adm, tel_adm]

    def login_admin(self, id_adm, senha_admin):
        # Verifica se o id e senha do administrador estão corretos
        if id_adm in self.admin and self.admin[id_adm][1] == senha_admin:
            return True
            # Caso esteja correto retorna True
        return False
        # Caso esteja incorreto retorna False

    def listar_administradores(self):
        # Lista os administradores cadastrados
        print("Lista de administradores:")
        for chave, valor in self.admin.items():         # Percorre o dicionário
            print(f'ID: {chave} - NOME: {valor[0]} - CPF: {valor[1]} - TELEFONE: {valor[2]}')
            # Imprime as informações do administrador
    
    def excluir_admin(self, id_adm):
        # Exclui o administrador
        del self.admin[id_adm]
        

# Definindo a classe E_commerce que representa uma loja.
class E_commerce:
     # Atributos da loja
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome  # Atributo do nome da loja
        self.endereco = endereco # Atributo do endereço da loja
        self.cnpj = cnpj # Atributo do cnpj da loja
    
    def getNome(self):
        return self.nome
    

    def listar_loja(self):
        # Lista as informações da loja
        print(f'Nome da loja: {self.nome} - Endereço: {self.endereco} - CNPJ: {self.cnpj}')

    def alterar_nome(self, nome):
        # Altera o nome da loja
        self.nome = nome

    def alterar_endereco(self, endereco):   
        # Altera o endereço da loja
        self.endereco = endereco

    def alterar_cnpj(self, cnpj):
        # Altera o cnpj da loja
        self.cnpj = cnpj

# Classe Produtos
class Produtos:
    # Atributos do produto
    def __init__(self, Id_produto, nome_produto, valor_produto, quantidade):           
        self.Id_produto = Id_produto            # Atributo de identificação do produto
        self.nome_produto = nome_produto        # Atributo do nome do produto
        self.valor_produto = valor_produto  # Atributo do valor do produto
        self.quantidade = quantidade  # Atributo da quantidade de produtos disponíveis
        self.produtos = {}  # ?Atributo para armazenar produtos (Composição)
        self.carrinho = {}  # ?Atributo para armazenar produtos no carrinho (Composição)
        self.cadastrarProduto(1, "Playstation 5", 5000, 10) # Cadastra os produtos
        self.cadastrarProduto(2, "Xbox Series X", 4500, 10) # Cadastra os produtos
        self.cadastrarProduto(3, "Controle Playstation 5", 500, 10) # Cadastra os produtos
        self.cadastrarProduto(4, "Controle Xbox Series X", 450, 10) # Cadastra os produtos
        self.cadastrarProduto(5, "Guitarra", 1500, 10)  # Cadastra os produtos
        self.cadastrarProduto(6, "Violão", 1000, 10)    # Cadastra os produtos
        self.cadastrarProduto(7, "IPhone 14", 10000, 10)    # Cadastra os produtos
    
    def excluir_produto(self, Id_produto):
        # Exclui o produto
        del self.produtos[Id_produto]

    
    # Método para listar produtos
    def listarprodutos(self):
        # Lista os produtos cadastrados
        for chave, valor in self.produtos.items():
            print(f'ID: {chave} - NOME: {valor[0]} - VALOR: {valor[1]} - QUANTIDADE: {valor[2]}')
            # Imprime as informações do produto


    def getId_produto(self):
        return self.Id_produto

    def getNome_produto(self):
        return self.nome_produto

    def getValor_produto(self):
        return self.valor_produto

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def cadastrarProduto(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto  # Atributo de identificação do produto
        self.nome_produto = nome_produto  # Atributo do nome do produto
        self.valor_produto = valor_produto  # Atributo do valor do produto
        self.quantidade = quantidade  # Atributo da quantidade de produtos disponíveis

        # !Dicionário para armazenar informações dos produtos (Agregação)
        self.produtos[self.Id_produto] = [self.nome_produto, self.valor_produto, self.quantidade]

    def adicionar_carrinho(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.quantidade = quantidade
        self.carrinho[self.Id_produto] = [self.nome_produto, self.valor_produto, self.quantidade]


    def listarCarrinho(self):
        #Listar carrinho, caso seja adicionando em cima do produto, ele vai somar a quantidade
        for chave, valor in self.carrinho.items():
            print(f'ID: {chave} - NOME: {valor[0]} - VALOR: {valor[1]} - QUANTIDADE: {valor[2]}')

            
    # Método para excluir produtos
    def excluir_produto_carrinho(self, Id_produto):
        # Exclui o produto do carrinho
        del self.carrinho[Id_produto]
        

    # Método para diminuir a quantidade de produtos quando o cliente comprar
    def diminuir_quantidade(self, Id_produto, quantidade):
        # Diminui a quantidade de produtos
        self.quantidade = quantidade
        self.produtos[Id_produto][2] -= self.quantidade 
        # Diminui a quantidade de produtos do estoque

    

    
