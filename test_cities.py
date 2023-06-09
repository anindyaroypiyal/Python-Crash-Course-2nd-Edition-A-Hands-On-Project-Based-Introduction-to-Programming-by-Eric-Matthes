import unittest
from city_functions import form_city_country

class CityCountyTest(unittest.TestCase):
    """ test for 'city_functions.py' """
    def test_city_country(self):
        ct_cnt = form_city_country(city = 'Santiago', country = 'chile')
        self.assertEqual(ct_cnt,'Santiago, Chile.')

    def test_city_country_population(self):
        ct_cnt = form_city_country(city = 'Santiago', country = 'chile', population = 50000)
        self.assertEqual(ct_cnt,'Santiago, Chile - Population 50000')

if __name__ == '__main__':
    unittest.main()
