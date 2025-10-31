print("CENSO 2025 - LEVANTAMENTO DEMOGRÁFICO")

total_residencias = 0
total_pessoas = 0
soma_idades_geral = 0
qtd_homens = qtd_mulheres = qtd_nao_inf = 0
soma_salarios_geral = 0
pessoas_com_salario = 0

while True:
    qtd = int(input("\nQuantas pessoas moram na residência? "))
    if qtd == 0:
        break

    total_residencias += 1
    soma_idades_residencia = 0
    soma_sal_homens = soma_sal_mulheres = 0
    qtd_homens_res = qtd_mulheres_res = 0

    for i in range(1, qtd + 1):
        print(f"\nPessoa {i}:")
        idade = int(input("Idade: "))
        sexo = input("Sexo (homem/mulher/não informado): ").strip().lower()
        salario = float(input("Salário: "))
        total_pessoas += 1
        soma_idades_geral += idade

        if sexo == "homem":
            qtd_homens += 1
            if salario > 0:
                soma_sal_homens += salario
                soma_salarios_geral += salario
                pessoas_com_salario += 1
                qtd_homens_res += 1
        elif sexo == "mulher":
            qtd_mulheres += 1
            if salario > 0:
                soma_sal_mulheres += salario
                soma_salarios_geral += salario
                pessoas_com_salario += 1
                qtd_mulheres_res += 1
        else:
            qtd_nao_inf += 1

        soma_idades_residencia += idade

    media_idade_res = soma_idades_residencia / qtd
    media_sal_homens = soma_sal_homens / qtd_homens_res if qtd_homens_res > 0 else 0
    media_sal_mulheres = soma_sal_mulheres / qtd_mulheres_res if qtd_mulheres_res > 0 else 0

    print(f"\n--- RESIDÊNCIA {total_residencias} ---")
    print(f"Total de pessoas: {qtd}")
    print(f"Média de idades: {media_idade_res:.1f}")
    print(f"Média salarial dos homens: R$ {media_sal_homens:.2f}")
    print(f"Média salarial das mulheres: R$ {media_sal_mulheres:.2f}")

if total_pessoas > 0:
    media_idade_geral = soma_idades_geral / total_pessoas
    media_salarial_geral = soma_salarios_geral / pessoas_com_salario if pessoas_com_salario > 0 else 0

    print("\nRELATÓRIO FINAL DO CENSO 2025")
    print(f"Total de residências: {total_residencias}")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Média geral de idades: {media_idade_geral:.1f}")
    print(f"Homens: {qtd_homens} | Mulheres: {qtd_mulheres} | Não informado: {qtd_nao_inf}")
    print(f"Média salarial geral: R$ {media_salarial_geral:.2f}")
else:
    print("\nNenhuma residência foi registrada.")
