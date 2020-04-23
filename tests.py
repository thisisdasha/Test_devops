import functions
import pytest


@pytest.mark.parametrize('tested_string',
                         ["Ivan Ivanov something 89112324509 12/11/1982",
                          "Petr Petrov 89112324509 89111012323 12/11/1982",
                          "Vanessa Voronchichina Perm  89112324509 12/11/1982",
                          "Katya Belyaeva Murmansk 89112324509 12/11/1982"])
def test_invalid_input(tested_string):
    arr = []  # an array in which directory lines are stored
    with open("file.txt") as file:
        arr = [row.strip() for row in file]
    assert functions.add(tested_string, arr) == "Invalid input"


@pytest.mark.parametrize('tested_string',
                         ["Ivan 12/12/1312 89112324509 12/11/1982",
                          "Petr **** 89111012323 12/11/1982",
                          "Katya (Belyaeva) 89112324509 12/11/1982"])
def test_invaild_surname(tested_string):
    arr = []
    with open("file.txt") as file:
        arr = [row.strip() for row in file]
    assert functions.add(tested_string, arr) == "Invalid surname"


@pytest.mark.parametrize('tested_string',
                         ["Ivan Ivanov 8911232459 12/11/1982",
                          "Katya Belyaeva 8910012324509 12/11/1982",
                          "Anna Tokareva 89112324q09 12/11/1982"])
def test_invalid_phone_num(tested_string):
    arr = []
    with open("file.txt") as file:
        arr = [row.strip() for row in file]
    assert functions.add(tested_string, arr) in \
           ["Invalid phone number",
            "Invalid character in phone number"]
