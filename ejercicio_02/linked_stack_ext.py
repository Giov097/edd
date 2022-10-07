import copy
from io import UnsupportedOperation
from typing import Any, List

from linked_stack import LinkedStack
from linked_stack_ext_abstract import LinkedStackExtAbstract


class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num: int) -> List[Any]:
        if self.is_empty():
            raise UnsupportedOperation("La pila está vacía. No se puede realizar la operación.")
        heads_popped = []
        for _ in range(num):
            heads_popped.append(self.pop())
        return heads_popped

    def replace_all(self, param1: Any, param2: Any) -> None:
        actual = self._head
        while self._head != None:
            if self._head.element == param1:
                self._head.element = copy.deepcopy(param2)
            self._head = self._head.next
        self._head = actual if param1 != actual else param2

    def exchange(self) -> None:
        if self.is_empty():
            raise UnsupportedOperation("La pila está vacía. No se puede realizar la operación.")
        head = copy.deepcopy(self._head)
        popped = self.multi_pop(self._size - 1)
        tail = copy.deepcopy(self._head)
        self._head.element = head.element
        for i in reversed(popped):
            self.push(i)
        self._head.element = tail.element
