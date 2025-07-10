teste = ['alves', 'joabe', 'luz']


with open('teste.txt', 'r') as file:
    for x in file:
        _x = x.strip()
        print(f'Sim - {_x}' if _x in teste else f'Não - {_x}')