import unittest
from str import pr_str, ch_case, uppercase_let
from gen import even_odd_gen

# Тест pr_str, ch_case та uppercase_let
class TestStr(unittest.TestCase):
    def test_pr_str(self):
        self.assertEqual(pr_str("Sergo"), "Sergo")
        self.assertEqual(pr_str(428), "Очікується string")

    def test_ch_case(self):
        self.assertEqual(ch_case("YOTSUBA"), "Великі")
        self.assertEqual(ch_case("yotsuba"), "Малі")
        self.assertEqual(ch_case("YotSuba"), "Змішані")
        self.assertEqual(ch_case(428), "Очікується string")

    def test_uppercase_let(self):
        self.assertEqual(uppercase_let("smogtether"), ["S", "M", "O", "G", "T", "E", "T", "H", "E", "R"])
        self.assertEqual(uppercase_let(428), "Очікується string")

# Тест even_odd_gen
class TestGen(unittest.TestCase):
    def test_even_odd_gen(self):
        gen = even_odd_gen()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")

if __name__ == '__main__':
    unittest.main()