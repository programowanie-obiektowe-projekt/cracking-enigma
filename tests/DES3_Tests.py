import unittest
from unittest import TestCase
from Crypto.Random import get_random_bytes

from algorithms.DES3 import DES3Adapter

class TestDES3Class(TestCase):

    def setUp(self):
        self.algorithm = DES3Adapter()

    def test_encrypt_des(self):
        text = b'hello'
        encrypted_text = self.algorithm.encrypt(text)
        self.assertIsNotNone(encrypted_text[0])

    def test_decrypt_des(self):
        text = b'hello'
        encrypted_text = self.algorithm.encrypt(text)
        decrypted_text = self.algorithm.decrypt(encrypted_text[0], encrypted_text[1])
        self.assertEqual(decrypted_text.encode('utf-8'), text)

    def test_brute_force_des(self):
        text = b'hello'
        encrypted_text = self.algorithm.encrypt(text)
        result = self.algorithm.brute_force(encrypted_text[0], text)
        self.assertIsNotNone(result)
        self.assertIn('msg', result)
        self.assertIn('status', result)

    def test_frequency_analysis_des(self):
        text = b'hello'
        encrypted_text = self.algorithm.encrypt(text)
        result = self.algorithm.frequency_analysis(encrypted_text[0])
        self.assertIsNotNone(result)
        self.assertIn('msg', result)
        self.assertIn('status', result)

if __name__ == '__main__':
    unittest.main()