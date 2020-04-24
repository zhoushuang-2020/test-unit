import unittest
import mathfunc

class TestMathFunc(unittest.TestCase):

    def setUp(self):
        print("do something before test.Prepare environment..")

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_add(self):
        """
        Test method add(a,b)
        :return:
        """
        self.assertEqual(3,mathfunc.add(1,2))
        self.assertNotEqual(3,mathfunc.add(2,2))

    def test_minus(self):
        """
        Test method minus(a,b)
        :return:
        """
        self.assertEqual(1,mathfunc.minus(3,2))

    def test_multi(self):
        """
        Test method multi(a,b)
        :return:
        """
        self.assertEqual(6,mathfunc.multi(2,3))
        self.assertNotEqual(8,mathfunc.multi(3,3))

    #@unittest.skipIf(True,'no run')
    def test_divide(self):
        """
        Test method divide(a,b)
        :return:
        """

        self.assertEqual(3,mathfunc.divide(4,2))
        self.assertEqual(2.5,mathfunc.divide(5,2))


if __name__ == '__main__':
    unittest.main()
