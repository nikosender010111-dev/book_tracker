from typing import List, Dict
from models import Book


def calculate_average_rating(books: List[Book]) -> float:
    """
    Рассчитывает среднюю оценку всех книг
    
    Args:
        books: Список книг
    
    Returns:
        Средняя оценка (0.0 если список пуст)
    """
    if not books:
        return 0.0
    
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)


def get_statistics_by_author(books: List[Book]) -> Dict[str, Dict]:
    """
    Получает статистику по авторам
    
    Args:
        books: Список книг
    
    Returns:
        Словарь {автор: {"count": число_книг, "average_rating": средняя_оценка}}
    """
    if not books:
        return {}
    
    author_data = {}
    
    for book in books:
        if book.author not in author_data:
            author_data[book.author] = {"total_rating": 0, "count": 0}
        
        author_data[book.author]["total_rating"] += book.rating
        author_data[book.author]["count"] += 1
    
    # Рассчитываем среднюю оценку для каждого автора
    result = {}
    for author, data in author_data.items():
        result[author] = {
            "count": data["count"],
            "average_rating": round(data["total_rating"] / data["count"], 2)
        }