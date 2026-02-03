
print("===================================")
print("   GERADOR DE CÓDIGO SIMPLES")
print("===================================")

# PEDIR NOME
nome = input("Digite seu nome: ")
nome = nome.upper()

# PEDIR DATA DE ANIVERSÁRIO
data = input("Digite sua data de aniversario: ")

# PEDIR COISA FAVORITA
favorito = input("Digite sua coisa favorita: ")
favorito = favorito.upper()

# PEGAR PRIMEIRA LETRA DO NOME
letra_nome = ""

for letra in nome:
    if letra != " ":
        letra_nome = letra
        break

# PEGAR PRIMEIRA LETRA DA COISA FAVORITA
letra_favorita = ""

for letra in favorito:
    if letra != " ":
        letra_favorita = letra
        break

# JUNTAR TUDO
codigo = letra_nome + data + letra_favorita

# MOSTRAR RESULTADO
print("-----------------------------------")
print("Codigo gerado:", codigo)
