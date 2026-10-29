from src.models.connection.db_connection_handler import DBConnectionHandler
from src.models.entities.users import Users
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface # noqa


class UserRepository(UsersRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler):
        self.__db_connection_handler = db_connection

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        with self.__db_conn_handler as database:
            try:
                new_user = Users(
                    person_name=person_name,
                    age=age,
                    height=height
                )
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

            def select_user(self, person_name: str) -> list[Users]:
                with self.__db_conn_handler as database:
                    users = (
                        database.session
                        .query(Users)
                        .filter(Users.person_name == person_name)
                        .all()
                    )
                return users