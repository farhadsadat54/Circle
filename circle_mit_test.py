#!/usr/bin/python3
# -------------------
#
# -------------------
import unittest
from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("Der Radius ist leider negativ")
    if type(r) not in [int, float]:
        raise TypeError("Nur Zahleneigabe  erlaubt")

    flaeche = pi * (r ** 2)
    return flaeche


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(0), 0)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -9)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, True)


r = float(input("Eingabe Radius= "))
#a = circle_area(r)
#print(a)
print("Flächeninhalt= ", circle_area(r))

if __name__ == '__main__':
    unittest.main(verbosity=2)