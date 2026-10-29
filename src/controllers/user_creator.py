from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface # noqa


class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface):  # Inverção da dependência - D SOLID # noqa
        self.__users_repository = users_repository

        def insert_new_user(self, person_name: str, age: int, height: float) -> dict: # noqa
        self.__check_if_user_exists(person_name)
        self.__create_new_user(person_name, age, height)
        return self.__format_response()

    def __check_if_user_exists(self, person_name: str) -> None:
        select_users = self.__users_repo.select_user(person_name)
        if not select_users or len(select_users) == 0:
            return

        raise Exception("Usuario já cadastrado!")

    def __create_new_user(self, person_name: str, age: int, height: float) -> None: # noqa
        # outras atividades caso necessário
        self.__users_repo.insert_user(person_name, age, height)

    def __format_response(self) -> dict:
        return {
            "type": "Users",
            "count": 1,
            "message": "Usuário cadastrado com sucesso!"
        }