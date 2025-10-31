import random

def jogar():
    print("\nDESAFIO DO NÚMERO SECRETO")
    numero_secreto = random.randint(1, 100)
    tentativas_max = 8

    for tentativa in range(1, tentativas_max + 1):
        print(f"\nTentativa {tentativa} de {tentativas_max}")
        try:
            palpite = int(input("Qual seu palpite (1 a 100)? "))
        except ValueError:
            print("Digite um número inteiro válido!")
            continue

        if palpite < 1 or palpite > 100:
            print("O número deve estar entre 1 e 100.")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
            return
        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        else:
            print("Muito alto! Tente um número menor.")

    print(f"\nFim das tentativas! O número secreto era {numero_secreto}.")

while True:
    jogar()
    repetir = input("\nDeseja jogar novamente? (sim/não): ").strip().lower()
    if repetir != "sim":
        print("\nObrigado por jogar!")
        break
