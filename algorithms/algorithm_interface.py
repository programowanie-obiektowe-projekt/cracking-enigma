from abc import ABC, abstractmethod

## Adapter pattern
class AlgorithmInterface(ABC):
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, encrypted_data, key):
        pass

    @abstractmethod
    def brute_force(self, encrypted_data, original):
        pass

    @abstractmethod
    def frequency_analysis(self, encrypted_data, original):
        pass