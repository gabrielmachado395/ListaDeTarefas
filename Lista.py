"""
Uma lista de tarefas com as seguintes opções:
    Adicionar tarefa
    Listar tarefas
    Desfazer (a cada vez que é chamada, desfaz a ultima ação)
    Refazer (a cada vez que é chamada, refaz a ultima ação)
"""


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor

    except ValueError:
        try:
            valor = float(valor)
            return valor

        except ValueError:
            pass
# Teste para que o programa não dê erro caso o usuário digite algum caractere errado


lista_tarefas = []

lixeira = []
# Feita para armazenar os itens excluídos caso o usuário queira recuperá-los

while True:
    print('=-' * 22)
    print('[1] Adicionar tarefa\n[2] Listar tarefas\n[3] Desfazer\n[4] Refazer\n[0] Sair')
    escolha = converte_numero(input('O que deseja fazer?: '))
    print('=-' * 22)

    if escolha is None:
        print('Você deve digitar um número. Tente Novamente.')

    if escolha == 1:
        nova_tarefa = lista_tarefas.append(input('Digite aqui sua tarefa: '))

    elif escolha == 2:
        for tarefas in lista_tarefas:
            print('°', tarefas)
            # Organiza as tarefas por tópicos

    elif escolha == 3:
        lixeira.append(lista_tarefas[-1])
        # O item excluído será enviado para a lixeira
        lista_tarefas.pop()
        print('Ultimo item removido com sucesso.')
        print(f'Lista Atual: {lista_tarefas}')

    elif escolha == 4:
        adicionar_novamente = lista_tarefas.append(lixeira)
        print('Item adicionado novamente.')
        print(lista_tarefas)

    elif escolha == 0:
        print('Ok, suas tarefas foram salvas. Tenha um ótimo dia.')
