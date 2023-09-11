'''1. O programa abaixo deve calcular a média dos valores digitados
pelo usuário.
No entanto, ele não está funcionando bem. Você pode
consertá-lo?'''




def calcular_media(valores):
    tamanho = len(valores)  # Corrigir o tamanho
    soma = sum(valores)  # Usar a função sum() para calcular a soma
    media = soma / tamanho
    return media  # Retornar a média calculada

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':  # Corrigir a chamada de lower()
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))