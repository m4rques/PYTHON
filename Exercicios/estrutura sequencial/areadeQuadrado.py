#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def area_do_quadrado(lado):
    area = lado * lado
    return area

lado = float(input('Digite o lado do quadrado: '))
area = area_do_quadrado(lado)
print(f"Area do quadrado é {area}")
dobro_da_area = area * 2
print(f"O dobro da area do quadrado é {dobro_da_area}")