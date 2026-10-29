import pytest
from .db_connection_handler import DBConnectionHandler


@pytest.mark.skip(reason="Integration with DB")
def test_db_connection():
    db_conn_handler = DBConnectionHandler()

    assert db_conn_handler.session is None

    with db_conn_handler:
        assert db_conn_handler.session is not None