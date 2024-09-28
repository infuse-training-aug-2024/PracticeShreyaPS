import unittest

# Import your test classes
from SortingTests import SortingTests
from SidebarTests import SidebarTests
from ShoppingCartTests import ShoppingCartTests
from LoginTests import LoginTests
from CheckoutTests import CheckoutTests

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()

    # Add tests from each test case class
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SortingTests))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SidebarTests))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTests))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTests))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CheckoutTests))

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
