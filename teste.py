import datetime

agenda = {
    "Cardiologia": {
        "Segunda-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Terça-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quarta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quinta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Sexta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
    },
    "Dermatologia": {
        "Segunda-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Terça-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quarta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quinta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Sexta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
    },
    "Ginecologia": {
        "Segunda-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Terça-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quarta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quinta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Sexta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
    },
    "Ortopedista": {
        "Segunda-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Terça-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quarta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Quinta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
        "Sexta-feira": {"Manhã": ["9:30", "10:30", "11:30", "12:30", "13:30"], "Tarde": ["14:30", "15:30", "16:30", "17:30", "18:30"]},
    }
}

lista_de_pacientes = [
        {
            "CPF": "13023033043",
            "Data de Nascimento": "20/05/1994",
            "Telefone/Celular": "8299997777",
            "Sexo": "Masculino",
            "Nome": "Sandro"
        },
        {
            "CPF": "12022032042",
            "Data de Nascimento": "08/05/1994",
            "Telefone/Celular": "8299998888",
            "Sexo": "Feminino",
            "Nome": "Dane"
        },
    ]

def obter_resposta_valida():
    while True:
        resposta = input("Por favor, responda com 'sim' ou 'não': ").lower()
        if resposta in ["sim", "não"]:
            return resposta
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def validar_cpf(cpf):
    if len(cpf) < 11:
        return False
    elif len(cpf) > 11:
        return False
    else:
        return True

def obter_dados_paciente(cpf):
    for paciente in lista_de_pacientes:
        if paciente["CPF"] == cpf:
            return paciente
    return None

def cadastrar_paciente():
    while True:
        cpf = input("Por favor, informe seu CPF: ")
        if cpf.lower() == "fake":
            print(f"CPF {cpf} foi recebido.")
            break
        elif validar_cpf(cpf):
            print(f"Seu CPF {cpf} foi recebido.")
            break
        else:
            print("CPF inválido. Por favor, verifique o número do CPF.")

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

def saudacao():
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def main():
    print(saudacao())

    cpf = ""

    print("Deseja marcar uma consulta? (sim/não): ")
    resposta = input().lower()

    if resposta == "sim":
        print("Ótimo! Você já realizou algum exame em nossa unidade?")
        realizou_exame = input().lower()

        if realizou_exame == "sim":
            while True:
                cpf = input("Por favor, informe seu CPF: ")
                if cpf.lower() == "fake":
                    print(f"CPF {cpf} foi recebido.")
                    break
                elif validar_cpf(cpf):
                    print(f"Seu CPF {cpf} foi recebido.")
                    paciente = obter_dados_paciente(cpf)
                    if paciente:
                        print(f"\nSr. {paciente['Nome']} seu CPF está cadastrado. Prossiga com a marcação da consulta.")
                        print("\nDados do paciente:")
                        print(f"CPF: {paciente['CPF']}")
                        print(f"Data de Nascimento: {paciente['Data de Nascimento']}")
                        print(f"Telefone/Celular: {paciente['Telefone/Celular']}")
                        print(f"Sexo: {paciente['Sexo']}")
                        marcar_consulta(paciente, agenda)
                        break
                    else:
                        print("CPF não encontrado. Por favor, verifique o número do CPF.")
                else:
                    print("CPF inválido. Por favor, verifique o número do CPF.")
        else:
            print("Informe sua data de nascimento:")
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            data_nascimento = datetime.date(ano, mes, dia)
            idade = calcular_idade(data_nascimento)

            if idade < 18:
                print("Desculpe, apenas maiores de 18 anos podem marcar consultas.")
            else:
                nome = input("Informe seu nome: ")

                telefone = input("Informe seu telefone ou celular: ")

                while True:
                    try:
                        sexo_opcao = int(input("Informe seu sexo (1 para Masculino, 2 para Feminino): "))
                        if sexo_opcao == 1:
                            sexo = "Masculino"
                            break
                        elif sexo_opcao == 2:
                            sexo = "Feminino"
                            break
                        else:
                            print("Opção inválida. Por favor, escolha 1 para Masculino, 2 para Feminino.")
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número válido.")
                paciente = {
                    "CPF": cpf,
                    "Data de Nascimento": data_nascimento,
                    "Idade": idade,
                    "Nome": nome,
                    "Telefone/Celular": telefone,
                    "Sexo": sexo
                }
                print(f"\nCadastro realizado com sucesso! Sr(a). {paciente['Nome']}")
                print("\nDados do paciente:")
                print(f"Nome: {paciente['Nome']}")
                print(f"Idade: {paciente['Idade']} anos")
                print(f"Telefone/Celular: {paciente['Telefone/Celular']}")
                print(f"Sexo: {paciente['Sexo']}")

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
                print("\nEscolha um dia disponível para a consulta:")
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

                print(f"\nSr(a). {nome}, a consulta foi marcada com sucesso para a especialidade: {especialidade_escolhida}")
                print(f"Dia: {dia_escolhido}")
                print(f"Período: {periodo_escolhido}")
                print(f"Horário: {horario_escolhido}")
                print("Tenha um ótimo dia, esperamos você.")
    else:
        print("Tudo certo, volte sempre. Até mais!")
if __name__ == "__main__":
    main()
