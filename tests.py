from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"


    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_books_genre() == {"Гарри Поттер": "Фантастика"}

    def test_get_book_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", "Мультфильмы")
        collector.add_new_book("Ужасы в подвале")
        collector.set_book_genre("Ужасы в подвале", "Ужасы")
        collector.add_new_book("Комедия про кота")
        collector.set_book_genre("Комедия про кота", "Комедии")

        children_books = collector.get_books_for_children()
        assert "Маленький принц" in children_books
        assert "Комедия про кота" in children_books
        assert "Ужасы в подвале" not in children_books


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.favorites


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Анна Каренина")
        collector.add_book_in_favorites("Анна Каренина")
        collector.delete_book_from_favorites("Анна Каренина")
        assert "Анна Каренина" not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Братья Карамазовы")
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Братья Карамазовы")
        collector.add_book_in_favorites("Дюна")
        favorites = collector.get_list_of_favorites_books()
        assert "Братья Карамазовы" in favorites
        assert "Дюна" in favorites
        assert len(favorites) == 2