try:
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
except FileNotFoundError:
    print("Erro: o arquivo palavras.txt não foi encontrado.")
    exit()
    
palavras = []
for line in arquivo:
    palavra = line.strip()
    palavras.append(palavra)

from random import radint
if len(palavras) == 0:
    print(f"Erro. Nao ha palavras no banco de dados.")
    exit(0)
        
palavra = palavras[radint(0, len(palavras)-1]
lenght = len(palavra)
    
letras_tentadas = []
letras_da_palavra = []

for letra in palavra:
    letras_da_palavra.append(letra)
    
tentativas = 7

def print_jogo():
    print("Palavra:", end="")
    for i in range(lenght):
        if palavra[i] in letras_tentadas and palavra[i] in letras_da_palavra:
            print(f" {palavra[i]}", end='')
        else:
            print(" _", end='')

def print_letras_tentadas():
    print("Letras tentadas:", end="")
    if len(letras_tentadas) == 0:
        print(" Nenhuma.", end="")
        return
                
    for letra in letras_tentadas:
        print(f" {letra}", end="")
        
def win():
    for letra in letras_da_palavra:
        if not letra in letras_tentadas:
            return False
    return True
    
print("\nBem vindo ao jogo da forca!\n")

while(tentativas > 0):
    print_jogo()
    print(f"\nTentativas restantes: {tentativas}")
    print_letras_tentadas()

    print("\n\nDigite uma letra maiuscula e sem acento: ")
    l = input()

    if len(l) > 1 or not letra.isaplha():
        print(f"\nTem que ser letra, jogador!\n")
        continue
    letra = l.upper()
    if letra in letras_tentadas:
        print("\nEssa letra ja foi tentada anteriomente, jogador. - to te tando uma colher de cha, nao vou diminuir teus pontos :)\n")
        continue
        
    letras_tentadas.append(letra)

    if letra in letras_da_palavra:
        print(f"\nBoa! A letra '{letra}' está na palavra.\n")
    else:
        print(f"\nUma pena! A letra '{letra}' nao está na palavra.\n")
        tentativas -= 1

    if win():
        print(f"Parabens, voce acertou! A palavra era {palavra}.\n")
        break

if not win():
    print(f"\nFim de jogo, a palvra era {palavra}.\n")
