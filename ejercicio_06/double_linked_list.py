from typing import Any, Iterator

from double_linked_list_abstract import DoubleLinkedListAbstract


class DoubleLinkedList(DoubleLinkedListAbstract):
    def __len__(self) -> int:
        pass

    def __getitem__(self, key: int) -> Any:
        pass

    def __setitem__(self, key: int, value: Any) -> None:
        pass

    def __delitem__(self, key: int) -> None:
        pass

    def __iter__(self) -> Iterator[Any]:
        pass

    def __str__(self) -> str:
        pass

    def is_empty(self) -> bool:
        pass

    def append(self, elem: Any) -> None:
        pass
