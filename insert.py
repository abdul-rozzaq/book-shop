import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

# =================================================================



from books.models import *

# from faker import Faker
import random

# def insert(model, data: list[dict]):
#     for i in data:
#         model.objects.create(**i)
        
        
"""
fake = Faker()


books = []


for _ in range(25):
    book = {
        'title': fake.text(max_nb_chars=100),
        'author_id': random.randint(1, 26),
        'published_time': fake.date_this_decade(),
        'isbn': fake.isbn13(),
        # 'genre': set([random.randint(1, 33) for _ in range(3)]),
        'image': fake.image_url(),
        'price': fake.random_digit(),
    }
    books.append(book)

insert(Book, books)


for book in Book.objects.all():
    # book.genre.add(*[random.randint(1, 33) for _ in range(3)])
    
    book.image = 'book_image/def.jpg'
    
    book.save()


"""

from PIL import Image

def get_files_in_directory(directory_path):
    file_list = []

    if os.path.exists(directory_path):
        file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    return file_list

directory_path = './media/book_image/'
new_directory_path = './media/new_book_image/'
files = get_files_in_directory(directory_path)



for x in files:
    
    image = Image.open(directory_path + x)

    new_image = image.resize([int(x * .5) for x in image.size])

    new_image.save(new_directory_path + x)


"""
for book in Book.objects.all():
    book.title = fake.first_name()
    book.image = '/book_image/' + random.choice(files)
    book.save()
    
user_ids = [x.pk for x in User.objects.all().order_by('?')]

for book in Author.objects.all():
    # etx = fake.text(max_nb_chars=1000)
    
    book.bio = book.bio[0: int(len(book.bio) / 2)]
    
    book.save()
    
    
    # for _ in range(50):
    #     data = {
    #         'user_id': random.choice(user_ids),
    #         'book': book,
    #         'rating': random.randint(1, 5),
    #         'text': fake.text(max_nb_chars=50),
    #     }
        
    #     Review.objects.create(**data)
"""