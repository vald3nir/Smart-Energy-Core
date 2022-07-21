from src.domain.use_cases import database_use_case


def restore_db():
    database_use_case.restore_db()
