import unittest

def main():
    unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("tests"))

if __name__ == "__main__":
    main()
