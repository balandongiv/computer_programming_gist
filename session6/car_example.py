class Phone:
    def __init__(self, color, weight, brand, price):
        self.color = color
        self.weight = weight
        self.brand = brand
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from my {self.brand} phone!")

    def take_photo(self):
        print(f"Taking a photo with my {self.brand} phone!")

# Create a phone object
my_phone = Phone("Black", 150, "Samsung", 999)

# Use data attributes
print(my_phone.color)   # Black
print(my_phone.weight)  # 150

# Use procedures (methods)
my_phone.make_call("123-4567")  # Calling 123-4567 from my Samsung phone!
my_phone.take_photo()           # Taking a photo with my Samsung phone!
