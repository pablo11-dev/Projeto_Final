//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#### Relatório


O código representa um sistema de comércio implementado em Python. Ao iniciar o software, a página inicial mostra um menu que possibilita o login como administrador ou como cliente, que levam a menus diferentes. Ao realizar o login, o usuário insere nome e senha. 

No menu voltado aos clientes, as opções são para a compra, ou seja: listar os produtos disponíveis, mostrando sua descrição, seu valor e seu ID; adicionar produto ao carrinho, usando seu ID; listar os produtos do carrinho e finalizar a compra, quando o produto sai do carrinho de compras e vai pra lista de produtos comprados. 

No menu voltado aos administradores, é possível cadastrar um cliente ou administrador novo, assim como listar produtos e clientes, analisar o histórico de compras do cliente e o histórico de vendas da loja.
Os métodos do código:
Login do cliente (Realiza o primeiro processo, pedindo usuário e senha, para que o cliente use o software. Caso a senha ou o usuário estejam errados, o software reinicia.)
Cadastrar cliente (Realiza o cadastro de um novo cliente.)
Listar clientes (Lista todos os cliente cadastrados.)
Listar compras do cliente (Lista as compras de cada cliente.)
Listar vendas da loja (Lista as compras de todos os clientes.)
Adicionar produto ao carrinho (Adiciona um produto ao carrinho do cliente.)
Cadastrar produto (Realiza o cadastro de um novo produto.)
Listar produtos do carrinho  (Lista os produtos do carrinho do cliente.)
Excluir produtos do carrinho (Exclui um ou mais produtos do carrinho do cliente.)
Listrar produtos (Lista os produtos disponíveis na loja.)
Cadastrar administradores (Realiza o cadastro de um novo administrador.)
Login do administrador (Realiza o primeiro processo, pedindo usuário e senha, para que o administrador use o software. Caso a senha ou o usuário estejam errados, o software reinicia.)
Listar administradores (Lista todos os administradores cadastrados.)
Diminuir quantidade de produtos (Reduz a quantidade de um produto no estoque.)
Listar loja (Lista os dados da loja: CNPJ, endereço e nome.)
Alterar loja (Altera os dados da loja: CNPJ, endereço e nome.)
O código é dividido em três classes, sendo elas:
Clientes (A classe tem a função de representar aquilo que é realizado pela loja sem relação aos produtos, ou seja, é a classe se refere as ações que envolvem os clientes. São elas: login do cliente, cadastrar cliente, listar clientes, listar compras do cliente e listar vendas da loja.)
Produtos (A classe tem a função de representar aquilo que é realizado pela loja com relação aos produtos, ou seja, é a classe se refere as ações que os envolvem. São elas: adicionar produto ao carrinho, cadastrar produto, listar produtos do carrinho, excluir produtos do carrinho, diminuir quantidade de produtos e listar produtos.)
Administrador (A classe tem a função de representar aquilo que é realizado pela loja com relação exclusivamente aos administradores. São elas: cadastrar administradores, login do administrador e listar administradores.)
E-Commerce (A classe tem a função de representar aquilo que é realizado pela loja sem relação aos clientes, administradores ou produtos. São elas: listar informações da loja e alterar nome, endereço ou cnpj da loja.)

