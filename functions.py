from datetime import datetime

import curse

def countries() -> list[str] | str:
    url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2"
    soup = curse.check_response(url)
    f = soup.find("tbody").find_all("a")
    if f:
        data = [td.text for td in f if len(td.text) > 0]
        return data
    return "Что-то пошло не так"

def langs() -> list[str] | str:
    url = "https://habr.com/ru/articles/179987/"
    soup = curse.check_response(url)
    f = soup.find("ol")
    if f:
        tbody = f.find_all("a")
        languages = [td.text for td in tbody if len(td.text) > 0]
        return languages
    return "Что-то пошло не так"

def cities() -> list[str] | str:
    url = "https://www.xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php"
    soup = curse.check_response(url)
    f = soup.find_all("ul")[1]
    if f:
        data2 = [a.text for a in f.find_all("a")]
        return data2
    return "Что-то пошло не так"

def names() -> list[str] | str:
    url = "https://namedb.ru/search-by-letter"
    soup = curse.check_response(url)
    if soup:
        pwd = [b.text[1:-1] for b in soup.find_all("li", class_="search-list")]
        return pwd
    return "Что-то пошло не так"

def curses() -> dict[datetime: list[str]]:
    data = {
        "date": datetime.now().date(),
        "rate": [
            curse.kurs("https://www.banki.ru/products/currency/usd/"), 
            curse.kurs("https://finance.rambler.ru/currencies/"), 
            curse.kurs("https://www.kursvaliut.ru/")
        ]
    }
    return data


if __name__ == "__main__":
    print(countries())
    print(langs())
    print(cities())
    print(names())
    print(curses())
