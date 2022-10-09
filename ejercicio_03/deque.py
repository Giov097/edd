from typing import Any, Union
from deque_abstract import DequeAbstract
from collections import deque
from io import UnsupportedOperation

from list_node.list_double_node import ListDoubleNode


class Deque(DequeAbstract):

    def __init__(self):
        self._first: Union[ListDoubleNode, None] = None
        self._last: Union[ListDoubleNode, None] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        if self.is_empty():
            return "Deque()"
        resultado = ""
        actual = self._first
        while actual != None:
            resultado += str(actual.element) + ", "
            actual = actual.next
        resultado = resultado[:len(resultado) - 2]
        return f"Deque({resultado})"

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self) -> Any:
        if self.is_empty():
            raise UnsupportedOperation("Deque vacía. Operación no soportada")
        return self._first.element

    def last(self) -> Any:
        if self.is_empty():
            raise UnsupportedOperation("Deque vacía. Operación no soportada")
        return self._last.element

    def add_first(self, element: Any) -> None:
        new_first = ListDoubleNode(element, next=self._first)
        if self.is_empty():
            self._last = new_first
        else:
            self._first.previous = new_first
        self._first = new_first
        self._size += 1

    def add_last(self, element: Any) -> None:
        new_last = ListDoubleNode(element, previous=self._last)
        if self.is_empty():
            self._first = new_last
        else:
            self._last.next = new_last
        self._last = new_last
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise UnsupportedOperation("Pila vacía. Operación no soportada")
        self._first = self._first.next
        self._size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise UnsupportedOperation("Pila vacía. Operación no soportada")
        self._last = self._last.previous
        self._last.next = None
        self._size -= 1
