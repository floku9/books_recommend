from uow.sql_orm_uow import SQLORMUnitOfWork


class GenericUOWService:
    def __init__(self, uow: SQLORMUnitOfWork):
        self._uow = uow
