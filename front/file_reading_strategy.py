from abc import ABC, abstractmethod


class FileReadingStrategy(ABC):
    @abstractmethod
    def read(self, file):
        pass


class ReadAsBytesStrategy(FileReadingStrategy):
    def read(self, file):
        return file.read()


class ReadAsStringStrategy(FileReadingStrategy):
    def read(self, file):
        return file.read().decode('utf-8')


class FileHandler:
    def __init__(self, strategy: FileReadingStrategy):
        self.strategy = strategy

    def handle_file(self, file):
        return self.strategy.read(file)