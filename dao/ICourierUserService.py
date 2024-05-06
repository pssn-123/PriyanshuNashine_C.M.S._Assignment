from abc import ABC, abstractmethod

class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courier):
        pass

    @abstractmethod
    def getOrderStatus(self):
        pass

    @abstractmethod
    def cancleOrder(self):
        pass

    @abstractmethod
    def getAssignedOrder(self):
        pass

