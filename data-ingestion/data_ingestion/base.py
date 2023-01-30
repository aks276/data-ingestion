from abc import ABC, abstractmethod


class Buckets(ABC):
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pull(self):
        pass
