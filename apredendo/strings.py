minha_string = "Pele é o maior da historia"
               #01234567891111111111222222
               #          0123456789012345
print(minha_string.upper()) #função upper, deixa a palavra em letras maiusculas
print(minha_string.lower()) #função lower, deixa todo o texto minusculo
print(minha_string.capitalize()) #função capitalize, deixa toda letra inicial do texto em maiusculo
print(minha_string.isupper()) #função isupper, ele avisa se o texto é com letra maiuscula ou não, usando o true ou false
print(minha_string.islower()) #função islower, ele avisa se o texto é com letra minuscula ou não, usando o true ou false
print(minha_string.strip()) #função strip, ela remove os espaoços que tem na frente e a tras do texto
print(minha_string.replace("Pele", "Messi")) #função replace, ela faz a troca de palavras ou de letra do texto
print(len(minha_string)) #Ele mostra quantas caracteres tem na frase
print(minha_string[10]) #ele pega uma letra expecifica do texto
print(minha_string.index("maior")) #função index, mostra o indice de uma letra do texto ou uma parte do texto

x = "Pele" in minha_string #mostra se existe a letra ou palavra existe na variavel
print(x)