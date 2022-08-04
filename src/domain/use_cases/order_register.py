from typing import Dict
from abc import ABC


class OrderRegister(ABC):

    @classmethod
    def register_order(self, data: Dict) -> Dict:
        pass
