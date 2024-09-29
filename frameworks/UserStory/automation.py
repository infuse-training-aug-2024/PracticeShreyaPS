import unittest
from FunctionalTests.SortingTests import SortingTests
from FunctionalTests.SidebarTests import SidebarTests
from FunctionalTests.ShoppingCartTests import ShoppingCartTests
from FunctionalTests.LoginTests import LoginTests
from FunctionalTests.CheckoutTests import CheckoutTests

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SortingTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SidebarTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CheckoutTests))

    runner = unittest.TextTestRunner()
    runner.run(suite)
