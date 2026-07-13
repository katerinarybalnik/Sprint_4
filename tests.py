from main import BooksCollector
import pytest

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
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

        #проверка,что у новой книги нет жанра
    def test_add_new_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Фиксики')

        assert collector.get_book_genre('Фиксики') == ''
    
        # Проверка, что устанавливается жанр книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Феиринки')
        collector.set_book_genre('Феиринки', 'Мультфильмы')

        assert collector.get_book_genre('Феиринки') == 'Мультфильмы'
    
    
        # Проверка получения жанра книги по названию
    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Феиринки')
        collector.set_book_genre('Феиринки', 'Мультфильмы')

        assert collector.get_book_genre('Феиринки') == 'Мультфильмы'
        
    
        # Проверка получения списка книг определенного жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Феиринки')
        collector.set_book_genre('Феиринки', 'Мультфильмы')

        collector.add_new_book('Один дома')
        collector.set_book_genre('Один дома', 'Ужасы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Феиринки']
    
        # Проверка получения словаря всех книг
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Феиринки')

        assert collector.get_books_genre() == {'Феиринки': ''}

        # Проверка книг, которые подходят детям
    @pytest.mark.parametrize('genre, result', [('Мультфильмы',True),('Ужасы', False),('Детективы', False)])
    def test_get_books_for_children(self, genre, result):
        collector = BooksCollector()

        collector.add_new_book('Книга')

        collector.set_book_genre('Книга', genre)

        books = collector.get_books_for_children()

        if result:
            assert 'Книга' in books
        else:
            assert 'Книга' not in books

        # Проверка добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.add_book_in_favorites('Поющие в терновнике')

        assert collector.get_list_of_favorites_books() == ['Поющие в терновнике']


        # Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.add_book_in_favorites('Поющие в терновнике')

        collector.delete_book_from_favorites('Поющие в терновнике')

        assert collector.get_list_of_favorites_books() == []

        # Проверка получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.add_book_in_favorites('Поющие в терновнике')

        assert collector.get_list_of_favorites_books() == ['Поющие в терновнике']



    




