import unittest
from citycountry import geosaver

class SuperTest(unittest.TestCase):
    """Tests for 'name_fucntion.py'"""
    def geosaver(self):
        """Generate a neatly formatted full name"""
        formatted_name = geosaver('amsterdam','netherlands')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()