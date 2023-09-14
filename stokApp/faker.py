import random
from faker import Faker
from django.contrib.auth.models import User
from .models import Firm, Category, Brand, Product, Sales, Purchases

fake = Faker(['tr-TR'])

def ie():
    
    

    # Kategori oluşturma
    categories = ["BOT", "MONT", "KEMER", "AYAKKABI"]
    for category_name in categories:
        Category.objects.create(name=category_name)

    # Marka oluşturma
    brands = ["CAT", "LCW", "COTON", "NIKE"]
    for brand_name in brands:
        Brand.objects.create(name=brand_name)

    # Firma oluşturma
    for _ in range(10):
        Firm.objects.create(
            name=fake.company(),
            phone=fake.phone_number(),
            address=fake.address(),
            # image = fake.image(),
        )

    # Ürün oluşturma
    for _ in range(20):
        category = random.choice(Category.objects.all())
        brand = random.choice(Brand.objects.all())
        Product.objects.create(
            name=fake.word(),
            category=category,
            brand=brand,
            stock=random.randint(0, 100),
        )

    # Kullanıcı oluşturma
    for _ in range(5):
        User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
        )

    # Satış oluşturma
    users = User.objects.all()
    products = Product.objects.all()
    for _ in range(30):
        user = random.choice(users)
        product = random.choice(products)
        quantity = random.randint(1, 100)
        price = random.uniform(1, 1000.0)
        Sales.objects.create(
            user=user,
            product=product,
            brand=product.brand,
            quantitiy=quantity,
            price=price,
            price_total=quantity * price,
        )

    # Alışveriş oluşturma
    users = User.objects.all()
    firms = Firm.objects.all()
    products = Product.objects.all()
    for _ in range(30):
        user = random.choice(users)
        firm = random.choice(firms)
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = random.uniform(5.0, 50.0)
        Purchases.objects.create(
            user=user,
            firm=firm,
            brand=product.brand,
            product=product,
            quantitiy=quantity,
            price=price,
            price_total=quantity * price,
        )

if __name__ == '__main__':
    ie()



# from .models import Category ,Product
# from faker import Faker

# def run():
#     '''
#         # https://faker.readthedocs.io/en/master/
#         $ pip install faker # install faker module
#         python manage.py flush # delete all exists data from db. dont forget: createsuperuser
#         python manage.py shell
#         from student_api.faker import run
#         run()
#         exit()
#     '''

#     fake = Faker(['tr-TR'])
#     categori= (
#         "BOT",
#         "MONT",
#         "TEKERLEK",
#         "KEMER",
#         "ŞAPKA"
#     )

#     for cate in categori:
#         new_cate = Category.objects.create(name = cate)
#         for _ in range(5):
#             Product.objects.create(category = new_cate, name = fake.name())
    
#     print('Finished')