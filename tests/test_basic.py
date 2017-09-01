# -*- coding: utf-8 -*-

from .context import blood_simulator

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dict(self):
        self.activity_class = Activity()
        self.exercise_dict = self.get_activity_dict(file_path + '/exercise.csv')
        self.food_dict = self.get_activity_dict(file_path + '/food.csv')
        self.assertTrue(self.exercise_dict.contains_key('id'))

    #TODO: Import other local tests, 

if __name__ == '__main__':
    unittest.main()