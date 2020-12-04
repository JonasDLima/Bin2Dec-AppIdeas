print(f'\n'
      f'                 Este é um programa usado para conversão de números bínarios em \n'
      f'                 equivalentes decimais, com no maximo 8 dígitos binários \n')

binario = input('Número em notação binária: \n')

binario = [b for b in binario if (b == '1') or (b == '0')]

if binario == []:
    print('Número binário informado inválido')

    exit()
'''
if len(binario) > 8:
    print('O número passado tem mais de 8 dígitos')

    exit()
'''

bases = [1, 2]

for x in range(len(binario)-2):
    bases.append(bases[x+1] * 2)

bases.sort(reverse=True)

dec = 0
for i, b in enumerate(binario):
    if b == '1':
        dec += bases[i]

print(f'O número equivalente em base 10 é: {dec}')
