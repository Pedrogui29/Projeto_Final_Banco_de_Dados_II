class SimpsonsDatabase:
    def __init__(self, database):
        self.db = database



    def create_member(self, name, profissao, idade):
        query = "CREATE (:Member {name: $name, profissao: $profissao, idade: $idade})"
        parameters = {"name": name, "profissao": profissao, "idade": idade}
        self.db.execute_query(query, parameters)

    def create_member_from_user_input(self):
        name = input("Digite o nome do membro: ")
        profissao = input("Digite a profissão do membro: ")
        idade = input("Digite a idade do membro: ")

        query = "CREATE (:Member {name: $name, profissao: $profissao, idade: $idade})"
        parameters = {"name": name, "profissao": profissao, "idade": idade}
        self.db.execute_query(query, parameters)
        print("Membro Simpson Criado com sucesso")

    def create_animal_member(self, name, pet):
        query = "CREATE (:Member {name: $name, pet: $pet})"
        parameters = {"name": name, "pet": pet}
        self.db.execute_query(query, parameters)

    def get_member(self):
        query = "MATCH (p:Member) RETURN p.name AS name, p.profissao AS profissao, p.idade AS idade"
        results = self.db.execute_query(query)
        return [(result["name"], result["profissao"], result["idade"]) for result in results]

    def get_animal_member(self):
        query = "MATCH (p:Member) RETURN p.name AS name, p.pet AS pet"
        results = self.db.execute_query(query)
        return [(result["name"], result["pet"]) for result in results]

    def update_member(self):
        old_name = input("Digite o nome do membro que deseja alterar: ")
        new_name = input("Digite o novo nome do membro: ")

        update_profissao = input("Deseja atualizar a profissão do membro? (S/N): ")
        if update_profissao.upper() == "S":
            new_profissao = input("Digite a nova profissão do membro: ")
        else:
            new_profissao = None

        update_idade = input("Deseja atualizar a idade do membro? (S/N): ")
        if update_idade.upper() == "S":
            new_idade = input("Digite a nova idade do membro: ")
        else:
            new_idade = None

        query = "MATCH (p:Member {name: $old_name}) "
        if new_name:
            query += "SET p.name = $new_name "
        if new_profissao:
            query += "SET p.profissao = $new_profissao "
        if new_idade:
            query += "SET p.idade = $new_idade "

        parameters = {
            "old_name": old_name,
            "new_name": new_name,
            "new_profissao": new_profissao,
            "new_idade": new_idade
        }

        self.db.execute_query(query, parameters)
        print("Dados do membro atualizados com sucesso")

    def delete_member(self):
        name = input("Digite o membro que deseja deletar: ")
        query = "MATCH (p:Member {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_parents_relationship(self, parent_name, child_name):
        query = "MATCH (parent:Member {name: $parent_name}), (child:Member {name: $child_name}) CREATE (parent)-[:pai]->(child)"
        parameters = {"parent_name": parent_name, "child_name": child_name}
        self.db.execute_query(query, parameters)

    def create_relationship_from_user_input(self):
        pergunta = input("Digite qual tipo de relacionamento você deseja criar: Parentesco, Esposo, Namorado, Dono ")


        if pergunta == "Parentesco":
            self.create_parents_relationship_input()
        elif pergunta == "Esposo":
            self.create_married_relationship_input()
        elif pergunta == "Namorado":
            self.create_boyfriend_relationship_input()
        elif pergunta == "Dono":
            self.create_pet_relationship_input()

    def create_parents_relationship_input(self):
        parent_name = input("Digite o nome da primeira pessoa do relacionamento")
        child_name = input("Digite o nome da segunda pessoa do relacionamento")
        query = "MATCH (parent:Member {name: $parent_name}), (child:Member {name: $child_name}) CREATE (parent)-[:Pai]->(child)"
        parameters = {"parent_name": parent_name, "child_name": child_name}
        self.db.execute_query(query, parameters)

    def create_married_relationship_input(self):
        esposo1_name = input("Digite o nome da primeira pessoa do relacionamento")
        esposo2_name = input("Digite o nome da segunda pessoa do relacionamento")
        query = "MATCH (esposo1:Member {name: $esposo1_name}), (esposo2:Member {name: $esposo2_name}) CREATE (esposo1)-[:Casado]->(esposo2)"
        parameters = {"esposo1_name": esposo1_name, "esposo2_name": esposo2_name}
        self.db.execute_query(query, parameters)

    def create_boyfriend_relationship_input(self):
        boyfriend_name = input("Digite o nome da primeira pessoa do relacionamento")
        girlfriend_name = input("Digite o nome da segunda pessoa do relacionamento")
        query = "MATCH (boyfriend:Member {name: $boyfriend_name}), (girlfriend:Member {name: $girlfriend_name}) CREATE (boyfriend)-[:namorado]->(girlfriend)"
        parameters = {"boyfriend_name": boyfriend_name, "girlfriend_name": girlfriend_name}
        self.db.execute_query(query, parameters)

    def create_pet_relationship_input(self):
        owner_name = input("Digite o nome da primeira pessoa do relacionamento")
        pet_name = input("Digite o nome do pet do relacionamento")
        query = "MATCH (owner:Member {name: $owner_name}), (pet:Member {name: $pet_name}) CREATE (owner)-[:dono]->(pet)"
        parameters = {"owner_name": owner_name, "pet_name": pet_name}
        self.db.execute_query(query, parameters)

    def create_married_relationship(self, esposo1_name, esposo2_name):
        query = "MATCH (esposo1:Member {name: $esposo1_name}), (esposo2:Member {name: $esposo2_name}) CREATE (esposo1)-[:casado]->(esposo2)"
        parameters = {"esposo1_name": esposo1_name, "esposo2_name": esposo2_name}
        self.db.execute_query(query, parameters)

    def create_boyfriend_relationship(self, boyfriend_name, girlfriend_name):
        query = "MATCH (boyfriend:Member {name: $boyfriend_name}), (girlfriend:Member {name: $girlfriend_name}) CREATE (boyfriend)-[:namorado]->(girlfriend)"
        parameters = {"boyfriend_name": boyfriend_name, "girlfriend_name": girlfriend_name}
        self.db.execute_query(query, parameters)

    def create_pet_relationship(self, owner_name, pet_name):
        query = "MATCH (owner:Member {name: $owner_name}), (pet:Member {name: $pet_name}) CREATE (owner)-[:dono]->(pet)"
        parameters = {"owner_name": owner_name, "pet_name": pet_name}
        self.db.execute_query(query, parameters)


    def query_family_graph(self, question):
        query = None
        if "Estudante" in question:
            query = "MATCH (member:Member {profissao: 'Estudante'}) RETURN member.name AS name"
        if query:
            result = self.db.execute_query(query)
            return [record["name"] for record in result]
        else:
            return "Desculpe, não entendi a pergunta."

