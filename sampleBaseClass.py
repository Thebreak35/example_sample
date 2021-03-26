from abc import ABC, abstractmethod

class SampleBaseClass(ABC):
    @abstractmethod
    def sample(self):
        raise NotImplementedError
