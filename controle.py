import psycopg2

#Dados para login no postgre
hostname = 'localhost'
database = 'bebidas'
username = 'postgres'
pwd = 'postgres'
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
    print(f"Conectado com sucesso ao banco de dados {database} do PostgreSQL!")

    print('O que você deseja fazer?')
    print('Adicionar, remover, consultar, atualizar')
    acao = input('Qual a opção escolhida? ').lower()

    if acao == 'adicionar':
        nome_bebida = input('Qual a bebida você deseja adicionar? ').upper()
        procurar_nome = f'''SELECT * FROM bebidas 
                            WHERE nm_bebidas = '{nome_bebida}' '''
        cursor.execute(procurar_nome)
        conn.commit()
        resultados = cursor.fetchall()
        if resultados:
            ja_existe = input('Esta bebida ja existe, invês disso gostaria de atualizar seu valor? ').lower()
            if ja_existe == 'sim':
                valor = input('Digite a quantidade desejada: ')
                soma = f'''UPDATE bebidas SET qtd_disponivel = qtd_disponivel + {valor}
                            WHERE nm_bebidas = '{nome_bebida}' '''
                cursor.execute(soma)
                conn.commit()
                print('Quantidade atualizada com sucesso')
        else:
            quantidade = input('Qual o valor desejado? ')
            inserir = f'''INSERT INTO BEBIDAS (nm_bebidas,qtd_disponivel)
                            VALUES ('{nome_bebida}', '{quantidade}')'''
            cursor.execute(inserir)
            conn.commit()
            print(f'A Bebida {nome_bebida} foi adicionada com sucesso')

    elif acao == 'remover':
        remover_bebida = input('Qual bebida você deseja remover? ').upper()
        confirmacao_remover = input('Você realmente deseja remover esta bebida? ').lower()
        if confirmacao_remover == 'sim':
            deletar = f'''DELETE FROM bebidas
                        WHERE bebidas.nm_bebidas = '{remover_bebida}' '''
            cursor.execute(deletar)
            conn.commit()
            print(f'A bebida {remover_bebida} foi removida com sucesso!')
        else:
            print('Ação não confirmada')

    elif acao == 'consultar':
        visualizar = '''SELECT * FROM bebidas'''
        cursor.execute(visualizar)
        resultado = cursor.fetchall()
        print('Essas são as bebidas registradas:')
        for linha in resultado:
            print(linha)

    elif acao == 'atualizar':
        nome_bebida = input('De qual bebida você quer atualizar o valor? ').upper()
        procurar_nome = f'''SELECT * FROM bebidas 
                            WHERE nm_bebidas = '{nome_bebida}' '''
        cursor.execute(procurar_nome)
        conn.commit()
        resultados = cursor.fetchall()
        if resultados:
            soma_diminui = input('Você deseja somar ou diminuir a quantidade? ').lower()
            valor = input('Qual a quantidade? ')
            if soma_diminui == 'somar':
                soma = f'''UPDATE bebidas SET qtd_disponivel = qtd_disponivel + {valor}
                            WHERE nm_bebidas = '{nome_bebida}' '''
                cursor.execute(soma)
                conn.commit()
                print('Valor atualizado com sucesso!')
            elif soma_diminui == 'diminuir':
                diminuir = f'''UPDATE bebidas SET qtd_disponivel = qtd_disponivel - {valor}
                                WHERE nm_bebidas = '{nome_bebida}' '''
                print('Valor atualizado com sucesso!')
        else:
            print('Bebida não encontrada')

    else:
        print('Ação inválida')
        
except Exception as error:
    print(error)

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()