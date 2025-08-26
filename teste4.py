def cpf_check(cpf: str, digitos=None, digito_atual=1):
    if digitos is None:
        digitos = []
    config_digitos = {1: {'range': [11, -2]}, 2: {'range': [12, -1]}}
    soma = sum([int(x) * y for x, y in zip(cpf[:config_digitos[digito_atual]['range'][1]][::-1], range(2, config_digitos[digito_atual]['range'][0]))])
    digitos.append(0 if soma % 11 < 2 else 11 - (soma % 11))
    return cpf_check(cpf=cpf, digitos=digitos, digito_atual=2) if digito_atual == 1 else cpf[-2:] == f'{digitos[0]}{digitos[1]}'
