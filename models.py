from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    """Класс для представления книги"""
    author: str
    title: str
    rating: int  # 1-5
    date_read: str  # формат: YYYY-MM-DD
    
    def __post_init__(self):
        """Валидация данных"""
        if not self.author or not isinstance(self.author, str):
            raise ValueError("Автор должен быть непустой строкой")
        
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Название должно быть непустой строкой")
        
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        
        # Проверка формата даты
        try:
            datetime.strptime(self.date_read, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
    
    def to_dict(self) -> dict:
        """Преобразование в словарь для JSON"""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Создание книги из словаря"""
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )
    
    def __str__(self) -> str:
        """Строковое представление для вывода"""
        return f"'{self.title}' - {self.author} | Оценка: {self.rating} | Прочитана: {self.date_read}"
