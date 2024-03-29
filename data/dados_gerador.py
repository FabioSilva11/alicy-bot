from faker import Faker

# Inicializa o Faker com localização para português do Brasil
faker = Faker('pt_BR')

def gerar_cpf():
    cpf = faker.cpf()
    nome = faker.name()
    endereco = faker.address()
    email = faker.email()
    telefone = faker.phone_number()

    introducao = "Conforme solicitado, aqui estão os detalhes solicitados:"
    resposta = (
        f"{introducao}\n\n"
        f"-💳 CPF:- {cpf}\n"
        f"-👤 Nome:- {nome}\n"
        f"-🏠 Endereço:- {endereco}\n"
        f"-📧 E-mail:- {email}\n"
        f"-📞 Telefone:- {telefone}"
    )

    return resposta

def gerar_cc():
    introducao = "Conforme solicitado, aqui estão os detalhes solicitados:"
    numero_cartao = faker.credit_card_number()
    nome_titular = faker.name()
    data_validade = faker.credit_card_expire()
    cvv = faker.credit_card_security_code()
    bandeira = faker.credit_card_provider()
    banco_emissor = faker.credit_card_full()
    endereco_cobranca = faker.address()

    resposta = (
        f"{introducao}\n\n"
        f"-💳 Número do cartão de crédito:- {numero_cartao}\n"
        f"-👤 Nome do titular:- {nome_titular}\n"
        f"-📅 Data de validade:- {data_validade}\n"
        f"-🔒 CVV:- {cvv}\n"
        f"-💳 Bandeira do cartão:- {bandeira}\n"
        f"-🏦 Banco emissor:- {banco_emissor}\n"
        f"-🏠 Endereço de cobrança associado ao cartão:- {endereco_cobranca}"
    )

    return resposta
