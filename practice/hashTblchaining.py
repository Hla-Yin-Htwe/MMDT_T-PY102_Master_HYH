# class HashTableChaining:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]  # Each slot has a list for collisions

#     # Hash function for string IDs
#     def hash_function(self, key):
#         hash_val = 0
#         for char in key:
#             hash_val = (hash_val * 31 + ord(char)) % self.size  # Better distribution
#         return hash_val

#     # Insert ID into the table
#     def insert(self, key):
#         index = self.hash_function(key)
#         self.table[index].append(key)
#         print(f"Inserted {key} at index {index} (chain length {len(self.table[index])})")

#     # Display the table
#     def display(self):
#         print("\nHash Table (with chaining):")
#         for i, chain in enumerate(self.table):
#             print(f"Index {i}: {chain}")


# # Example usage
# ht = HashTableChaining(size=10)

# # Insert 20 IDs
# for i in range(3, 23):  # PY102001003 → PY102001022
#     id_ = f"PY102001{i:03d}"
#     ht.insert(id_)

# ht.display()

class HashTableNoModulo:
    def __init__(self):
        self.table = {}  # Use dictionary for automatic collision handling

    # Insert ID into table
    def insert(self, key):
        hashed_key = hash(key)  # Python generates an integer hash
        if hashed_key in self.table:
            # If collision occurs, store in a list
            self.table[hashed_key].append(key)
        else:
            self.table[hashed_key] = [key]  # First ID at this hash
        print(f"Inserted {key} at hashed key {hashed_key}")

    # Display the table
    def display(self):
        print("\nHash Table (No manual modulo, using Python hash):")
        for hashed_key, ids in self.table.items():
            print(f"{hashed_key}: {ids}")


# ---------------------------
# Example usage
# ---------------------------

ht = HashTableNoModulo()

# Insert 20 IDs: PY102001003 → PY102001022
for i in range(3, 23):
    id_ = f"PY102001{i:03d}"
    ht.insert(id_)

ht.display()