import requests
from bs4 import BeautifulSoup

def clear(soup: str) -> float | str:
    bad_symbols = ["\xa0", "₽", "&nbsp;", "\t", "\n", "\r", "$"]
    for bad in bad_symbols:
        if bad in soup:
            soup = soup.replace(bad, "").replace(",", ".")
    try:
        return float(soup.strip())
    except ValueError:
        return "Что-то не так с курсом!"


def check_response(url: str) -> BeautifulSoup | str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException:
        return "Что-то не так с сайтом!"

def kurs(url: str) -> float | str:
    sites_config = [
    {
        "url": "https://www.banki.ru/products/currency/usd/",
        "tag": "div",
        "class": "Text__sc-vycpdy-0 cQqMIr",
    },
    {
        "url": "https://finance.rambler.ru/currencies/",
        "tag": "span",
        "class": "dsS9XXNx",
    },
    {
        "url": "https://www.kursvaliut.ru/",
        "tag": "td",
        "class": "text-right last-exchange-rate",
    }
    ]
    for site in sites_config:
        if site["url"] == url:
            soup = check_response(url)
            tag = site["tag"]
            cls = site["class"]
            elem = soup.find(tag, class_=cls)
            if elem:
                return clear(elem.text)
            return "Элемента нету на странице"
    return "Сайт не поддерживается"


if __name__ == "__main__":
    print(kurs("https://finance.rambler.ru/currencies/"))
    print(kurs("https://www.banki.ru/products/currency/usd/"))
    print(kurs("https://www.kursvaliut.ru/"))
