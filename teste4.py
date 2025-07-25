def solucao_1(lista: list, val: int) -> int:
    p = 0
    while p < len(lista):
        if lista[p] != val:
            p+=1
            continue
        del lista[p]
    return p

def solucao_2(lista: list, val: int) -> int:
    return len([x for x in lista if x != val])


print(solucao_1(lista=[3,2,5,1], val=3))
print(solucao_2(lista=[3,2, 2, 2,5,1], val=2))






[x for x in range(10235893745) if x // 2 != 0]