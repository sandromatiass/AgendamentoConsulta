import datetime
from agenda import agenda


def obter_resposta_valida():
    while True:
        resposta = input("Por favor, responda com 'sim' ou 'não': ").lower()
        if resposta in ["sim", "não"]:
            return resposta
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False

    if not cpf.isdigit():
        return False

    digitos = cpf 
    soma1 = sum(int(digitos[i]) * (10 - i) for i in range(9))
    soma2 = sum(int(digitos[i]) * (11 - i) for i in range(10))
    digito1 = (soma1 * 10) % 11
    digito2 = (soma2 * 10) % 11

    if digito1 == 10:
        digito1 = 0
    if digito2 == 10:
        digito2 = 0

    if int(digitos[9]) != digito1 or int(digitos[10]) != digito2:
        return False

    return True

def cpf_cadastrado(cpf):
    cadastros = ["12643717643", "11585280437", "11122233344"]
    return cpf in cadastros

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

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


def obter_dados_paciente(cpf):
    lista_de_pacientes = [
        {
            "CPF": "12345678901",
            "Data de Nascimento": "20/05/1994",
            "Telefone/Celular": "8299997777",
            "Sexo": "Masculino",
            "Nome": "João"
        },
        {
            "CPF": "98765432101",
            "Data de Nascimento": "08/05/1994",
            "Telefone/Celular": "8299998888",
            "Sexo": "Feminino",
            "Nome": "Maria"
        },
    ]