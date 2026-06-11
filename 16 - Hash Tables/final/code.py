class HashTable:
    def __init__(self, size: int = 7):
        self.data = [None] * size

    def __hash(self, key: str) -> int:
        hash_value = 0
        for letters in key:
            hash_value = (hash_value + ord(letters) * 23) % len(self.data)
        return hash_value

    def print_table(self):
        for i, value in enumerate(self.data):
            print(f"{i}: {value}")

    def set_item(self, key: str, value: int):
        index = self.__hash(key)
        if self.data[index] is None:
            self.data[index] = []
        self.data[index].append([key, value])

    def get_item(self, key: str):
        index = self.__hash(key)
        if self.data[index] is not None:
            for item in self.data[index]:
                if item[0] == key:
                    return item[1]
        return None

    def get_keys(self):
        keys = []
        for items in self.data:
            if items is not None:
                for key in items:
                    keys.append(key[0])
        return keys


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 10000)
my_hash_table.set_item("washers", 54)
my_hash_table.set_item("lubmber", 2)

# my_hash_table.print_table()
print(my_hash_table.get_item("bolts"))

print( my_hash_table.get_keys())
