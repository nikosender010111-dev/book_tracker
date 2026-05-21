import json
import os
from typing import List
from models import Book


class BookStorage:
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            self._save_books([])
    
    def _load_books(self) -> List[dict]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_books(self, books: List[dict]):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self) -> List[Book]:
        books_data = self._load_books()
        return [Book.from_dict(book) for book in books_data]
    
    def add_book(self, book: Book) -> bool:
        existing_books = self.get_all_books()
        for existing in existing_books:
            if (existing.author.lower() == book.author.lower() and 
                existing.title.lower() == book.title.lower()):
                return False
        
        books = self._load_books()
        books.append(book.to_dict())
        self._save_books(books)
        return True
    
    def delete_book(self, index: int) -> bool:
        books = self._load_books()
        if 0 <= index < len(books):
            books.pop(index)
            self._save_books(books)
            return True
        return False