from typing import Dict
from abc import ABC, abstractmethod


class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def register_order(self, data: Dict) -> Dict:
        pass
