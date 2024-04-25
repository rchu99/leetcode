class Vector:
    def __init__(self):
        self.capacity = 2  # Set an initial capacity of 2
        self.size = 0
        self.elements = [None] * self.capacity  # Initialize elements with the initial capacity

    def get_elements(self):
        return self.elements

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def at(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Out of bounds")
        else:
            return self.elements[index]

    #Add items to the end of list
    def push(self, item):
        if self.is_full():
            self._resize(1)
        self.elements[self.size] = item
        self.size += 1

    #insert item at index and shifts all elements to right
    def _insert(self, index, item):
        if index > self.size or index < 0:
            raise IndexError("Out of bounds")
        
        if self.is_full():
            self._resize(1)
        
        # starts at self.size and decrements by 1 until it reaches index (not including index itself).
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i-1]
        self.elements[index] = item
        
    #insert item at index 0 and shift all elements to right
    def prepend(self, item):
        self.size +=1
        self._resize(1)

        for i in range(self.size, 0, -1):
            self.elements[i] = self.elements[i-1]
        self.elements[0] = item

    #delete item at index, shifting all trailing elements left
    def delete(self, index):
        for i in range(index, self.size):
            self.elements[i] = self.elements[i+1]
        self._resize(-1)
        self.size -=1

    #looks for value and removes index holding it (even if in multiple places)
    def remove(self, item):
        for i in range(0, self.size):
            if self.elements[i] == item and i == self.size:
                self.elements[i] = None
                self._resize(-1)
            elif self.elements[i] == item:
                self.delete(i)


    def pop(self):
        return self.elements[self.size]

    def is_full(self):
        return self.size == self.capacity

    def _resize(self, new_capacity):
        new_elements = [None] * (self.capacity + new_capacity)
        for i in range(0, self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity += new_capacity


            
# Example usage:
v = Vector()
print(v.get_size())  # Output 0
print(v.is_empty())  # Output True
v.push(1)
v.push(3)
v.push(4)

print(v.at(2)) # Output 4
print(v._insert(1,2)) #insert 2 at index 1
print(v.get_elements()) 

print(v.prepend(0)) #insert 0 in begin
print(v.get_elements()) 
print(v.pop())
print("after pop " + str(v.get_elements())) 
print(v._insert(1,25))
print("after ins " + str(v.get_elements())) 
print(v._insert(4,25))
print("after ins " + str(v.get_elements())) 
print(v.remove(25))
print("after rem " + str(v.get_elements())) 