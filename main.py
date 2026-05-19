import sys
from datetime import datetime
from storage import BookStorage
from stats import calculate_average_rating, get_statistics_by_author
from models import Book


def print_menu():
    """Выводит главное меню"""
    print("\n" + "=" * 50)
    print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("=" * 50)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("=" * 50)


def add_book(storage: BookStorage):
    """Добавляет новую книгу"""
    print("\n--- Добавление новой книги ---")
    
    author = input("Введите автора: ").strip()
    if not author:
        print("Ошибка: автор не может быть пустым")
        return
    
    title = input("Введите название: ").strip()
    if not title:
        print("Ошибка: название не может быть пустым")
        return
    
    # Ввод и проверка оценки
    try:
        rating = int(input("Введите оценку (1-5): ").strip())
        if not 1 <= rating <= 5:
            print("Ошибка: оценка должна быть от 1 до 5")
            return
    except ValueError:
        print("Ошибка: оценка должна быть целым числом")
        return
    
    # Ввод и проверка даты
    date_read = input("Введите дату прочтения (ГГГГ-ММ-ДД): ").strip()
    try:
        datetime.strptime(date_read, "%Y-%m-%d")
    except ValueError:
        print("Ошибка: неверный формат даты. Используйте ГГГГ-ММ-ДД")
        return
    
    # Создание и добавление книги
    try:
        book = Book(author, title, rating, date_read)
        if storage.add_book(book):
            print(f"Книга '{title}' успешно добавлена!")
        else:
            print(f"Книга '{title}' автора {author} уже существует в библиотеке")
    except ValueError as e:
        print(f"Ошибка: {e}")


def show_all_books(storage: BookStorage):
    """Показывает все книги"""
    books = storage.get_all_books()
    
    if not books:
        print("\nБиблиотека пуста. Добавьте первую книгу!")
        return
    
    print("\n--- Все книги ---")
    print(f"Всего книг: {len(books)}\n")
    
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")


def show_average_rating(storage: BookStorage):
    """Показывает среднюю оценку всех книг"""
    books = storage.get_all_books()
    avg_rating = calculate_average_rating(books)
    
    if avg_rating == 0:
        print("\nНет книг для расчёта средней оценки")
    else:
        print(f"\nСредняя оценка всех книг: {avg_rating}")


def show_author_statistics(storage: BookStorage):
    """Показывает статистику по авторам"""
    books = storage.get_all_books()
    stats = get_statistics_by_author(books)
    
    if not stats:
        print("\n📊 Нет книг для статистики по авторам")
        return
    
    print("\n--- Статистика по авторам ---")
    for author, data in sorted(stats.items()):
        print(f"\n{author}:")
        print(f"   Книг: {data['count']}")
        print(f"   Средняя оценка: {data['average_rating']}")


def delete_book(storage: BookStorage):
    """Удаляет книгу по номеру"""
    books = storage.get_all_books()
    
    if not books:
        print("\nНет книг для удаления")
        return
    
    print("\n--- Удаление книги ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
    
    try:
        choice = int(input("\nВведите номер книги для удаления (0 - отмена): ").strip())
        
        if choice == 0:
            print("Операция отменена")
            return
        
        if 1 <= choice <= len(books):
            deleted_book = books[choice - 1]
            confirm = input(f"Удалить книгу '{deleted_book.title}'? (да/нет): ").strip().lower()
            
            if confirm in ['да', 'yes', 'y', 'д']:
                if storage.delete_book(choice - 1):
                    print(f"Книга '{deleted_book.title}' успешно удалена!")
                else:
                    print("Ошибка при удалении книги")
            else:
                print("Операция отменена")
        else:
            print("Неверный номер книги")
    except ValueError:
        print("Ошибка: введите число")


def main():
    """Главная функция приложения"""
    storage = BookStorage()
    
    print("Добро пожаловать в Трекер прочитанных книг!")
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == '1':
            add_book(storage)
        elif choice == '2':
            show_all_books(storage)
        elif choice == '3':
            show_average_rating(storage)
        elif choice == '4':
            show_author_statistics(storage)
        elif choice == '5':
            delete_book(storage)
        elif choice == '6':
            print("\nДо свидания! Хорошего чтения!")
            sys.exit(0)
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 6.")


if __name__ == "__main__":
    main()