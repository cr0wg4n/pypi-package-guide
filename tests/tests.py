from pypi_package_template import Phraser
import unittest 

class Test(unittest.TestCase):
    def test_charge_data(self):
        phraser = Phraser()
        expected_lines = 200
        real_size = len(phraser.charge_data())
        self.assertGreater(real_size, expected_lines)

    def test_firts_phrase(self):
        expected_phrase = "Cada persona forja su propia grandeza. Los enanos permanecerán enanos aunque se suban a los Alpes. (August von Kotzebue)"
        phraser = Phraser()
        phrases = phraser.get_all_phrases()
        self.assertEqual(phrases[0], expected_phrase)

    def test_get_random_phrase(self):
        phraser = Phraser()
        phrase = phraser.get_random_phrase()
        print('\n', phrase, '\n')
        self.assertGreater(len(phrase), 0)        

if __name__ == "__main__":
    unittest.main()