"""
Base mapper class and common mapping utilities
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

S = TypeVar('S')  # Source type
T = TypeVar('T')  # Target type

class BaseMapper(ABC, Generic[S, T]):
    @abstractmethod
    def map(self, source: S) -> T:
        """Map source object to target object"""
        pass