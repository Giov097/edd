from ctypes.wintypes import DWORD
from deque import Deque
import unittest


class TestDeque(unittest.TestCase):

    def test_empty_deque(self):
        deque = Deque()
        self.assertTrue(deque.is_empty())
        self.assertEqual(deque.__len__(), 0)
        deque.add_first(1)
        self.assertFalse(deque.is_empty())
        self.assertEqual(deque.__len__(), 1)

    def test_add_first(self):
        deque = Deque()
        deque.add_first(50)
        deque.add_first(40)
        deque.add_first(30)
        self.assertEqual(deque.__str__(), "Deque(30, 40, 50)")
        self.assertEqual(deque.first(), 30)
        self.assertEqual(deque.last(), 50)

    def test_add_last(self):
        deque = Deque()
        deque.add_last(60)
        deque.add_last(70)
        deque.add_last(80)
        self.assertEqual(deque.__str__(), "Deque(60, 70, 80)")
        self.assertEqual(deque.first(), 60)
        self.assertEqual(deque.last(), 80)

    def test_mixed_additions_1(self):
        deque = Deque()
        deque.add_last(50)
        deque.add_last(40)
        deque.add_last(30)
        self.assertEqual(deque.__str__(), "Deque(50, 40, 30)")
        deque.add_first(60)
        deque.add_first(70)
        deque.add_first(80)
        self.assertEqual(deque.__str__(), "Deque(80, 70, 60, 50, 40, 30)")
        self.assertEqual(deque.first(), 80)
        self.assertEqual(deque.last(), 30)

    def test_mixed_additions_2(self):
        deque = Deque()
        deque.add_last(40)
        deque.add_first(30)
        deque.add_last(50)
        deque.add_first(20)
        deque.add_last(60)
        deque.add_first(10)
        self.assertEqual(deque.__str__(), "Deque(10, 20, 30, 40, 50, 60)")
        self.assertEqual(deque.first(), 10)
        self.assertEqual(deque.last(), 60)

    def test_delete_first(self):
        deque = Deque()
        deque.add_first(50)
        deque.add_first(40)
        deque.add_first(30)
        deque.add_first(20)
        deque.add_first(10)
        self.assertEqual(deque.__str__(), "Deque(10, 20, 30, 40, 50)")
        deque.delete_first()
        self.assertEqual(deque.__str__(), "Deque(20, 30, 40, 50)")
        deque.delete_first()
        self.assertEqual(deque.__str__(), "Deque(30, 40, 50)")

    def test_delete_last(self):
        deque = Deque()
        deque.add_first(50)
        deque.add_first(40)
        deque.add_first(30)
        deque.add_first(20)
        deque.add_first(10)
        self.assertEqual(deque.__str__(), "Deque(10, 20, 30, 40, 50)")
        deque.delete_last()
        self.assertEqual(deque.__str__(), "Deque(10, 20, 30, 40)")
        deque.delete_last()
        self.assertEqual(deque.__str__(), "Deque(10, 20, 30)")

    def test_first_and_last(self):
        deque = Deque()
        deque.add_last(50)
        deque.add_last(40)
        deque.add_last(30)
        deque.add_last(20)
        deque.add_last(10)
        self.assertEqual(deque.__str__(), "Deque(50, 40, 30, 20, 10)")
        self.assertEqual(deque.first(), 50)
        self.assertEqual(deque.last(), 10)


if __name__ == '__main__':
    unittest.main()
