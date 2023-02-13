class Array(object):
    def __init__(self, initialSize):
        # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially

    def __len__(self):
        # Special def for len() func
        return self.__nItems # Return number of items

    def get(self, n):
        # Return the value at index n
        if 0 <= n and n < self.__nItems:
            # Check if n is in bounds, and
            return self.__a[n] # only return item if in bounds

    def set(self, n, value):
        # Set the value at index n
        if 0 <= n and n < self.__nItems:
            # Check if n is in bounds, and
            self.__a[n] = value # only set item if in bounds

    def swap(self, j, k):
        # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and # Check if indices are in bounds, before processing
            0 <= k and k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        # Insert item at end
        if self.__nItems >= len(self.__a):
            # If array is full, raise exception
            raise Exception("Array overflow")
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items

    def find(self, item):
        # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found, then return index to element
                return j
        return -1 # Not found -> return -1

    def search(self, item):
        # Search for item and return item if found
        return self.get(self.find(item))

    def delete(self, item):
        # Delete first occurrence of an item
        for j in range(self.__nItems): # of an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from right over 1
                    self.__a[k] = self.__a[k+1]
                return True # Return success flag
        return False # Made it here, so couldn't find the item

    def traverse(self, function=print):
        # Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        # Special def for str() func
        ans = "[" # Surround with square brackets
        for i in range(self.__nItems): # Loop through items
            if len(ans) > 1: # Except next to left bracket, separate items with comma
                ans += ", "
            ans += str(self.__a[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans

    def bubbleSort(self): # Sort comparing adjacent vals
        for last in range(self.__nItems-1, 0, -1): # and bubble up
            for inner in range(last): # inner loop goes up to last
                if self.__a[inner] > self.__a[inner+1]: # If elem less than adjacent value, swap
                    self.swap(inner, inner+1)

    def selectionSort(self): # Sort by selecting min and swapping min to leftmost
        for outer in range(self.__nItems-1):
            min = outer # Assume min is leftmost
            for inner in range(outer+1, self.__nItems): # Hunt to right
                if self.__a[inner] < self.__a[min]: # If we find new min, update the min index
                    min = inner # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min) # Swap leftmost and min

    def insertionSort(self): # Sort by repeated inserts
        for outer in range(1, self.__nItems): # Mark one element
            temp = self.__a[outer] # Store marked elem in temp
            inner = outer # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner-1]: # If marked elem smaller, then shift elem to right
                self.__a[inner] = self.__a[inner-1]
                inner -= 1
            self.__a[inner] = temp # Move marked elem to 'hole'

    def dualbubbleSort(self):
        for i in range(self.__nItems):
            for j in range(i, self.__nItems-i-1):
                if self.__a[j] > self.__a[j+1]:
                    self.swap(j, j+1)
            for j in range(self.__nItems-i-2, i-1, -1):
                if self.__a[j] < self.__a[j-1]:
                    self.swap(j, j-1)

    def median(self):
        if self.__nItems % 2 == 0:
            # average of middle two elements for even number of elements
            return (self.__a[self.__nItems//2-1] + self.__a[self.__nItems//2]) / 2
        else:
            # middle element for odd number of elements
            return self.__a[self.__nItems//2]

    def deduplicate(self):
        # create a dictionary to store the frequency of each element
        freq = {}
        for i in range(self.__nItems):
            if self.__a[i] not in freq:
                freq[self.__a[i]] = 1
            else:
                freq[self.__a[i]] += 1
        # create a new list with unique elements
        unique_list = []
        for i in range(self.__nItems):
            if freq[self.__a[i]] == 1:
                unique_list.append(self.__a[i])
                freq[self.__a[i]] = 0
        # set the new list as the array and update the number of items
        self.__a = unique_list
        self.__nItems = len(unique_list)


    def oddEvenSort(self):
        n = self.__nItems
        sorted = False
        while not sorted:
            sorted = True
            # Odd-Even phase: compare elements with odd/even indices
            for i in range(1, n-1, 2):
                if self.__a[i] > self.__a[i+1]:
                    self.swap(i, i+1)
                    sorted = False
            # Even-Odd phase: compare elements with even/odd indices
            for i in range(0, n-1, 2):
                if self.__a[i] > self.__a[i+1]:
                    self.swap(i, i+1)
                    sorted = False

    def swap(self, i, j):
        temp = self.__a[i]
        self.__a[i] = self.__a[j]
        self.__a[j] = temp



    
    def insertionSortcounter(self):
        dupli = 0
        for outer in range(1, self.__nItems):
            temp = self.__a[outer]
            inner = outer
            while inner > 0 and temp < self.__a[inner-1]:
                self.__a[inner] = self.__a[inner-1]
                inner -= 1
            self.__a[inner] = temp
            if inner > 0 and temp == self.__a[inner-1]:
                dupli += 1
        print("Numero de duplicados: ",dupli)




    def insertionSortAndDedupe(self):

        for outer in range(1, self.__nItems):
            temp = self.__a[outer]
            inner = outer
            while inner > 0 and self.__a[inner-1] > temp:
                inner -= 1
            # Check for duplicates
            for i in range(outer, inner, -1):
                if self.__a[i-1] == temp:
                    temp = None
                    break
            self.__a[inner+1:outer+1] = self.__a[inner:outer]
            self.__a[inner] = temp
        # Remove None values
        self.__a = list(filter(None, self.__a))
        self.__nItems = len(self.__a)
        unique_items = [] # lista auxiliar para almacenar elementos únicos
        for i in range(1, self.__nItems):
            key_item = self.__a[i]
            # si el elemento no está en la lista auxiliar, insertarlo en la lista ordenada y en la lista auxiliar
            if key_item not in unique_items:
                j = i - 1
                while j >= 0 and self.__a[j] > key_item:
                    self.__a[j+1] = self.__a[j]
                    j -= 1
                self.__a[j+1] = key_item
                unique_items.append(key_item) # agregar elemento a la lista auxiliar
        self.__nItems = len(unique_items) # actualizar el número de elementos en el array
        self.__a = unique_items # reemplazar el array original con la lista de elementos únicos

