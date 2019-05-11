import requests
from bs4 import BeautifulSoup
from cachetools import cached, TTLCache


TOP_GROSSING_URL = "https://www.boxofficemojo.com/alltime/world/"


def movie(name, grossing, year):
    grossing_num = float(grossing[1:].replace(",", ""))
    dollar_amount = f"${round(grossing_num * 1000000):,.0f}"
    return {
        "name": name.strip(),
        "grossing": dollar_amount,
        "year": year.replace("^", "").strip(),
    }


@cached(TTLCache(maxsize=2, ttl=900))
def get_top_grossing():
    resp = requests.get(TOP_GROSSING_URL).content
    soup = BeautifulSoup(resp, "html.parser")
    table = soup.find_all("table")[2]
    rows = table.find_all("tr")[1:8]
    movies = []
    for row in rows:
        cols = row.find_all("td")
        movies.append(movie(cols[1].text, cols[3].text, cols[8].text))

    return movies

