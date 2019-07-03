import QuantLib as ql
import unittest


class CashflowsTest(unittest.TestCase):
    def runTest(self):
        "Testing cash flows"
        ql.SubPeriodsCoupon()


if __name__ == "__main__":
    print("testing QuantLib " + ql.__version__)
    suite = unittest.TestSuite()
    suite.addTest(CashflowsTest())
    unittest.TextTestRunner(verbosity=2).run(suite)
