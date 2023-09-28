# Documentação do Software E-commerce

Este documento fornece uma visão geral do software E-commerce, que é um sistema de comércio eletrônico simples com funcionalidades para administradores e clientes. O software é implementado em Python e usa classes para organizar as funcionalidades.

## Funcionalidades

### Classe Cliente

#### `__init__(self)`

#### `login_cliente(self, id, senha)`

#### `cadastrarCliente(self, id, nome, senha, cpf, tel, carrinho_cli={})`

#### `listarClientes(self)`

#### `listar_compras_clietne(self)`

#### `listar_compras_loja(self)`

#### `exclui_cliente(self, id)`

### Classe Administrador

#### `__init__(self)`

#### `cadastrar_admin(self, id_adm, nome_adm, senha_admin, cpf_adm, tel_adm)`

#### `login_admin(self, id_adm, senha_admin)`

#### `listar_administradores(self)`

#### `excluir_admin(self, id_adm)`

### Classe E_commerce

#### `__init__(self, nome, endereco, cnpj)`

#### `listar_loja(self)`

#### `alterar_nome(self, nome)`

#### `alterar_endereco(self, endereco)`

#### `alterar_cnpj(self, cnpj)`

### Classe Produtos

#### `__init__(self, Id_produto, nome_produto, valor_produto, quantidade)`

#### `excluir_produto(self, Id_produto)`

#### `listarprodutos(self)`

#### `adicionar_carrinho(self, Id_produto, nome_produto, valor_produto, quantidade)`

#### `listarCarrinho(self)`

#### `excluir_produto_carrinho(self, Id_produto)`

#### `diminuir_quantidade(self, Id_produto, quantidade)`

## Uso do Software

O software pode ser usado para gerenciar clientes, administradores, produtos e realizar compras. Existem dois tipos de usuários: administradores e clientes. Os administradores podem gerenciar produtos, clientes e administradores, enquanto os clientes podem listar produtos, adicionar produtos ao carrinho, listar produtos no carrinho, excluir produtos do carrinho e finalizar compras.

## Executando o Software

Para executar o software, siga as etapas abaixo:

1. Certifique-se de ter Python instalado em seu sistema.

2. Baixe o código-fonte do software.

3. Execute o arquivo principal, chamado de `main.py`.

4. Siga as instruções apresentadas no console para interagir com o software.
