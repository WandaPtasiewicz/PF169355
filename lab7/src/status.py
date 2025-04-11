from enum import Enum, auto


class Status(Enum):
        AVAILABLE = auto()
        BORROWED = auto()
        RESERVED = auto()
        ARCHIVED = auto()