def mostrar_inventario(inventario):
    print("\n--- INVENTÁRIO ---")
    for item in inventario:
        print(f"- {item}")
    print("------------------\n")


print("Seja bem-vindo!!!")
print("A névoa de Venarium")
print("Em uma vila esquecida pelos mapas, cercada por uma floresta densa e coberta por uma névoa eterna, pessoas" \
" começaram a desaparecer sem deixar vestígios, os moradores juram ouvir sussurros vindos das árvores à noite. Ninguém ousa" \
" sair depois do pôr do Sol. Dizem que a vila foi construída sobre as ruínas de um antigo santuário profano... Mas ninguém lembra qual.\n")

nome = input("Digite o nome do Seu personagem: ")

print("\nEscolha a classe do seu personagem: ")
print("1 - Mago")
print("2 - Guerreiro")
print("3 - Ladrão")
print("4 - Bastardo")

classe = input("Digite sua classe: ")

inventario = []
vida = 0
poder = 0

if classe == "Mago":
    print("\nVocê escolheu a classe MAGO. Nível 7, Poder 15, Vida 7")
    inventario = ["Cajado da Maldição", "Poção de cura", "30 moedas"]
    vida = 7
    poder = 15

elif classe == "Guerreiro":
    print("\nVocê escolheu a classe GUERREIRO. Nível 10, Poder 1, Vida 15")
    inventario = ["Espadona", "Poção de Força", "30 moedas"]
    vida = 15
    poder = 1

elif classe == "Ladrão":
    print("\nVocê escolheu a classe LADRÃO. Nível 8, Poder 3, Vida 10")
    inventario = ["Adaga", "Poção de Invisibilidade", "30 moedas"]
    vida = 10
    poder = 3

elif classe == "Bastardo":
    print("\nVocê escolheu a classe BASTARDO. Nível 3, Poder 2, Vida 5")
    inventario = ["Faquinha", "20 moedas"]
    vida = 5
    poder = 2
else:
    print("\nClasse inválida. Você será um Viajante sem glória.")
    inventario = ["Roupa rasgada"]
    vida = 3
    poder = 1

# loop do jogo
while True:
    print("\nO que deseja fazer?")
    print("1 - Ver inventário")
    print("2 - Explorar a floresta")
    print("3 - Lutar contra uma criatura")
    print("4 - Sair do jogo")

    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_inventario(inventario)

    elif opcao == "2":
        print("\nVocê entra na floresta, a névoa fica mais densa...")
        print("De repente, você encontra um baú misterioso!")
        inventario.append("Chave Enferrujada")
        print("Você adicionou 'Chave Enferrujada' ao inventário.")

    elif opcao == "3":
        print("\nUma sombra surge diante de você... um espectro da névoa!")
        if poder > 5:
            print("Você usa sua força e derrota o inimigo facilmente!")
            inventario.append("Alma da Névoa")
        else:
            print("Você não é forte o suficiente... o espectro te fere!")
            vida -= 2
            if vida <= 0:
                print("Sua vida chegou a 0... você morreu na névoa.")
                break
        print(f"Sua vida atual: {vida}")

    elif opcao == "4":
        print("\nVocê decide abandonar a névoa por hoje. Fim de jogo.")
        break

    else:
        print("\nOpção inválida.")