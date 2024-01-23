from src.dni_cif import Dni
import random
import string


def test_random_cases_dni():
    NUMBER_OF_CASES = 25

    testCases = []

    for _ in range(NUMBER_OF_CASES + 1):
        testCases.append(
            f"{random.randint(0, 99999999):08}{random.choice(string.ascii_uppercase)}"
        )

    for testString in testCases:
        dni = Dni(testString)
        if dni.checkCIF():
            assert dni.getNumeroSano()
            assert dni.getLetraSana()
        else:
            assert not (dni.getNumeroSano() and dni.getLetraSana())
