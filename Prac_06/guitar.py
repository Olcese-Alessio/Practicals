"""Create guitar class(name, year, cost)"""
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """ Store details of guitar"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string for guitar added"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate age of guitar based off of current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if guitar is vintage based on age"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitar by year"""
        return self.year < other.year
