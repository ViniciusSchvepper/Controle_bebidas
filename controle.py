import psycopg2

#Dados para login no postgre
hostname = 'localhost'
database = 'bebidas'
username = 'postgres'
pwd = 'pwd'
port_id = 5432
conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cursor = conn.cursor()
    print(f'Conectado com sucesso ao banco de dados {database}')

    acao = input('O que você deseja fazer?\n'
          'Adicoinar, remover, atualizar, consultar ou sair?\n').lower()
    
    def executar():
        cursor.execute(acao)
        conn.commit()
    
    def soma():
        quantidade = input('Quantas unidades deseja adicionar?\n')
        acao = f'''UPDATE bebidas SET qtd_disponivel = qtd_disponivel + {quantidade}
                    WHERE nm_bebidas = '{nome_bebida}' '''
        executar()

    def checagem():
        acao = f'''SELECT * FROM bebidas
                                WHERE nm_bebidas = '{nome_bebida}' '''
        executar()
        resultado = cursor.fetchall()
        return resultado

    while acao != 'sair':
        if acao == 'adicionar':
            nome_bebida = input('Qual bebida deseja adicionar?\n')
            checagem()

            if resultado:
                ja_existe = input('Esta bebida já existe, invês disso gostaria de atualizar seu valor?\n').lower()
                if ja_existe == 'sim':
                    soma()
            else:
                quantidade = input('Qual o valor desejado?')
                inserir = f'''INSERT INTO bebidas (nm_bebidas,qtd_diponivel)
                                VALUES ('{nome_bebida}, '{quantidade}')'''
                executar()

        elif acao == 'remover':
            remover = input('Qual bebida você deseja remover? \n')
            confirmacao = input('Você realmente deseja remover esta bebida? \n')
            if confirmacao == 'sim':
                acao = f'''DELETE FROM bebidas
                            WHERE bebidas.nm_bebidas = '{remover}' '''
                executar()
            else:
                print('Ação não confirmada')

        elif acao == 'atualizar':
            nome_bebida = input('Qual bebida você deseja atualizar o valor?')
            resultado = checagem()
            if resultado:
                soma_subtrai = input('Você deseja adicionar ou retirar?\n').lower()
                if soma_subtrai == 'somar':
                    soma()
                elif soma_subtrai == 'subtrair':
                    valor = input('Qual o valor?')
                    acao = f'''UPDATE bebidas SET qtd_disponivel = qtd_disponivel - {valor}
                                    WHERE nm_bebidas = '{nome_bebida}' '''
            else:
                print('Bebida não encontrada')

        elif acao == 'consultar':
            checagem()
            print('Estas são as bebidas registradas: ')
            for linha in resultado:
                print(linha)
        elif acao == 'sair':
            print('Saindo do sistema!')
            cursor.close()
            conn.close()

except Exception as error:
    print(error)

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
