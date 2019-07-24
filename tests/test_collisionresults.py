"""

tests/test_debug.py

written by: Oliver Cordes 2019-07-22
changed by: Oliver Cordes 2019-07-22

"""

from pycollision.collision import CollisionResult


import unittest
from unittest import mock
from unittest.mock import patch
import io


class TestDebug(unittest.TestCase):
    """
    CollisionResult: collision item
    """
    def test_result1(self):
        result = CollisionResult()

        result['collision'] = True

        self.assertEqual(result['collision'], True)

    """
    CollisionResult: random item
    """
    def test_result2(self):
        result = CollisionResult()

        result['collision'] = True
        result['item'] = 'value'

        self.assertEqual(result['item'], 'value')

    """
    CollisionResult: item iterations
    """
    def test_result3(self):
        result = CollisionResult()

        result['collision'] = True
        result['item'] = 'value'

        for i in result.items():
            self.assertEqual(i[0], 'item')
            self.assertEqual(i[1], 'value')

    """
    CollisionResult: call of the object
    """
    def test_result4(self):
        result = CollisionResult()

        # the default value
        self.assertEqual(result(), False)

        result['collision'] = True

        self.assertEqual(result(), True)

    """
    CollisionResult: __str__
    """
    def test_result5(self):
        result = CollisionResult()

        result['collision'] = True
        result['item'] = 'value'

        self.assertEqual(result.__str__(),
                         '{collision: True, data: {\'item\': \'value\'}}')
