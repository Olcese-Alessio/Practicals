from Prac_06.guitar import Guitar


def run_tests():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar_1.name, 98,
                                                      guitar_1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar_2.name, 7,
                                                      guitar_2.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_1.name,
                                                         True,
                                                         guitar_1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_2.name,
                                                         False,
                                                         guitar_2.is_vintage()))


run_tests()
