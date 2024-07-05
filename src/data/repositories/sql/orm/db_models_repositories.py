from data.db.models.author import Author
from data.db.models.book import Book, BookAuthors, BookGenres
from data.db.models.genre import Genre
from data.db.models.recommendation import Recommendation
from data.db.models.request import Request
from data.db.models.user import User
from data.repositories.sql.orm.generic_repository import GenericORMRepository


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


class BookAuthorsRepository(GenericORMRepository[BookAuthors]):
    model = BookAuthors


class BookGenresRepository(GenericORMRepository[BookGenres]):
    model = BookGenres
