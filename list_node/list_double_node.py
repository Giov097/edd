from typing import Any, Union


class ListDoubleNode:
    __slots__ = "element", "next", "previous"

    def __init__(self, element: Any, next=None, previous=None) -> None:
        self.element = element
        self.next: Union[ListDoubleNode, None] = next
        self.previous: Union[ListDoubleNode, None] = previous
