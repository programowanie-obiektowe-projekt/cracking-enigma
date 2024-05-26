from abc import ABC, abstractmethod

## Adapter pattern
class AlgorithmInterface(ABC):
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, encrypted_data, key):
        pass