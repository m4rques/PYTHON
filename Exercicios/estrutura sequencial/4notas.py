#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f"Soma dos 4 numeros é {soma}")

print(f"A media é {media}")