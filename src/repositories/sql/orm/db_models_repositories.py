from db.models.author import Author
from db.models.book import Book
from db.models.genre import Genre
from db.models.recommendation import Recommendation
from db.models.request import Request
from db.models.user import User
from repositories.sql.orm.generic_repository import GenericORMRepository


class AuthorRepository(GenericORMRepository[Author]):
    model = Author


class BookRepository(GenericORMRepository[Book]):
    model = Book


class UserRepository(GenericORMRepository[User]):
    model = User


class GenreRepository(GenericORMRepository[Genre]):
    model = Genre


class RequestRepository(GenericORMRepository[Request]):
    model = Request


class RecommendationRepository(GenericORMRepository[Recommendation]):
    model = Recommendation
