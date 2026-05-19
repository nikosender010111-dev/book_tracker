import json
import os
from typing import List, Optional
from models import Book


class BookStorage:
    """Класс для управления хранением книг в JSON файле"""
    
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Создаёт файл с пустым списком, если он не существует"""
        if not os.path.exists(self.filename):
            self._save_books([])
    
    def _load_books(self) -> List[dict]:
        """Загружает список книг из JSON файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_books(self, books: List[dict]):
        """Сохраняет список книг в JSON файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self) -> List[Book]:
        """Возвращает список всех книг в виде объектов Book"""
        books_data = self._load_books()
        return [Book.from_dict(book) for book in books_data]
    
    def add_book(self, book: Book) -> bool:
        """
        Добавляет новую книгу
        
        Args:
            book: Объект Book для добавления
        
        Returns:
            True если добавление успешно, False если книга уже существует
        """

        existing_books = self.get_all_books()
        for existing in existing_books:
            if (existing.author.lower() == book.author.lower() and 
                existing.title.lower() == book.title.lower()):
                return False  # Книга уже существует
        
        books = self._load_books()
        books.append(book.to_dict())
        self._save_books(books)
        return True
    
    def delete_book(self, index: int) -> bool:
        """
        Удаляет книгу по индексу
        
        Args:
            index: Индекс книги в списке (начиная с 0)
        
        Returns:
            True если удаление успешно, False если индекс недействителен
        """
        books = self._load_books()
        if 0 <= index < len(books):
            books.pop(index)
            self._save_books(books)
            return True
        return False
    
    def get_books_count(self) -> int:
        """Возвращает количество книг в хранилище"""
        return len(self._load_books())
    
    def find_books_by_author(self, author: str) -> List[Book]:
        """Ищет книги по автору (частичное совпадение, без учёта регистра)"""
        all_books = self.get_all_books()
        return [book for book in all_books if author.lower() in book.author.lower()]