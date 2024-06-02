import unittest
import AES_Tests, Cezar_Tests, DES3_Tests

def main():
    # Create a test loader
    loader = unittest.TestLoader()

    # Create a test suite
    suite = unittest.TestSuite()

    # Add tests to the suite
    suite.addTests(loader.loadTestsFromModule(AES_Tests))
    suite.addTests(loader.loadTestsFromModule(Cezar_Tests))
    suite.addTests(loader.loadTestsFromModule(DES3_Tests))

    # Run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()