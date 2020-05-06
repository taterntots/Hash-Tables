class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity # This is the number of buckets in our hash table
        self.storage = [None] * capacity
        self.head = None
        self.key_count = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Define variables for legibility
        index = self.hash_index(key)
        node = self.storage[index]
        new_node = HashTableEntry(key, value)
        load_factor = None

        # If our node exists in storage
        if node:
            # Replace our node with the value
            node = value
        # Otherwise
        else:
            # Create a new record for the list and assign to the head
            new_node.next = self.head
            print(new_node.key)
            # Make the head the new node
            self.head = new_node
            # Add one to our counter for calculating load factor
            self.key_count += 1
            # Set our load_factor
            load_factor = self.key_count / self.capacity

            # If load factor is greater than 0.7
            if load_factor > 0.7:
                # Double the size of our hashtable
                self.resize(self.capacity * 2)
                # Set our load_factor to the new size
                load_factor = self.key_count / self.capacity
                
            print(load_factor)
            # print(self.count)
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Define variables for legibility
        current = self.head
        load_factor = self.key_count / self.capacity
        print(f'count', self.key_count)

        # While the current node exists (starting at the head)
        while current:
            # If the current node's key is equal to the key being passed
            if current.key == key:
                # Reset that node's key to None
                current.key = None
                # Reduce the key count by one
                self.key_count -= 1
                print(f'count', self.key_count)
                # Set a new load factor with the reduced key count
                load_factor = self.key_count / self.capacity
                print(f'lf', load_factor)

                # If load factor falls below 0.2
                if load_factor < 0.2:
                    # Half the size of the hashtable
                    self.resize(self.capacity // 2)
                    # Set our load_factor to the new size
                    load_factor = self.key_count / self.capacity

                print(f'LOOK HERE', load_factor)
            
            # Redefine current node to the next node before looping again
            current = current.next

        # Otherwise, if there are no more 'next' nodes, return None
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Define variables for legibility
        current = self.head

        # WWhile the current node exists (starting at the head)
        while current:
            # If the current node's key is equal to the key being passed
            if current.key == key:
                # Return that node's value
                return current.value
            
            # Redefine current node to the next node before looping again
            current = current.next

        # Otherwise, if there are no more 'next' nodes, return None
        return None

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # Redefine our capacity to be the passed in capacity from our argument
        self.capacity = new_capacity
        # Create a new storage variable for containing our updated list
        new_storage = [None] * self.capacity
        
        # For each value in our original stored list
        for value in self.storage:
            # If a value exists
            if value:
                # Change our index and store the hashed key's value to our new storage
                hashed_key = self.hash_index(value[0])
                new_storage[hashed_key] = value
        
        # Replace the old storage with the new one
        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print(ht.delete("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize(843)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
