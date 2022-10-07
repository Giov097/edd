from ctypes.wintypes import DWORD
from double_linked_list import DoubleLinkedList
import unittest


class TestDoubleLinkedList(unittest.TestCase):

    def test_empty_deque(self):
        double_linked_list = DoubleLinkedList()
        self.assertTrue(double_linked_list.is_empty())
        self.assertEqual(double_linked_list.__len__(), 0)
        double_linked_list.append(1)
        self.assertFalse(double_linked_list.is_empty())
        self.assertEqual(double_linked_list.__len__(), 1)

    def test_get_item(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.append(500)
        double_linked_list.append(10)
        double_linked_list.append(20)
        self.assertEqual(double_linked_list.__getitem__(0), 500)
        self.assertEqual(double_linked_list.__getitem__(1), 10)
        self.assertEqual(double_linked_list.__getitem__(2), 20)

    def test_set_item(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.append(500)
        double_linked_list.append(10)
        double_linked_list.append(20)
        double_linked_list.__setitem__(0, 1000)
        double_linked_list.__setitem__(1, 2000)
        double_linked_list.__setitem__(2, 3000)
        self.assertEqual(double_linked_list.__getitem__(0), 1000)
        self.assertEqual(double_linked_list.__getitem__(1), 2000)
        self.assertEqual(double_linked_list.__getitem__(2), 3000)

    def test_del_item(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.append(500)
        double_linked_list.append(10)
        double_linked_list.append(20)
        double_linked_list.append(50)
        double_linked_list.append(800)
        double_linked_list.__delitem__(0)
        self.assertEqual(double_linked_list.__getitem__(0), 10)
        self.assertEqual(double_linked_list.__getitem__(1), 20)
        double_linked_list.__delitem__(2)
        self.assertEqual(double_linked_list.__getitem__(0), 10)
        self.assertEqual(double_linked_list.__getitem__(1), 20)
        self.assertEqual(double_linked_list.__getitem__(2), 800)

    def test_str(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.append(500)
        double_linked_list.append(10)
        double_linked_list.append(20)
        self.assertEqual(double_linked_list.__str__(),
                         "DoubleLinkedList(500, 10, 20)")

    def test_iter(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.append(500)
        double_linked_list.append(10)
        double_linked_list.append(20)
        x = double_linked_list.__iter__()
        self.assertEqual(x.__next__(), 500)
        self.assertEqual(x.__next__(), 10)
        self.assertEqual(x.__next__(), 20)


if __name__ == '__main__':
    unittest.main()
