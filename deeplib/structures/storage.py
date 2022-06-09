import re


class Storage:
    """
    General-purpose data container.
    """

    def __init__(self, storage={}):
        self.storage = storage

    def items(self):
        return self.storage.items()

    def get(self, key=""):
        return Storage(
            {name: data for name, data in self.storage.items() if re.search(key, name)}
        )

    def values(self):
        return [a.value() for a in self.storage.values()]

    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __contains__(self, key):
        return key in self.storage

    def __len__(self):
        return len(self.storage)

    def __iter__(self):
        return iter(self.storage)

    def layers(self):
        return list(self.storage.keys())