# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
num1 = float(input("Escolha um número"))
num2 = float(input("Escolha outro número"))
operacao = input("Escolha a operação(+,-,*,/)")
if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} - {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Reultado:{num1} * {num2} = {resultado}")
elif operacao == "/":
    if num2 !=0:
        print("divisão por zero")
        resultado = num1 / num2
        print(f"Resultado:{num1} / {num2} = {resultado}")