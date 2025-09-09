number1 = int(input("Digite um numero: "))
number2 = int(input("Digite outro numero: "))

if number1 > number2:
    print(f"O numero {number1} é  maior que o numero {number2}")
elif number1 == number2:
    print(f"O numero {number1} é igual que o numero {number2}")
else:
    print(f"O numero {number2} é maior que o numero {number1}")