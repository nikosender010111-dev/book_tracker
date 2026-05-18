from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Book:
    """Класс для представления книги"""
    author: str
    title: str
    rating: int  # от 1 до 5
    date_read: str  # формат: ГГГГ-ММ-ДД
    
    def __post_init__(self):
        """Валидация данных при создании"""
        if not self.author or not self.author.strip():
            raise ValueError("Автор не может быть пустым")
        
        if not self.title or not self.title.strip():
            raise ValueError("Название не может быть пустым")
        
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")

        try:
            datetime.strptime(self.date_read, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
    
    def to_dict(self) -> Dict:
        """Преобразует книгу в словарь для JSON"""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Создаёт книгу из словаря"""
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )
    
    def __str__(self) -> str:
        """Строковое представление книги"""
        return f"'{self.title}' - {self.author} (Оценка: {self.rating}, Прочитана: {self.date_read})"
