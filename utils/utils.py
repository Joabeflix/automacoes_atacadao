

def log(obj):
    if isinstance(obj, list):
        for t in obj:
            print(f'>>> {t}\n')
        return None
    print(f'>>> {obj}\n')

lista = ['joabe', 'alves', 23475]
