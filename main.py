print(f'\n'
      f'                 Este é um programa usado para conversão de números bínarios em \n'
      f'                 equivalentes decimais, com no maximo 8 dígitos binários \n')

binario = input('Número em notação binária: \n')

binario = [b for b in binario if (b == '1') or (b == '0')]

if binario == []:
    print('Número binário informado inválido')

    exit()
if len(binario) > 8:
    print('O número passado tem mais de 8 dígitos')

    exit()

bases = [128, 64, 32, 16, 8, 4, 2, 1]

dec = 0

for i, b in enumerate(binario):
    b = int(b)
    if b == 1:
        dec += bases[i]

print(f'O número equivalente em base 10 é: {dec}')
