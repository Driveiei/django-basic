from django.test import TestCase
from application.models import Dog,Cat,Hotel

class DogTest(TestCase):
    def setUp(self):
        Dog.objects.create(dog_name="Hayato")
        Dog.objects.create(dog_name="Kawai")

    def test_create_dogs(self):
        #Number of objects
        self.assertEqual(2,Dog.objects.count())

    def test_name_dogs(self):
        self.assertTrue(Dog.objects.filter(dog_name="Hayato"))


class CatTest(TestCase):
    def setUp(self):
        Cat.objects.create(cat_name="Hayatos")
        Cat.objects.create(cat_name="Kawais")

    def test_models_dogs(self):
        self.assertEqual(2,Cat.objects.count())
        self.assertTrue(Cat.objects.filter(cat_name="Hayatos"))


class HotelTest(TestCase):
    def setUp(self):
        self.Japan = Dog.objects.create(dog_name="Hayato")
        self.New = Cat.objects.create(cat_name="Vichakorn")
        self.Tong = Cat.objects.create(cat_name="Thanaphon")
        self.New.save()
        self.Tong.save()
        Hotel.objects.create(
            hotel_name='James Brucker hotel',
            room_text='58', 
            room_number = 58,
            price = 60700,
            dog_relate_name=self.Japan,
            )

    def test_check_hotel(self):
        self.assertTrue(Hotel.objects.filter(hotel_name="James Brucker hotel"))
        self.assertTrue(Hotel.objects.filter(room_text='58'))
        self.assertTrue(Hotel.objects.filter(room_number=58))
        self.assertTrue(Hotel.objects.filter(price=60700))
        self.assertTrue(Hotel.objects.filter(dog_relate_name=self.Japan))

    def test_love_couple(self):
        hotel = Hotel.objects.all().first()
        hotel.cat_relate_name.add(self.New)
        hotel.cat_relate_name.add(self.Tong)
        self.assertEqual(list(hotel.cat_relate_name.all()),[self.New,self.Tong])
