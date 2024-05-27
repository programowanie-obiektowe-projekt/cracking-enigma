from algorithms.AES import AESAdapter
from algorithms.Cezar import CezarAdapter
from algorithms.DES3 import DES3Adapter

class AlgorithmFactory:
    @staticmethod
    def create_algorithm(algorithm_name):
        if algorithm_name == 'AES':
            return AESAdapter()
        elif algorithm_name == 'Szyfr cezara':
            return CezarAdapter()
        elif algorithm_name == 'DES3':
            return DES3Adapter()

