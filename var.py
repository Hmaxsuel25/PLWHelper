def menu():
    print('''
            SETOR:

            [V] - BR040 - Vendas
            [E] - BR040 - Escritório
            [F] - Fábrica
            [T] - Loja Tamoios
            [U] - Loja Tupis
            [S] - Sair
        ''')
    str(input('Escolha uma opção: '))

br040vendas = "v"
br040esc = "e"
brfabrica = "f"
brtamoios = "t"
brtupis = "u"
sair = "s"

menu()
if (sair):
    print ('Programa Finalizado')