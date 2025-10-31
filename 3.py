print("ELEIÇÕES GRANTIETÊ 2025 - URNA ELETRÔNICA")
candidatos = {
    13: ("Márcio", "Partido da Tecnologia (PT)"),
    35: ("Capella", "Partido dos Matemáticos (PM)"),
    51: ("Gallo", "Partido da Coordenação (PC)"),
    60: ("José Mangili", "Partido das Arquiteturas de Computador (PAC)")
}

votos = {13: 0, 35: 0, 51: 0, 60: 0}
votos_brancos = 0
votos_nulos = 0
alunos_votaram = []

while True:
    aluno = input("\nDigite o número do aluno (0 para encerrar): ")
    if not aluno.isdigit():
        print("Digite apenas números.")
        continue

    aluno = int(aluno)
    if aluno == 0:
        break

    if aluno in alunos_votaram:
        print("Este aluno já votou! Tente outro número.")
        continue

    voto = int(input("Digite seu voto: "))
    if voto in candidatos:
        nome, partido = candidatos[voto]
        confirmacao = input(f"Confirma seu voto em “{nome} - {partido}”? (sim/não): ").lower()
        if confirmacao == "sim":
            votos[voto] += 1
            print("Voto computado com sucesso!")
            alunos_votaram.append(aluno)
        else:
            print("Voto cancelado, tente novamente.")
            continue

    elif voto == 0:
        confirmacao = input("Confirma seu voto em “Branco”? (sim/não): ").lower()
        if confirmacao == "sim":
            votos_brancos += 1
            print("Voto em branco computado com sucesso!")
            alunos_votaram.append(aluno)
        else:
            print("Voto cancelado, tente novamente.")
            continue
    else:
        confirmacao = input("Confirma seu voto em “Nulo”? (sim/não): ").lower()
        if confirmacao == "sim":
            votos_nulos += 1
            print("Voto nulo computado com sucesso!")
            alunos_votaram.append(aluno)
        else:
            print("Voto cancelado, tente novamente.")
            continue

total_votos = sum(votos.values()) + votos_brancos + votos_nulos
total_validos = sum(votos.values())

print("\nRESULTADO DAS ELEIÇÕES GRANTIETÊ 2025")
print(f"Total de votos apurados: {total_votos}\n")

for numero, (nome, partido) in candidatos.items():
    qtd = votos[numero]
    porcentagem = (qtd / total_validos * 100) if total_validos > 0 else 0
    print(f"{nome} ({partido}): {qtd} votos ({porcentagem:.1f}%)")

print(f"\nVotos brancos: {votos_brancos}")
print(f"Votos nulos: {votos_nulos}")

if total_validos > 0:
    vencedor_numero = max(votos, key=votos.get)
    vencedor_nome, vencedor_partido = candidatos[vencedor_numero]
    print(f"\nCandidato mais votado: {vencedor_nome} com {votos[vencedor_numero]} voto(s)")
else:
    print("\nNenhum voto válido foi registrado.")
