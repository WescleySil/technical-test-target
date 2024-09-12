def verifica_letra_a(texto):
    contador_a = texto.count('a') + texto.count('A')

    if contador_a > 0:
        return f"A letra 'a' aparece {contador_a} vezes."
    else:
        return "A letra 'a' não foi encontrada.
        
texto = input("Digite uma string: ")
resultado = verifica_letra_a(texto)
print(resultado)