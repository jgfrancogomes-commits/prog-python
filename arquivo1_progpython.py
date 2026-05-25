
# Receba 3 numeros
# Imprima o maior deles

num1 = float (input('escolha um numero:\n'))
num2 = float (input('escolha um numero:\n'))
num3 = float (input('escolha um numero:\n'))
maior = num3 # null -> Vazio -> Python = None
if num1 > num2 and num1 > num3: 
    maior = num1 
elif num2 > num1 and num2 > num3:
    maior = num2
else : 
    maior = num3 

    print (f'O maior número é: {maior}')





# EXERCICIO EM SALA 

# 3 watts necessários por metro quadrado e a cada 3 metros quadrados há um bocal para lâmpada 
                                                                                                                                                                
Potencia = float (input ('quantos watts em cada lampada'))
largura = float (input ('qual a largura do comodo'))
comprimento = float (input ('qual o comprimento do quarto'))
lampadas = float (input('quantas lampadas serão necessárias'))
watts = Potencia
area = largura * comprimento 
bocais = area/3
potencia_necessaria = area * 3
lampadas = (potencia_necessaria/potencia_lampada)
print(f'potencia necessaria: {potencia_necessaria}')
print(f'bocais: {bocais}')
print(f'lampadas: {lampadas}')

if lampadas > bocais:
    print('precisamos de lampadas mais fortes')
else: 
    print('tudo iluminado')





# resolução 

potencia_lampada = 5
largura = 3 
comprimento = 5

#area -> descobrir metragem 
area = largura * comprimento
# descobrir quantos watts eu preciso 
potencia_necessaria = area * 3
# descobrir o número de bocais 
#calcular a qtd de lampadas 


# exercicio 2 

import math

# Entrada de dados
comprimento = float(input("Digite o comprimento (m): "))
largura = float(input("Digite a largura (m): "))
altura = float(input("Digite a altura (m): "))

# Cálculo da área total das paredes
area_paredes = 2 * altura * (comprimento + largura)

# Cada caixa de azulejo cobre 1,5 m²
area_por_caixa = 1.5

# Cálculo do número de caixas (arredondado para cima)
caixas = math.ceil(area_paredes / area_por_caixa)

# Saída
print(f"Área total das paredes: {area_paredes:.2f} m²")
print(f"Quantidade de caixas necessárias: {caixas}")

 



