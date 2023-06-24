from Database import Database
from SimpsonsDatabase import SimpsonsDatabase

db = Database("bolt://3.237.90.25:7687", "neo4j", "runs-slashes-components")
db.drop_all()

members_database = SimpsonsDatabase(db)


def cria_simpsons():
    members_database.create_member("Clancy", "Aposentado", 95)
    members_database.create_member("Abe", "Aposentado", 83)
    members_database.create_member("Marge", "Dona de casa", 38)
    members_database.create_member("Homer", "Inspetor de segurança", 38)
    members_database.create_member("Lisa", "Estudante", 8)
    members_database.create_member("Maggie", "sem profissao", 1)
    members_database.create_member("Bart", "Estudante", 10)
    members_database.create_member("Ned", "Balconista", 60)
    members_database.create_member("Maude", "Ativista", 50)
    members_database.create_member("Rod", "Estudante", 9)
    members_database.create_member("Todd", "Estudante", 7)
    members_database.create_member("Mona", "artista", 100)
    members_database.create_animal_member("Bola de neve", "Gato")
    members_database.create_animal_member("Ajudante do papai Noel", "Cachorro")
    members_database.create_parents_relationship("Abe", "Homer")
    members_database.create_parents_relationship("Clancy", "Marge")
    members_database.create_parents_relationship("Homer", "Bart")
    members_database.create_parents_relationship("Homer", "Lisa")
    members_database.create_parents_relationship("Homer", "Maggie")
    members_database.create_parents_relationship("Marge", "Bart")
    members_database.create_parents_relationship("Marge", "Lisa")
    members_database.create_parents_relationship("Marge", "Maggie")
    members_database.create_parents_relationship("Mona", "Ned")
    members_database.create_parents_relationship("Ned", "Rod")
    members_database.create_parents_relationship("Ned", "Todd")
    members_database.create_parents_relationship("Maude", "Rod")
    members_database.create_parents_relationship("Maude", "Todd")
    members_database.create_pet_relationship("Bart", "Ajudante do papai Noel")
    members_database.create_pet_relationship("Lisa", "Bola de neve")
    members_database.create_married_relationship("Homer", "Marge")
    members_database.create_married_relationship("Ned", "Maude")


def exibir_menu():
    print("Bem-vindo(a) ao programa!")
    print("Aqui estão as ações disponíveis:")
    print("1. Adicionar novo Membro")
    print("2. Descobrir quais pessoas possuem determinada profissao")
    print("3. Fazer o update de um membro")
    print("4. Deletar um membro")
    print("5. Adiconar relacionamentos")
    print("6. Sair")


def executar_acao(acao):
    if acao == 1:
        print("Executando a Ação 1...")
        members_database.create_member_from_user_input()
    elif acao == 2:
        print("Executando a Ação 2...")
        pergunta = input("Digite a profissao que deseja buscar: ")
        resultado = members_database.query_family_graph(pergunta)
        print(resultado)
    elif acao == 3:
        print("Executando a Ação 3...")
        members_database.update_member()
    elif acao == 4:
        print("Executando a Ação 4")
        members_database.delete_member()
    elif acao == 5:
        print("Executando a Açao 5")
        members_database.create_relationship_from_user_input()
    elif acao == 6:
        return False
    else:
        print("Opção inválida. Por favor, escolha uma ação válida.")

    return True


# Função principal
def main():
    cria_simpsons()
    print("Grafo Simpsons criado")
    exibir_menu()
    executar = True
    while executar:
        acao = int(input("Escolha uma ação (1-6): "))
        executar = executar_acao(acao)


if __name__ == "__main__":
    main()

db.close()
