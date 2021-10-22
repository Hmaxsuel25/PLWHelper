def menu():
    print('''
            SETOR:

            [V] - BR040 - Vendas
            [E] - BR040 - Escritório
            [F] - Fábrica
            [T] - Loja Tamoios
            [U] - Loja Tupis
            [I] - Loja Ipatinga
            [S] - Sair
        ''')
    str(input('Escolha uma opção: '))

br040vendas = "v"
br040esc = "e"
brfabrica = "f"
brtamoios = "t"
brtupis = "u"
bripatinga = "i"
sair = "s"

menu()
if (br040vendas, br040esc, brfabrica, brtamoios, brtupis, bripatinga): 
    print ('descreva o problema:')
    def menu2():
        print('''
            PROBLEMA:

            [P] Periféricos (Teclado, Mouse, Monitor, etc.)
            [T] Suprimentos (Toner, Cilindo de impressão)
            [C] Suporte Técnico (Computador)
            [S] Suporte Técnico (Sistemas Integrados)
            [A] Acessos (Permissão de acessos) 
            [V] Voltar ao menu anterior
        ''')
        str(input('Escolha uma Opção:'))
perif = "p"
suprir = "t"
compt = "c"
suport = "s"
acess = "a"
voltar = "v"

if (sair):
    print ('Programa Finalizado')