import unittest


class TestRaisesModuleNotFoundError(unittest.TestCase):
    def test_raises_module_not_found(self):
        # test basic functionality
        with self.assertRaises(ModuleNotFoundError):
            import raise_module_not_found_error

    def test_raises_module_not_found_with_correct_message(self):
        # test that the error message fulfills memetic and humoristic requirements
        with self.assertRaises(ModuleNotFoundError, msg="Ceci n'est pas un module"):
            import raise_module_not_found_error
