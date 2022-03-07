travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(new_country, number_visits, new_cities):
    new_visit = {"country": new_country, "visits": number_visits, "cities": new_cities}
    travel_log.append(new_visit)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
