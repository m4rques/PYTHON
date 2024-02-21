#def big_mac (): 
#    print("Big Mac")

#print("Preparando")
#big_mac()
#print("Big Mac está pronto")

#def fazer_big_mac (nome):
   # print(f"Big Mac de {nome}")

#fazer_big_mac("Kauan")
#fazer_big_mac("Jose")
#fazer_big_mac("Paloma")
    
#def fazer_batata (tamanho):
    #print(f"Batata tamanho {tamanho}")

#def preparar_refrigerante (tipo,tamanho):
    #print(f"{tipo} {tamanho}")

#fazer_big_mac("Kauan")
#fazer_batata("Media")
#preparar_refrigerante("Coca", "Grande")

#def combo (nome, tamanho_batata, tipo_refri, tamanho_refri):
    #fazer_big_mac(nome)
    #fazer_batata(tamanho_batata)
    #preparar_refrigerante(tipo_refri, tamanho_refri)

#combo("Kauan", "Grande", "Coca", "Media")


def soma (num1, num2):
    return num1 + num2

#resultado = soma(15,10)
#print(resultado)

def maior_num (list_num):
    list_num.sort()
    list_num.reverse()
    maior_num = list_num[0]
    return maior_num
resultado = maior_num([4341,34134,3414,144,34134,34134,3414,4,14,134,14,144,1,51,5,1])
print(resultado)

    
