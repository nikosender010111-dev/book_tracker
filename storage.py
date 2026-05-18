import json
import os
from typing import List, Optional
from models import Book


class BookStorage:
    """Класс для управления хранением книг"""
    
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Создаёт файл, если его нет"""
        if not os.path.exists(self.filename):
            self._save_books([])
    
    def _load_books(self) -> List[dict]:
        """Загружает все книги из JSON"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_books(self, books: List[dict]):
        """Сохраняет книги в JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self) -> List[Book]:
        """Возвращает список всех книг"""
        books_data = self._load_books()
        return [Book.from_dict(book) for book in books_data]
    
    def add_book(self, book: Book) -> bool:
        """Добавляет новую книгу"""
        books = self._load_books()
        books.append(book.to_dict())
        self._save_books(books)
        return True
    
    def delete_book(self, index: int) -> bool:
        """Удаляет книгу по индексу (начиная с 0)"""
        books = self._load_books()
        if 0 <= index < len(books):
            deleted = books.pop(index)
            self._save_books(books)
            return True
        return False
    
    def find_books_by_author(self, author: str) -> List[Book]:
        """Ищет книги по автору (частичное совпадение)"""
        all_books = self.get_all_books()
        return [book for book in all_books if author.lower() in book.author.lower()]
    
    def get_books_count(self) -> int:
        """Возвращает количество книг"""
        return len(self._load_books())
