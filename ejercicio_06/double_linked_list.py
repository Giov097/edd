from io import UnsupportedOperation
from typing import Any, Iterator
from double_linked_list_abstract import DoubleLinkedListAbstract
from list_node.list_double_node import ListDoubleNode


class DoubleLinkedList(DoubleLinkedListAbstract):

    _EMPTY_LIST_EXCEPTION = "Operación no permitida si la estructura está vacía."
    _OUT_OF_BOUNDS_EXCEPTION = "Índice fuera de rango. No se puede continuar."

    def __init__(self):
        self._header: ListDoubleNode = ListDoubleNode(None)
        self._footer: ListDoubleNode = ListDoubleNode(None)
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, key: int) -> Any:
        if self.is_empty():
            raise UnsupportedOperation(DoubleLinkedList._EMPTY_LIST_EXCEPTION)
        if key < 0 or key >= self._size:
            raise UnsupportedOperation(
                DoubleLinkedList._OUT_OF_BOUNDS_EXCEPTION)
        i = 0
        actual = self._header
        while actual:
            if i == key:
                return actual.element
            actual = actual.next
            i += 1
        return None

    def __setitem__(self, key: int, value: Any) -> None:
        if self.is_empty():
            raise UnsupportedOperation(DoubleLinkedList._EMPTY_LIST_EXCEPTION)
        if key < 0 or key >= self._size:
            raise UnsupportedOperation(
                DoubleLinkedList._OUT_OF_BOUNDS_EXCEPTION)
        i = 0
        actual = self._header
        while actual:
            if i == key:
                actual.element = value
            actual = actual.next
            i += 1

    def __delitem__(self, key: int) -> None:
        if self.is_empty():
            raise UnsupportedOperation(DoubleLinkedList._EMPTY_LIST_EXCEPTION)
        if key < 0 or key >= self._size:
            raise UnsupportedOperation(
                DoubleLinkedList._OUT_OF_BOUNDS_EXCEPTION)
        i, previous, actual = 0, None, self._header
        while actual:
            if i == key:
                break
            previous, actual = actual, actual.next
            i += 1
        if previous:
            previous.next = actual.next
        else:
            self._header = actual.next
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        actual = self._header
        while actual:
            yield actual.element
            actual = actual.next

    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleLinkedList()"
        res = ""
        actual = self._header
        while actual:
            res += str(actual.element) + ", "
            actual = actual.next
        res = res[:-2]
        return f"DoubleLinkedList({res})"

    def is_empty(self) -> bool:
        return self._size == 0

    def append(self, elem: Any) -> None:
        nuevo_nodo = ListDoubleNode(elem, previous=self._footer)
        if self.is_empty():
            self._header, self._footer = nuevo_nodo, nuevo_nodo
        else:
            self._footer.next, self._footer = nuevo_nodo, nuevo_nodo
        self._size += 1
