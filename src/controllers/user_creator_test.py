from src.controllers.user_creator import UserCreator

# Classe Mock


class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

    def insert_user(self, person_name: str, age: int, height: float) -> None:
            self.insert_user_att["person_name"] = person_name
            self.insert_user_att["age"] = age
            self.insert_user_att["height"] = height
            return


def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    person_name = "my_person_name"
    age = 33
    height = 1.69

    response = user_creator.insert_new_user(person_name, age, height)
    
    assert user_repository.select_user_att["person_name"] == person_name
    assert isinstance(response, dict)
    assert "type" in response
    assert response["count"] == 1
    assert response["message"] == "Usuario cadastrado com sucesso!"