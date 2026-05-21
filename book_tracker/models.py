from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Book:
    author: str
    title: str
    rating: int
    date_read: str
    
    def __post_init__(self):
        if not self.author or not self.author.strip():
            raise ValueError("Avtor ne mozhet byt pustym")
        
        if not self.title or not self.title.strip():
            raise ValueError("Nazvanie ne mozhet byt pustym")
        
        if not 1 <= self.rating <= 5:
            raise ValueError("Ocenka dolzhna byt ot 1 do 5")
        
        try:
            datetime.strptime(self.date_read, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data dolzhna byt v formate GGGG-MM-DD")
    
    def to_dict(self) -> Dict:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )
    
    def __str__(self) -> str:
        return f"'{self.title}' - {self.author} (Оценка: {self.rating}, Прочитана: {self.date_read})"
