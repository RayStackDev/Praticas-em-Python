number1 = int(input("Digite um numero: "))
number2 = int(input("Digite outro numero: "))

if number1 > number2:
    print(f"O numero {number1} é maior que {number2} com uma diferença de {number1-number2}")
elif number2 > number1:
    print(f"O numero {number2} é maior que {number1} com uma diferença de {number2-number1}")
else:
    print("Numeros iguais, sem diferença")
