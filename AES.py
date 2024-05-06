from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import itertools
import time

def szyfruj_aes(napis):
    klucz = get_random_bytes(16)

    cipher = AES.new(klucz, AES.MODE_ECB)
    napis = napis.encode()
    padded_data = pad(napis, AES.block_size)

    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data, klucz

def bruteForce_aes(encrypted_data):
    start_time = time.time()  # Zapisz czas startu
    max_time = 30  # Maksymalny czas działania w sekundach
    attempts = 0  # Licznik prób

    for i in itertools.product(range(ord('a'), ord('z')+1), repeat=16):
        klucz = bytes(i)
        attempts += 1  # Zwiększ licznik prób
        cipher = AES.new(klucz, AES.MODE_ECB)
        try:
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            print("Klucz:", klucz, "Tekst:", decrypted_data.decode())
            return  # Zwróć jeśli udało się odszyfrować
        except ValueError:
            pass

        # Sprawdź, czy upłynęło 30 sekund
        if time.time() - start_time > max_time:
            print(f"Nie udało się złamać po: {attempts} prób")
            return  # Zakończ jeśli upłynęło 30 sekund
def main():
    napis = input("Podaj napis do zaszyfrowania: ")
    szyfrogram, klucz = szyfruj_aes(napis)
    print("Zaszyfrowany napis:", szyfrogram)
    print("Klucz:", klucz)
    bruteForce_aes(szyfrogram)

if __name__ == "__main__":
    main()