from typing import Union, Self

class Manufacturer:
    def __init__(self, data_obg):
        self.id: str = data_obg['id']
        self.name: str = data_obg['name']
        self.description: str = data_obg['description']
        # Assert
        assert isinstance(self.id, str)
        assert isinstance(self.id, str)
        assert isinstance(self.id, str)