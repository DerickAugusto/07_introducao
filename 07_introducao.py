# Exercícío 1
print('\n-=-=-=-=-=-= Ex. 1 -=-=-=-=-=-=-=-')


def amplitude(lst):
    print('Mínimo:', min(lst), 'Máximo:', max(lst))


# Teste da função
lista = [10, 20, 36, 547, 201, 325]
print('A lista utilizada para teste é:', lista)
print('\nAplicando a função:')
amplitude(lista)

# Exercícío 2
print('\n-=-=-=-=-=-= Ex. 2 -=-=-=-=-=-=-=-')


def vertical(nome):
    for n in nome:
        print(n)


# Teste da função
nome_teste = 'Dérick'
print('O nome utilizado para teste é:', nome_teste)
print('\nAplicando a função:')
vertical(nome_teste)


# Exercícío 3
print('\n-=-=-=-=-=-= Ex. 3 -=-=-=-=-=-=-=-')


def faixa_preco(peso):
    if peso < 10:
        print('R$ 50,00')
    elif peso < 20:
        print('R$ 80,00')
    else:
        print('Transporte não aceito')


# Teste da função
peso = 12
print('O peso utilizado para teste é:', peso)
print('\nAplicando a função:')
faixa_preco(peso)
