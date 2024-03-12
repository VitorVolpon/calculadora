print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("escolha uma operação (1/2/3/4): ")

num1 = int(input("Digite o número que deseja utilizar: "))
num2 = int(input("Digite o segundo número que irá utilizar: "))

if escolha == '1':
  soma = num1 + num2
  print(f"Resultado da soma: {soma}")
elif escolha == '2':
  subtracao = num1 - num2
  print(f"Resultado da subtração: {subtracao}")
elif escolha == '3':
  multiplicacao = num1 * num2
  print(f"Resultado da multiplicação: {multiplicacao}")
elif escolha == '4':
  divisao = num1 / num2
  print(f"Resultado da divisão: {divisao}")