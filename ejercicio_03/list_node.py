from typing import Any, Union


class ListNode:
    __slots__ = "element", "next", "previous"

    def __init__(self, element: Any, next=None, previous=None) -> None:
        self.element = element
        self.next: Union[ListNode, None] = next
        self.previous: Union[ListNode, None] = previous
