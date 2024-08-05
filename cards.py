
from faker import Faker

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

        self.names_length = len(self.name) + len(self.surname) + 1
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")
    @property
    def sum_names(self):
        return self.names_length

class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone, email, position, company_name, work_phone):
        super().__init__(name, surname, phone, email)
        self.position = position
        self.company_name = company_name
        self.work_phone = work_phone
    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}")

def create_contacts(cardType, qty):
    cards = []
    for _ in range(qty):
        if cardType == "base":
            card = BaseContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), email=fake.email())
            cards.append(card)
        elif cardType == "business":
            card = BusinessContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.basic_phone_number(), email=fake.email(), position=fake.job(), company_name=fake.company(), work_phone=fake.phone_number())
            cards.append(card)
        else:
            raise ValueError("cardType must be 'base' or 'business'")
    return cards


fake = Faker()

cards_base = create_contacts("base", 5)
cards_business = create_contacts("business", 5)

for card in cards_base:
    card.contact()
    
for card in cards_business:
    card.contact()