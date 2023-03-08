class Stack(object):
    def __init__(self, size):
        self.__stackList = []
        self.__size = size
        self.__top = -1

    def push(self, item):
        if self.isFull():
            raise Exception('Stack overflow')
        else:
            self.__stackList.append(item)
            self.__top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack underflow')
        else:
            self.__top -= 1
            return self.__stackList.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__stackList[-1]

    def isEmpty(self):
        return self.__top == -1

    def isFull(self):
        return self.__top == self.__size - 1
    
    def __len__(self): # Return # of items on stack
        return self.__top + 1
    
    def __str__(self): # Convert stack to string
        ans = "[" # Start with left bracket
        for i in range(self.__top + 1): # Loop through current items
            if len(ans) > 1: # Except next to left bracket, 
                ans += ", " # separate items with comma
            ans += str(self.__stackList[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans
