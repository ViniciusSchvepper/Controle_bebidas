Tem como objetivo automatizar o processo de consulta, adição e remoção de produtos e alteração de quantidade disponível.

Linkedin: linkedin.com/in/vinicius-schvepper-39711b247/

A única lib importada, psycopg2, é impostíssima para que possamos executas scripts em SQL dentro do interpretador, que no meu caso foi o VSCODE. 
Primeiro dou os dados de login do banco de dados PostgreSQL, para que possamos posteriormente executar os scripts como se estivéssemos em uma query.
Após fazer a conexão crio um input que permite que possamos transitar por entre as opções disponíveis: Adicionar, remover, consultar e atualizar.
Adicionar: É a parte que permite fazer a adição de novos produtos, caso o produto que for adicionado já esteja criado, existe a opção de alterar o valor já criado. Optei por usar apenas soma uma vez que, caso esteja se registrado um produto novo, entende-se que ele terá um valor positivo.
Remover: Onde caso queiramos tirar produtos de estoque ou que não são relevantes por qualquer motivo que seja.
Consultar: Usado unicamente para fazer a consulta dos valores disponíveis na tabela, retornando dentro do terminal os produtos.
Atualizar: Por fim onde podemos fazer a adição ou subtração da quantidade de produtos disponíveis, de modo que seja fácil fazer o balanço.
