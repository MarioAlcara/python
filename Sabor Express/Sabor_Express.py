import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]
'''
def exibir_nome_do_programa():
    """
    Exibe o nome do programa na tela.

    Não recebe parâmetros e não retorna valor.
    """
    print("=== Sistema de Gerenciamento de Restaurantes ===")'''
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
'''
def exibir_opcoes():
   Exibe as opções disponíveis do menu na tela.
   Não recebe parâmetros e não retorna valor.
   print("Opções disponíveis:")
   print("1. Cadastrar novo restaurante")
   print("2. Listar restaurantes")
   print("3. Alternar estado de um restaurante")
   print("4. Finalizar o programa")
'''
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

'''

def finalizar_app():
    """
    Finaliza a execução do programa.

    Não recebe parâmetros e não retorna valor.
    """
    print("Encerrando o programa...")


'''
def finalizar_app():
    exibir_subtitulo('Finalizar app')

'''

def finalizar_app():
    """
    Finaliza a execução do programa.

    Não recebe parâmetros e não retorna valor.
    """
    print("Encerrando o programa...")
'''
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

'''

comando responsavel por voltar ao menu principal

'''
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

    '''
    def opcao_invalida():
    """
    Informa ao usuário que a opção escolhida é inválida.

    Não recebe parâmetros e não retorna valor.
    """
    print("Opção inválida! Por favor, escolha uma opção válida.")

    '''

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

'''
def exibir_subtitulo(texto):
    
    Exibe um texto como subtítulo na tela.

    Parâmetros:
    texto (str): Texto a ser exibido como subtítulo.

    Não retorna valor.
    
    print(f"--- {texto} ---")
'''

def cadastrar_novo_restaurante():

    '''Essa função é responsavel por cadastrar um novo restaurante
    
    inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()




def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

        

    voltar_ao_menu_principal()

    '''
def listar_restaurantes():
    """
    Simula a função de listar os restaurantes cadastrados.

    Não recebe parâmetros e não retorna valor.
    """
    # Implementação simulada de listagem de restaurantes
    print("Listagem de restaurantes.")
'''

def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

''' def alternar_estado_restaurante():
    """
    Simula a função de alternar o estado de um restaurante.

    Não recebe parâmetros e não retorna valor.
    """
    # Implementação simulada de alternar estado de restaurante
    print("Alternando estado de restaurante.")
'''


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

'''def escolher_opcao():
    """
    Simula a função de escolha de opção do usuário.

    Não recebe parâmetros.
    Retorna:
    int: Opção escolhida pelo usuário.
    """
    opcao = int(input("Escolha uma opção: "))
    return opcao'''        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


'''def main():
    """
    Função principal que coordena a execução do programa.

    Não recebe parâmetros e não retorna valor.
    """
    exibir_nome_do_programa()
    while True:
        exibir_opcoes()
        opcao = escolher_opcao()

        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
            break
        else:
            opcao_invalida()'''



























