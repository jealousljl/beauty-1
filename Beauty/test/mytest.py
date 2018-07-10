import unittest


def setUpModule():
    print('In setUpModule()...')


def tearDownModule():
    print('In tearDownModule()...')


class TestClass02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()...')

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()...')

    def setUp(self):
        print('\nIn setUp()...')

    def tearDown(self):
        print('In tearDown()...')

    def test_case01(self):
        self.assertTrue('PYTHON'.isupper())
        print('In test_case01()')


if __name__ == '__main__':
    unittest.main()
