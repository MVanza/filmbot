import requests
from bs4 import BeautifulSoup
import yandex_search
import googlesearch


class MyError(Exception):
    pass


class AnimeRate:

    def __init__(self, anime_name):
        self.anime_name = anime_name

    def get_anime_id(self, anime_name):
        f = googlesearch.search(f'yummyanime.club {anime_name}', tld='ru', lang='ru', num=1, start=0, stop=2)
        g = ''
        for i in f:
            g = i
            break
        lurl = g.split('/')
        if lurl[2] != 'yummyanime.club' and lurl[3] != 'catalog':
            raise MyError("")
        fid = lurl[-1]
        return fid

    def get_anime_rate(self):
        try:
            anime_id = self.get_anime_id(self.anime_name)
        except:
             raise MyError("")
        url = f'https://yummyanime.club/catalog/item/{anime_id}'
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text)
        f = soup.find('span', {'class': 'main-rating'})
        return f.text, anime_id


class FilmRate:

    def __init__(self, film_name):
        self.film_name = film_name

   # def get_film_id(self, film_name):
   #     yandex = yandex_search.Yandex(api_user='kazuskoma', api_key='03.606752745:7ea3e0c9e28c34883b65704625d931d1')
   #     f = yandex.search(f'kinopoisk {film_name.lower()}').items
   #     url = f[0].get('url')
   #     lurl = url.split('/')
   #     if lurl[2] != 'www.kinopoisk.ru':
   #         raise MyError("")
   #     else:
   #         fid = lurl[-2]
   #         return fid

    def get_film_id(self, film_name):
        f = googlesearch.search(f'кинопоиск {film_name}', tld='ru', lang='ru', num=2, start=0, stop=2)
        g = ''
        for i in f:
            g = i
            break
        lurl = g.split('/')
        if lurl[2] != 'www.kinopoisk.ru':
            raise MyError("")
        else:
            fid = lurl[-2]
        return fid
    def gfr_KpIm(self):
        try:
            film_id = self.get_film_id(self.film_name)
        except:
             raise MyError("")
        url = f'https://rating.kinopoisk.ru/{film_id}.xml'
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text)
        lst = []
        lst.append(soup.find('kp_rating').text)
        lst.append(soup.find('imdb_rating').text)
        lst.append(film_id)
        return lst

    #def gfr_MC(self):
    #    lmcname = self.film_name.split()
    #    mcname = "-".join(lmcname)
    #    url = f'https://www.metacritic.com/movie/{mcname}/user-reviews'
    #    headers = {
    #        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'
    #    }
    #    r = requests.get(url, headers=headers)
    #    soup = BeautifulSoup(r.text)
    #    f = soup.find('td', {'class': 'num_wrapper'})
    #    return f.find_all('span')[0].text

    #def gfr_RT(self):
    #    lrtname = self.film_name.split()
    #    rtname = "_".join(lrtname)
    #    url = f'https://www.rottentomatoes.com/m/{rtname}'
    #    headers = {
    #        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'
    #    }
    #    r = requests.get(url, headers=headers)
    #    soup = BeautifulSoup(r.text)
    #    f = soup.find('div', {'class': 'mop-ratings-wrap__half audience-score'})
    #    return f.find('span', {'class': 'mop-ratings-wrap__percentage'}).text.split()[0]



