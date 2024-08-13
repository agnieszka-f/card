import random
from faker import Faker
import datetime

fake = Faker()

genres = ['przygodowy', 'dramat', 'horror', 'komedia', 'thriller', 'sci-fi', 'fantasy', 'akcja', 'romans']

class Movie():
    def __init__(self, title, publication_date, type):
        self.title = title
        self.publication_date = publication_date
        self.type = type

        self.number_of_plays = 0

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        return f"{self.title} ({self.publication_date.split('-')[0]})"

class Serial(Movie):
    def __init__(self, title, publication_date, type, episode_number, season_number):
        super().__init__(title, publication_date, type)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"
    
def get_sorted_list(list):
    return sorted(list, key=lambda item: item.title)

def get_media(list, media_type):
    return get_sorted_list([ item for item in list if type(item) is media_type])

def get_movies(list):
    return get_media(list, Movie)

def get_series(list):
    return get_media(list, Serial)

def search(title, list):
    return [item for item in list if item.title.lower() == title.lower()]

def generate_views(list):
    generated_item = random.choice(list)
    generated_number_of_plays = random.choice(range(1, 101))
    generated_item.number_of_plays += generated_number_of_plays

def run_generate_views(list):
    for _ in range(10):
        generate_views(list)

def top_titles(list, qty):
    return sorted([ item for item in list], key=lambda item: item.number_of_plays, reverse=True)[:qty]

def show_media(media_list):
    for media in media_list:
        print(media)

def create_movies(qty):
    movies = []
    for _ in range(qty):
        movies.append(Movie(title=fake.sentence(nb_words=3).rstrip('.'),publication_date=fake.date_this_century().strftime('%Y-%m-%d'), type=random.choice(genres)))
    return movies

def create_series(qty):
    movies = []
    for _ in range(qty):
        movies.append(Serial(title=fake.sentence(nb_words=3).rstrip('.'), publication_date=fake.date_this_century().strftime('%Y-%m-%d'), type=random.choice(genres),episode_number=fake.random_int(min=1, max=99), season_number=fake.random_int(min=1, max=10)))
    return movies

def main():
    print("Biblioteka filmów")
    media_list  = create_movies(10) + create_series(10)
    run_generate_views(media_list)
    top_media = top_titles(media_list, 3)
    today = datetime.date.today()
    print(f"Najpopularniejsze filmy i seriale dnia {today.strftime('%d.%m.%Y')}")
    show_media(top_media)
    print("\nSorted movies:")
    movies = get_movies(media_list)
    show_media(movies)
    print("\nSorted series:")
    series = get_series(media_list)
    show_media(series)

if __name__ == "__main__":
    main()
