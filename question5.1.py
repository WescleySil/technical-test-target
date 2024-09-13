def inverter_string(s):
  # Converte a string em uma lista de caracteres
  lista_caracteres = list(s)
  inicio = 0
  fim = len(lista_caracteres) - 1

  # Inverte a lista de caracteres
  while inicio < fim:
      # Troca os caracteres na posição 'inicio' e 'fim'
      lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
      inicio += 1
      fim -= 1

  # Converte a lista de caracteres de volta para uma string
  return ''.join(lista_caracteres)

def main():
  # Defina a string ou obtenha a entrada do usuário
  string_original = input("Digite a string a ser invertida: ")

  # Inverte a string
  string_invertida = inverter_string(string_original)

  # Exibe a string invertida
  print("String invertida:", string_invertida)

if __name__ == "__main__":
  main()
