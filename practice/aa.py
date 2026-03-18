# class HashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [None] * size

#     # Simple hash function: mod table size
#     def hash_function(self, key):
#         return key % self.size

#     # Insert ID into the table
#     def insert(self, key):
#         index = self.hash_function(key)
#         original_index = index
#         steps = 0

#         # Linear probing to reduce collisions
#         while self.table[index] is not None:
#             steps += 1
#             index = (original_index + steps) % self.size
#             if steps >= self.size:
#                 print("HashTable is full!")
#                 return

#         self.table[index] = key
#         print(f"Inserted {key} at index {index}")

#     # Display the table
#     def display(self):
#         print("Hash Table:")
#         for i, val in enumerate(self.table):
#             print(f"Index {i}: {val}")


# # Usage
# ht = HashTable(size=10)
# ids_to_insert = [12, 22, 32, 42, 5, 15]

# for id_ in ids_to_insert:
#     ht.insert(id_)

# ht.display()


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Hash function for string IDs
    def hash_function(self, key):
        # Convert string to integer by summing ASCII values
        hash_value = sum(ord(char) for char in key)
        return hash_value % self.size

    # Insert ID into the table (with linear probing)
    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        steps = 0

        while self.table[index] is not None:
            steps += 1
            index = (original_index + steps) % self.size
            if steps >= self.size:
                print("HashTable is full!")
                return

        self.table[index] = key
        print(f"Inserted {key} at index {index}")

    # Display the table
    def display(self):
        print("Hash Table:")
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


# Example usage
ht = HashTable(size=10)
ids_to_insert = ["PY102001003", "PY102001004", "PY102001005", "PY102001006"]

for id_ in ids_to_insert:
    ht.insert(id_)

ht.display()