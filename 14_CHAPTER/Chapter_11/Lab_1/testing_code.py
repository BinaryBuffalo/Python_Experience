import unittest
from name_function import get_formatted_name

class NamestestCase(unittest.TestCase):
    """Tests for 'name_fucntion.py'"""
    def get_formatted_name(self):
        """Generate a neatly formatted full name"""
        formatted_name = get_formatted_name('Janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()