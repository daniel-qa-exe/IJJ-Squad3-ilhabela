from faker import Faker

faker = Faker('pt_BR')

persona = {
    "Nome":faker.name(),
    "Endereço": faker.address()
}
print(persona)

