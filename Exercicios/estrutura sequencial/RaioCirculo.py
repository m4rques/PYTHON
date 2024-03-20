#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def area_do_circulo(raio):
    return 3.14159 * raio**2
def main():
    raio = float(input('Digite o raio do círculo: '))
    area = area_do_circulo(raio)
    print(f'A área do círculo é {area:.2f}m²')
    
if __name__ == '__main__':
    main()