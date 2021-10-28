import os




def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao APP Suporte Palowa')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'{nome}Escolha um Setor{os.linesep}[V] - BR040 - Vendas{os.linesep}[E] - BR040 - Escritório{os.linesep}[F] - Fábrica{os.linesep}[T] - Loja Tamoios{os.linesep}[U] - Loja Tupis{os.linesep}[I] - Loja Ipatinga{os.linesep}[S] - Sair{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

#opções
br040vendas = "v"
br040esc = "e"
brfabrica = "f"
brtamoios = "t"
brtupis = "u"
bripatinga = "i"
sair = "s"

#segunda parte
def processar_resposta(resposta, nome):
    if resposta != 's':
        print(f'{os.linesep}{nome} Qual é o seu problema?')
        while True:
            resposta2 = input(
                f'{os.linesep}[P] Problemas com Periféricos (Teclado, Mouse, etc){os.linesep}[] - BR040 - Escritório{os.linesep}[F] - Fábrica{os.linesep}[T] - Loja Tamoios{os.linesep}[U] - Loja Tupis{os.linesep}[I] - Loja Ipatinga{os.linesep}[S] - Sair{os.linesep}')
    elif resposta == 's':
        print('Programa Finalizado')
        exit()
    else:
        print('Digite apenas as opções citadas')


    
if __name__ == '__main__':
    start()