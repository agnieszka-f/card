
from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")
    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone, email, position, company_name, work_phone):
        super().__init__(name, surname, phone, email)
        self.position = position
        self.company_name = company_name
        self.work_phone = work_phone
    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}")
    @property
    def label_length(self):
        return super().label_length

def create_contacts(card_type, qty):
    cards = []
    for _ in range(qty):
        if card_type == "base":
            card = BaseContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), email=fake.email())
            cards.append(card)
        elif card_type == "business":
            card = BusinessContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.basic_phone_number(), email=fake.email(), position=fake.job(), company_name=fake.company(), work_phone=fake.phone_number())
            cards.append(card)
        else:
            raise ValueError("cardType must be 'base' or 'business'")
    return cards

def show_contact(cards):
    for card in cards:
        card.contact()   

def main():
    cards_base = create_contacts("base", 5)
    cards_business = create_contacts("business", 5)
    print("Cards base:")
    show_contact(cards_base)
    print("Cards business:")
    show_contact(cards_business)

if __name__ == "__main__":
    main()


