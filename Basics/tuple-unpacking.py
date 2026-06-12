albums = [
    ("robinhood", "england", 1990),
    ("titanic", "england", 1992),
     ("Aba", "sri lanka", 2006),
      ("Ra-One", "india", 2010),
       ("Parker", "USA", 2013),
        ("Shelter", "USA", 2026)
]
print(len(albums))

for album in albums:
    film, country, year = album
    print("film: {}, country: {} and the year: {}".format(film,country,year))
print()
for film,country,year in albums:
    print("film: {}, country: {} and the year: {}".format(film,country,year))
