from abc import ABC, abstractmethod

class VueBase(ABC):
    def __init__(self):
        self._children = []

    @abstractmethod
    def render(self):
        pass

    def add(self, child):
        self._children.append(child)
        return self

class VueComponent(VueBase):
    pass

class VuePage(VueBase):
    pass
