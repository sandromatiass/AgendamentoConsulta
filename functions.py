import datetime
from patients_data import lista_de_pacientes

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

