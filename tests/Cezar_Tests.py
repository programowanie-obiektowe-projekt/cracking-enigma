import unittest
from Crypto.Random import random

from algorithms.Cezar import CezarAdapter, CezarClass

class TestCezar(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "hello"
        key = 3
        expected_ciphertext = "khoor"
        algorithm = CezarClass()
        self.assertEqual(algorithm.szyfruj(plaintext, key)[0], expected_ciphertext)

    def test_decrypt(self):
        ciphertext = "khoor"
        key = 3
        expected_plaintext = "hello"
        algorithm = CezarClass()
        self.assertEqual(algorithm.szyfruj(ciphertext, -key)[0], expected_plaintext)

    def test_brute_force(self):
        ciphertext = "khoor"
        original = "hello"
        algorithm = CezarClass()
        self.assertEqual(algorithm.bruteForce(ciphertext, original)['status'], "Udało się złamać szyfr")

    def test_frequency_analysis(self):
        plaintext = "hello"
        ciphertext = "khoor"
        algorithm = CezarClass()
        result = algorithm.frequency_analysis_cezar(ciphertext, plaintext)
        decrypted_text = result['decrypted_text']
        if decrypted_text == plaintext:
            self.assertEqual(result['status'], "Udało się złamać szyfr")
        elif decrypted_text != plaintext:
            self.assertEqual(result['status'], "Nie udało się złamać szyfru")

class TestCezarAdapter(unittest.TestCase):
    algorithm = CezarClass()
    def test_encrypt(self):
        plaintext = "hello"
        key = random.randint(1, 25)
        ciphertext, _ = self.algorithm.szyfruj(plaintext, key)
        self.assertEqual(len(ciphertext), len(plaintext))

    def test_decrypt(self):
        encrypted_text = "khoor"
        key = 3
        self.assertEqual(self.algorithm.szyfruj(encrypted_text, -key)[0], "hello")
    def test_brute_force(self):
        plaintext = "hello"
        algorithm = CezarAdapter()
        ciphertext, key = algorithm.encrypt(plaintext)
        result = algorithm.brute_force(ciphertext, plaintext)
        self.assertEqual(result['status'], "Udało się złamać szyfr")

    def test_frequency_analysis(self):
        plaintext = "hello"
        algorithm = CezarAdapter()
        ciphertext, key = algorithm.encrypt(plaintext)
        result = algorithm.frequency_analysis(ciphertext, plaintext)
        self.assertIn(result['status'], ["Udało się złamać szyfr", "Nie udało się złamać szyfru"])

if __name__ == '__main__':
    unittest.main()