from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import itertools
import time

from algorithms.algorithm_interface import AlgorithmInterface


class AESAdapter(AlgorithmInterface):
    def __init__(self):
        self.algorithm = AESClass()

    def encrypt(self, text):
        return self.algorithm.szyfruj_aes(text)

    def decrypt(self, encrypted_text, key):
        return self.algorithm.odszyfruj_aes(encrypted_text, key)

    def brute_force(self, encrypted_text, original):
        return self.algorithm.bruteForce_aes(encrypted_text)

    def frequency_analysis(self, encrypted_text):
        return self.algorithm.frequency_analysis_aes(encrypted_text)



class AESClass:
    def szyfruj_aes(self, napis):
        klucz = get_random_bytes(16)

        cipher = AES.new(klucz, AES.MODE_ECB)
        padded_data = pad(napis, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        return encrypted_data, klucz

    def odszyfruj_aes(self, encrypted_data, klucz):
        cipher = AES.new(klucz, AES.MODE_ECB)
        padded_data = cipher.decrypt(encrypted_data)
        decrypted_data = unpad(padded_data, AES.block_size).decode()
        return decrypted_data

    def bruteForce_aes(self, encrypted_data):
        start_time = time.time()
        max_time = 5
        attempts = 0

        for i in itertools.product(range(ord('a'), ord('z') + 1), repeat=16):
            klucz = bytes(i)
            attempts += 1
            cipher = AES.new(klucz, AES.MODE_ECB)
            try:
                decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode()
                end_time = time.time()
                msg = "Klucz: " + str(klucz) + " Tekst: " + decrypted_data + " Złamano w " + str(
                    end_time - start_time) + " sekund"
                return msg, klucz, decrypted_data
            except ValueError:
                pass

            msg = f"Nie udało się złamać po: {attempts} prób"
            print(time.time() - start_time, max_time)
            if time.time() - start_time > max_time:
                return {
                    "msg": msg,
                    "iterations": attempts,
                    'decrypted_data': ''
                }



    def frequency_analysis_aes(self, encrypted_data):
        freq_polish = {'a': 8.91, 'b': 1.47, 'c': 3.96, 'd': 3.25, 'e': 7.66, 'f': 0.3, 'g': 1.42, 'h': 1.08, 'i': 8.21,
                       'j': 2.28, 'k': 3.51, 'l': 2.1, 'm': 2.8, 'n': 5.52, 'o': 7.75, 'p': 3.13, 'q': 0.14, 'r': 4.69,
                       's': 4.32, 't': 3.98, 'u': 2.5, 'v': 0.04, 'w': 4.65, 'x': 0.02, 'y': 3.76, 'z': 5.64}

        start_time = time.time()
        max_time = 5
        attempts = 0

        for i in itertools.product(range(ord('a'), ord('z') + 1), repeat=16):
            if time.time() - start_time > max_time:
                msg = f"Nie udało się złamać po: {attempts} prób"
                return {
                    "msg": msg,
                    "iterations": attempts,
                    'decrypted_data': ''
                }

            attempts += 1
            klucz = bytes(i)
            cipher = AES.new(klucz, AES.MODE_ECB)
            try:

                decrypted_data = cipher.decrypt(encrypted_data)

                freq_decrypted = {}
                for letter in decrypted_data:
                    if letter in freq_decrypted:
                        freq_decrypted[letter] += 1
                    else:
                        freq_decrypted[letter] = 1

                diff_freq = {}
                for letter in freq_decrypted:
                    diff_freq[letter] = abs(freq_decrypted[letter] - freq_polish.get(letter, 0))

                min_diff_letter = min(diff_freq, key=diff_freq.get)

                if diff_freq[min_diff_letter] < 0.01:
                    end_time = time.time()
                    time_elapsed = end_time - start_time
                    msg = "Klucz: " + str(klucz) + " Tekst: " + decrypted_data + " Złamano w " + str(
                        time_elapsed) + " sekund"
                    return msg, klucz, decrypted_data
            except ValueError:
                pass

