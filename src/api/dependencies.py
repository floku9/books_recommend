from typing import Annotated

from fastapi import Depends

from data.uow.abstract_uow import AbstractUnitOfWorkAsync
from data.uow.sql_orm_uow import SQLORMUnitOfWork

UOWDependency = Annotated[AbstractUnitOfWorkAsync, Depends(SQLORMUnitOfWork)]
