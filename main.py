altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

imc = (peso / (altura / 100) ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc}, e é classificado como Magreza')
elif 18.5 <= imc < 24.9:
    print(f'Seu imc é de {imc}, e é classificado como Normal')
elif 25 <= imc < 29.9:
    print(f'Seu imc é de {imc} e é classificado como Sobrepeso')
elif 30 <= imc < 39.9:
    print(f'Seu imc é de {imc} e é classificado como Obesidade')
else:
    print("Pode parar de comer e começar a malhar pois o negócio está feio! Obesidade Grave")
