from bs4 import BeautifulSoup
import requests
from .models import Movie

def storeMovies():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find('tbody', class_='lister-list')
    movies = soup.find_all('tr')
    # print(movies[0])
    # movie = movies[0]
    # img = (movie.find('td', class_='posterColumn')).img['src']
    # img = img.split('@')
    # img = img[0]+'@.jpg'
    # print(img)
    
    # title = movie.find('td', class_='titleColumn').a

    # print(title.string)
    # rating = movie.find('td', class_='imdbRating').strong
    # print(rating.string)
    db_movies = []
    for movie in movies:
        img = (movie.find('td', class_='posterColumn')).img['src']
        img = img.split('@')
        img = img[0]+'@.jpg'
        title = (movie.find('td', class_='titleColumn').a).string
        rating = (movie.find('td', class_='imdbRating').strong).string
        mv = Movie(name=title, rating=rating, image_url=img)
        db_movies.append(mv)

    print(len(db_movies))
    # print(db_movies)
    Movie.objects.bulk_create(db_movies)
# storeMovies()