from LinkedList import LinkedList


class HashTable:
    capacity = 16
    length = 0

    def __init__(self):
        self.keys = [None] * self.capacity

    def insert(self, value):
        key_sum = self.hash_func(value)
        key = self.get_index_from_hash(key_sum)

        if not self.keys[key]:
            self.keys[key] = LinkedList()
        self.keys[key].append(value)
        self.length += 1

        if self.length / self.capacity > 0.74:
            self.get_more_size()

    def get_index_from_hash(self, hash_sum):
        return hash_sum % self.capacity

    def get_more_size(self):
        self.capacity *= 2
        arr = [None] * self.capacity
        for v in self.keys:
            if not v:
                continue
            q = v.popleft()
            print(q)
            while q or q == 0:
                v_sum = self.hash_func(q)
                v_key = self.get_index_from_hash(v_sum)

                if not arr[v_key]:
                    arr[v_key] = LinkedList()
                arr[v_key].append(q)

                q = v.popleft()
            print(arr)
        print(arr)
        self.keys = arr

    def find(self, value):
        v_sum = self.hash_func(value)
        v_key = self.get_index_from_hash(v_sum)
        if self.keys[v_key]:
            return self.keys[v_key]
        return False

    def delete(self, value):
        v_sum = self.hash_func(value)
        v_key = self.get_index_from_hash(v_sum)
        print(v_key)
        if self.keys[v_key]:
            self.keys[v_key] = None
            return True
        return False

    @staticmethod
    def hash_func(value):
        try:
            text = str(value)
        except Exception:
            raise Exception(f'{value} is not hashable')
        return sum(ord(character) for character in text)

    def __str__(self):
        out = []
        for v in self.keys:
            if v:
                out.append(str(v))
            else:
                out.append('_')
        return ' | '.join(out)
