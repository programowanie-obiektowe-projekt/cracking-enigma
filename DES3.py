from Crypto.Random import get_random_bytes
import itertools
import time
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

def encrypt_DES3(text):
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            pass

    cipher = DES3.new(key, DES3.MODE_CFB)
    text_bytes = text.encode()
    msg = cipher.iv + cipher.encrypt(text_bytes)
    return msg, cipher.iv

def bruteForce_des3(encrypted_data, iv):
    start_time = time.time()
    max_time = 30
    attempts = 0

    for i in itertools.product(range(256), repeat=24):
        klucz = bytes(i)
        attempts += 1
        cipher = DES3.new(klucz, DES3.MODE_CFB, iv=iv)
        try:
            decrypted_data = unpad(cipher.decrypt(encrypted_data), DES3.block_size)
            print("Klucz:", klucz, "Tekst:", decrypted_data.decode())
            return
        except ValueError:
            pass

        if time.time() - start_time > max_time:
            print(f"Nie udało się złamać po: {attempts} prób")
            return

def frequency_analysis_des3(encrypted_data, iv):
    start_time = time.time()
    max_time = 300
    attempts = 0
    freq_polish = {'a': 8.91, 'b': 1.47, 'c': 3.96, 'd': 3.25, 'e': 7.66, 'f': 0.3, 'g': 1.42, 'h': 1.08, 'i': 8.21, 'j': 2.28, 'k': 3.51, 'l': 2.1, 'm': 2.8, 'n': 5.52, 'o': 7.75, 'p': 3.13, 'q': 0.14, 'r': 4.69, 's': 4.32, 't': 3.98, 'u': 2.5, 'v': 0.04, 'w': 4.65, 'x': 0.02, 'y': 3.76, 'z': 5.64}

    for i in itertools.product(range(256), repeat=24):
        klucz = bytes(i)
        cipher = DES3.new(klucz, DES3.MODE_CFB, iv=iv)
        try:
            decrypted_data = unpad(cipher.decrypt(encrypted_data), DES3.block_size).decode()

            freq_decrypted = {}
            for letter in decrypted_data:
                if letter in freq_decrypted:
                    freq_decrypted[letter] += 1
                else:
                    freq_decrypted[letter] = 1

            diff_freq = {}
            for letter in freq_decrypted:
                diff_freq[letter] = abs(freq_decrypted[letter] - freq_polish.get(letter, 0))
                attempts += 1

            min_diff_letter = min(diff_freq, key=diff_freq.get)

            if diff_freq[min_diff_letter] < 0.01:
                msg = "Znaleziono klucz: " + str(klucz) + " Oryginalny tekst: " + decrypted_data + " Złamano w " + str(time.time() - start_time) + " sekund"
                return msg, klucz, decrypted_data
        except ValueError:
            pass
    if time.time() - start_time > max_time:
        msg = f"Nie udało się złamać po: {attempts} prób"
        return msg
def main():
    txt = input("Podaj napis do zaszyfrowania: ")
    encrypt_DES3(txt)

if __name__ == "__main__":
    main()