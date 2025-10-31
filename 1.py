def jogar(historico):
    print("\n=== JOGO DOS ANIMAIS ===")
    print("Responda apenas com 's' ou 'n'.")

    animal = "Desconhecido"

    mamifero = input("É mamífero? ").lower()
    if mamifero == "s":
        quadrupede = input("É quadrúpede? ").lower()
        if quadrupede == "s":
            carnivoro = input("É carnívoro? ").lower()
            if carnivoro == "s":
                animal = "Leão"
            else:
                herbivoro = input("É herbívoro? ").lower()
                if herbivoro == "s":
                    animal = "Cavalo"
        else:
            bipede = input("É bípede? ").lower()
            if bipede == "s":
                onivoro = input("É onívoro? ").lower()
                if onivoro == "s":
                    animal = "Homem"
                else:
                    frutifero = input("É frutífero? ").lower()
                    if frutifero == "s":
                        animal = "Macaco"
            else:
                voador = input("É voador? ").lower()
                if voador == "s":
                    animal = "Morcego"
                else:
                    aquatico = input("É aquático? ").lower()
                    if aquatico == "s":
                        animal = "Baleia"
    else:
        ave = input("É ave? ").lower()
        if ave == "s":
            nao_voadora = input("É não-voadora? ").lower()
            if nao_voadora == "s":
                tropical = input("É tropical? ").lower()
                if tropical == "s":
                    animal = "Avestruz"
                else:
                    animal = "Pinguim"
            else:
                nadadora = input("É nadadora? ").lower()
                if nadadora == "s":
                    animal = "Pato"
                else:
                    rapina = input("É de rapina? ").lower()
                    if rapina == "s":
                        animal = "Águia"
        else:
            reptil = input("É réptil? ").lower()
            if reptil == "s":
                com_casco = input("Tem casco? ").lower()
                if com_casco == "s":
                    animal = "Tartaruga"
                else:
                    carnivoro = input("É carnívoro? ").lower()
                    if carnivoro == "s":
                        animal = "Crocodilo"
                    else:
                        sem_patas = input("Não tem patas? ").lower()
                        if sem_patas == "s":
                            animal = "Cobra"
    print(f"\nEntão o animal identificado foi: {animal}\n")

    if len(historico) == 10:
        historico.pop(0)
    historico.append(animal)


def ver_top10(historico):
    print("\n=== ÚLTIMOS 10 ANIMAIS IDENTIFICADOS ===")
    if not historico:
        print("Nenhum animal identificado ainda.\n")
    else:
        for i, a in enumerate(historico, start=1):
            print(f"{i}. {a}")
    print()
    
def main():
    historico = []
    while True:
        print("MENU DE OPÇÕES")
        print("1 - JOGAR")
        print("2 - VER TOP 10")
        print("3 - SAIR")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            jogar(historico)
        elif opcao == "2":
            ver_top10(historico)
        elif opcao == "3":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")
            
if __name__ == "__main__":
    main()
