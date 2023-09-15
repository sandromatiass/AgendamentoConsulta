def marcar_consulta(paciente, agenda):
    print("\nEscolha uma especialidade para a consulta:")
    especialidades = list(agenda.keys())
    for i, especialidade in enumerate(especialidades, start=1):
        print(f"{i}. {especialidade}")

    while True:
        try:
            escolha_especialidade = int(input("Digite o número da especialidade desejada: "))
            if 1 <= escolha_especialidade <= len(especialidades):
                especialidade_escolhida = especialidades[escolha_especialidade - 1]
                break
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Seleção do dia
    print(f"\nEscolha um dia disponível para a consulta:")
    dias = list(agenda[especialidade_escolhida].keys())
    for i, dia in enumerate(dias, start=1):
        print(f"{i}. {dia}")

    while True:
        try:
            escolha_dia = int(input("Digite o número do dia desejado: "))
            if 1 <= escolha_dia <= len(dias):
                dia_escolhido = dias[escolha_dia - 1]
                break
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Seleção do período
    print("\nEscolha um período disponível para a consulta (Manhã ou Tarde):")
    periodos = list(agenda[especialidade_escolhida][dia_escolhido].keys())
    for i, periodo in enumerate(periodos, start=1):
        print(f"{i}. {periodo}")

    while True:
        try:
            escolha_periodo = int(input("Digite o número do período desejado: "))
            if 1 <= escolha_periodo <= len(periodos):
                periodo_escolhido = periodos[escolha_periodo - 1]
                break
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Seleção do horário
    horarios_disponiveis = agenda[especialidade_escolhida][dia_escolhido][periodo_escolhido]
    print("\nEscolha um horário disponível para a consulta:")
    for i, horario in enumerate(horarios_disponiveis, start=1):
        print(f"{i}. {horario}")

    while True:
        try:
            escolha_horario = int(input("Digite o número do horário desejado: "))
            if 1 <= escolha_horario <= len(horarios_disponiveis):
                horario_escolhido = horarios_disponiveis[escolha_horario - 1]
                break
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    print(f"\nSr(a). {paciente['Nome']}, a consulta foi marcada com sucesso para a especialidade: {especialidade_escolhida}")
    print(f"Dia: {dia_escolhido}")
    print(f"Período: {periodo_escolhido}")
    print(f"Horário: {horario_escolhido}")
    print("Tenha um ótimo dia, esperamos você.")
