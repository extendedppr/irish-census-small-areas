class Base:
    def __init__(self, *args, **kwargs):
        self.model_name = self.__class__.__name__
        self.data = self._parse(args[0])

    def __repr__(self):
        return f"<{self.model_name}>"

    def to_dict(self):
        return {"data": self.data}
