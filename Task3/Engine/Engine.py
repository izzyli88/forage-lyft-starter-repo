from abc import ABC, abstractmethod

"""
Abstract class for an engine, extending to the CapuletEngine.py, WilloughbyEngine,
and SternmanEngine subclasses
"""
class Engine(ABC):

    """
    Constructor for the class
    """
    def __init__(self):
        pass

    """
    Abstract method returning a boolean flag for needsServicing
    """
    @abstractmethod
    def needs_service(self):
        pass

