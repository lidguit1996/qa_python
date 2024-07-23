from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_init_books_genre_in_class_object(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_init_favorites_in_class_object(self):
        collector = BooksCollector()
        assert collector.favorites == []

    @pytest.mark.parametrize('genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_genre_in_class_object(self, genres):
        collector = BooksCollector()
        assert genres in collector.genre

    @pytest.mark.parametrize('genres_age_rating', ['Ужасы', 'Детективы'])
    def test_init_genre_age_rating_in_class_object(self, genres_age_rating):
        collector = BooksCollector()
        assert genres_age_rating in collector.genre_age_rating

    def test_add_new_book_for_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        assert collector.books_genre['Оно'] == ''

    def test_set_book_genre_for_book_name_and_genre_name(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_get_book_genre_for_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        book_genre = collector.get_book_genre('Оно')
        assert book_genre == 'Ужасы'

    def test_get_books_with_specific_genre_for_genre_name(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Собака Баскервиллей')
        collector.set_book_genre('Собака Баскервиллей', 'Детективы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Ужасы')
        assert books_with_specific_genre == ['Оно', 'Сияние']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Собака Баскервиллей')
        collector.set_book_genre('Собака Баскервиллей', 'Детективы')
        collector.add_new_book('Волшебник изумрудного города')
        collector.set_book_genre('Волшебник изумрудного города', 'Мультфильмы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Волшебник изумрудного города', 'Гарри Поттер']

    def test_add_book_in_favorites_for_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.favorites == ['Гарри Поттер']

    def test_delete_book_from_favorites_for_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Собака Баскервиллей')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Собака Баскервиллей')
        favorites_list = collector.get_list_of_favorites_books()
        assert favorites_list == ['Гарри Поттер', 'Собака Баскервиллей']
