from Crypto.Random import get_random_bytes
import itertools
import time
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

def encrypt_DES3():
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            pass

    cipher = DES3.new(key, DES3.MODE_CFB)
    plaintext = b'We are no longer the knights who say ni!'
    msg = cipher.iv + cipher.encrypt(plaintext)
    print(msg)

def bruteForce_des3(encrypted_data, iv):
    start_time = time.time()  # Zapisz czas startu
    max_time = 30  # Maksymalny czas działania w sekundach
    attempts = 0  # Licznik prób

    for i in itertools.product(range(256), repeat=24):
        klucz = bytes(i)
        attempts += 1  # Zwiększ licznik prób
        cipher = DES3.new(klucz, DES3.MODE_CFB, iv=iv)
        try:
            decrypted_data = unpad(cipher.decrypt(encrypted_data), DES3.block_size)
            print("Klucz:", klucz, "Tekst:", decrypted_data.decode())
            return  # Zwróć jeśli udało się odszyfrować
        except ValueError:
            pass

        # Sprawdź, czy upłynęło 30 sekund
        if time.time() - start_time > max_time:
            print(f"Nie udało się złamać po: {attempts} prób")
            return  # Zakończ jeśli upłynęło 30 sekund
def main():
    encrypt_DES3()

if __name__ == "__main__":
    main()