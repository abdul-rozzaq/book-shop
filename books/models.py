from django.db import models
from accounts.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_time = models.DateField()
    isbn = models.CharField(max_length=20)
    genre = models.ManyToManyField('Genre')
    image = models.ImageField(upload_to='book_image/')
    price = models.FloatField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_rating(self):
        ratings = [x.rating for x in self.reviews.all()]

        if len(ratings) != 0:
            return round(sum(ratings) / len(ratings), 1)
        else:
            return 0

    def rating(self):
        yellows = ['<div class="rate fill">&#9733;</div>' for x in range(int(self.get_rating()))]
        greys = ['<div class="rate">&#9734;</div>' for x in range(5 - int(self.get_rating()))]
        return ''.join(yellows) + ''.join(greys)

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()


    def __str__(self):
        return f"{self.user.username}'s review for {self.book.title}"
    

class Discount(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='discount')
    new_price = models.FloatField()

    def __str__(self):
        return self.book.title


class Badge(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='badge')
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.book.title
    
    