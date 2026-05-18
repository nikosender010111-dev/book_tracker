from typing import List, Dict, Tuple
from models import Book
from collections import defaultdict


def calculate_average_rating(books: List[Book]) -> float:
    """Рассчитывает среднюю оценку всех книг"""
    if not books:
        return 0.0
    total_rating = sum(book.rating for book in books)
    return round(total_rating / len(books), 2)


def get_statistics_by_author(books: List[Book]) -> Dict[str, Dict]:
    """
    Возвращает статистику по авторам:
    - количество книг
    - средняя оценка
    """
    if not books:
        return {}
    
    author_stats = defaultdict(lambda: {"count": 0, "total_rating": 0})
    
    for book in books:
        author_stats[book.author]["count"] += 1
        author_stats[book.author]["total_rating"] += book.rating
    
    # Рассчитываем среднюю оценку для каждого автора
    result = {}
    for author, stats in author_stats.items():
        result[author] = {
            "count": stats["count"],
            "average_rating": round(stats["total_rating"] / stats["count"], 2)
        }
    
    return result


def get_books_by_rating(books: List[Book], min_rating: int = 4) -> List[Book]:
    """Возвращает книги с оценкой выше указанной"""
    return [book for book in books if book.rating >= min_rating]


def get_reading_statistics(books: List[Book]) -> Dict:
    """Расширенная статистика чтения"""
    if not books:
        return {
            "total_books": 0,
            "unique_authors": 0,
            "average_rating": 0,
            "max_rating": 0,
            "min_rating": 0
        }
    
    ratings = [book.rating for book in books]
    authors = set(book.author for book in books)
    
    return {
        "total_books": len(books),
        "unique_authors": len(authors),
        "average_rating": calculate_average_rating(books),
        "max_rating": max(ratings),
        "min_rating": min(ratings)
    }
