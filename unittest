import unittest
from optimal_change import ChangeMaker

class ChageMakerTest(unittest.TestCase):
    
    def test_case1(self):
        Change_Maker1 = ChangeMaker(62.13, 100)
        self.assertEqual(Change_Maker1.optimal_change(), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, 2 pennies.")

    def test_case2(self):
        Change_Maker2 = ChangeMaker(31.51, 50)
        self.assertEqual(Change_Maker2.optimal_change(), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, 4 pennies.")

    def test_case3(self):
        ''' Test the payment equals the price.'''
        Change_Maker3 = ChangeMaker(1000, 1000)
        self.assertEqual(Change_Maker3.optimal_change(), "The payment equals the price. No changes.")

    def test_case4(self):
        '''Test the payment is not enough.'''
        Change_Maker4 = ChangeMaker(0.5, 0.1)
        self.assertEqual(Change_Maker4.optimal_change(), "The costs are $0.5 and the amount you paid are $0.1, please go on the payment.")

    def test_case5(self):
        ''' Test the change is $0.01.'''
        Change_Maker5 = ChangeMaker(0.01, 0.02)
        self.assertEqual(Change_Maker5.optimal_change(), "The optimal change for an item that costs $0.01 with an amount paid of $0.02 is 1 penny.")


if __name__=='__main__':
    unittest.main()
