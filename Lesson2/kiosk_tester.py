import unittest
import unittest.mock
from kiosk import Kiosk

class TestKiosk(unittest.TestCase):
    def setUp(self):
        self.kiosk = Kiosk()
        self.kiosk.items_={"milk":[4.50,4.50],"bread":[2.75],"cereal":[3.75]}
        self.kiosk.item_total = 4
        self.kiosk.transcation_total = 15.5
        self.kiosk.payment = 20
        self.kiosk.change = 4.5
        
    def test_attributes(self):
        self.assertEqual(self.kiosk.item_total,4)
        self.assertAlmostEqual(self.kiosk.transcation_total,15.50,1)
        self.assertEqual(self.kiosk.payment, 20)
        self.assertAlmostEqual(self.kiosk.change,4.5,1)
        
    def test_print_receipt(self):
        self.kiosk.print_receipt()
        

if __name__ == '__main__':
    unittest.main()