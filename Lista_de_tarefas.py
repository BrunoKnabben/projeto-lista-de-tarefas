def printa_titulo(texto='Insira o título', num_lin=7):
    print('=' * num_lin, texto, '=' * num_lin)


contador = 1
tarefas = {}
opcao = 0
temp = {}

while opcao != 5:
    print('Selecione uma opção:\n')
    print('[1] Adicionar tarefa')
    print('[2] Listar tarefas')
    print('[3] Undo')
    print('[4] Redo')
    print('[5] Encerrar')
    try:
        opcao = int(input())
    except ValueError:
        print('Opção inválida')
    print()

    if opcao == 1:
        print(f'Tarefa {contador}: ', end='')
        nova_tarefa = input()
        tarefas[f'Tarefa {contador}'] = nova_tarefa
        contador += 1

    if opcao == 2:
        if contador != 1:
            printa_titulo('Lista de Tarefas')
            for num_tarefa, descricao in tarefas.items():
                print(f'{num_tarefa}: {descricao}')
        else:
            print('Ainda não há nenhuma tarefa.')
        print()

    if opcao == 3:
        if contador == 1:
            print('Não há nada para desfazer.\n')
        else:
            temp[f'Tarefa {contador - 1}'] = tarefas[f'Tarefa {contador - 1}']
            del tarefas[f'Tarefa {contador - 1}']
            contador -= 1

    if opcao == 4:
        try:
            tarefas[f'Tarefa {contador}'] = temp[f'Tarefa {contador}']
            contador += 1
        except KeyError:
            print('Não há nada para refazer.')
