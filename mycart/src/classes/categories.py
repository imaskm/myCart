class Category:

    def __init__(self, _id, name):
        self.name = name
        self.__id = _id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def get_id(self):
        return self.__id


