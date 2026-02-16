from db import db_session

from functions import names, countries, cities, langs
from models import Country, Name, City, Language, CurrencyRate
from functions import curses


funcs = {
    countries: Country,
    names: Name,
    cities: City,
    langs: Language,
}


def save():  # check -> for -> check + db.query.filter_by.first() -> add
    for func in funcs:
        data = func()
        for item in data:
            if not db_session.query(funcs.get(func)).filter_by(name=item).first():
                db_session.add(funcs.get(func)(name=item))
            db_session.commit()

    data = curses()
    if data:
        for item in data["rate"]:
            db_session.add(CurrencyRate(date=data["date"], rate=item))
    db_session.commit()


if __name__ == "__main__": 
    save()
    print("Все изменения применены.")
