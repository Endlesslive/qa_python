from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""


    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"


    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Три мушкетёра")
        collector.set_book_genre("Три мушкетёра", "Роман")
        assert collector.get_book_genre("Три мушкетёра") == ""


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


    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.favorites


    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")  # Повтор
        assert collector.favorites.count("Преступление и наказание") == 1


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


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.add_new_book("Детектив в Париже")
        collector.set_book_genre("Детектив в Париже", "Детективы")
        collector.add_new_book("Маша и медведь")
        collector.set_book_genre("Маша и медведь", "Мультфильмы")

        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert horror_books == ["Сияние"]

        comedy_books = collector.get_books_with_specific_genre("Комедии")
        assert comedy_books == []


    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()
        collector.add_new_book("Остров сокровищ")
        collector.set_book_genre("Остров сокровищ", "Приключения")
        collector.add_new_book("Звёздные войны")
        collector.set_book_genre("Звёздные войны", "Фантастика")

        books_dict = collector.get_books_genre()
        assert books_dict == {
            "Остров сокровищ": "Приключения",
            "Звёздные войны": "Фантастика"
        }