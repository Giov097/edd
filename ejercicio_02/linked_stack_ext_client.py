from io import UnsupportedOperation
from linked_stack_ext import LinkedStackExt
import unittest


class TestLinkedStackExt(unittest.TestCase):

    def test_multi_pop(self):
        linked_stack_ext = LinkedStackExt()
        self.assertTrue(linked_stack_ext.is_empty())
        self.assertEqual(linked_stack_ext.__len__(), 0)
        linked_stack_ext.push(1)
        linked_stack_ext.push(20)
        linked_stack_ext.push(3)
        linked_stack_ext.push(3)
        linked_stack_ext.push(3)
        linked_stack_ext.push(3)
        linked_stack_ext.push(45)
        linked_stack_ext.push(70)
        self.assertFalse(linked_stack_ext.is_empty())
        self.assertEqual(linked_stack_ext.__len__(), 8)
        self.assertEqual("LinkedStack(70, 45, 3, 3, 3, 3, 20, 1)",
                         linked_stack_ext.__str__())
        linked_stack_ext.multi_pop(2)
        self.assertEqual(linked_stack_ext.__len__(), 6)
        self.assertEqual("LinkedStack(3, 3, 3, 3, 20, 1)",
                         linked_stack_ext.__str__())

    def test_exchange(self):
        linked_stack_ext = LinkedStackExt()
        linked_stack_ext.push(1)
        linked_stack_ext.push(20)
        linked_stack_ext.push(3)
        linked_stack_ext.push(3)
        self.assertEqual(linked_stack_ext.__str__(),
                         "LinkedStack(3, 3, 20, 1)")
        linked_stack_ext.exchange()
        self.assertEqual(linked_stack_ext.__str__(),
                         "LinkedStack(1, 3, 20, 3)")

    def test_replace(self):
        linked_stack_ext = LinkedStackExt()
        linked_stack_ext.push(1)
        linked_stack_ext.push(20)
        linked_stack_ext.push(3)
        linked_stack_ext.push(3)
        self.assertEqual(linked_stack_ext.__str__(),
                         "LinkedStack(3, 3, 20, 1)")
        linked_stack_ext.replace_all(3, 4)
        self.assertEqual(linked_stack_ext.__str__(),
                         "LinkedStack(4, 4, 20, 1)")

if __name__ == '__main__':
    unittest.main()