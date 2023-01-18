class binary_tree:
    def __init__(self, key):   #function to insert data to our binary tree
        self.leftchild = None #setting leftchild of the tree to add items
        self.rightchild = None #setting rightchild of the tree to add items
        self.key = key
    class binary_tree:
        def __init__(self): #generate a tree to hold values 
            self.root = None
    #this is the end 
    
    def add(self, value): #function to add data items to the tree
        if self.key is None:
            self.key = data #begin adding elements to the binary tree
            return
        if self.key == value:   # this will take care for duplicate nodes
            return              
        if value < self.key:  #if value of the key node is more than the leftchild accept values
            if self.leftchild:
                self.leftchild.add(value) #set values to the leftchild of the tree
            else:   
                self.leftchild = binary_tree(value)
        else:   #values are more than the key value
            if self.rightchild:     #if on the rigghtchild of the tree
                self.rightchild.add(value)  #set values to rightchild
            else:
                self.rightchild = binary_tree(value) #values cannot be less then the root key
        ##End of search of our binary tree
        
    def search(self, value):
        if self.key == value:     #check if value is equal to the key val
            print("The node is present")
            return
        if value < self.key:    #Here left subtree can be empty or it can contain one or more nodes
            if self.leftchild:   #this condition is true if left subtree exists
                self.leftchild.search(value)
            else:
                print("The node is empty in the tree!")
        else:
            if self.rightchild:
                self.rightchild.search(value)   #search for all the values in the rightchild
                return True
            else:   
                print("The node is empty in the tree!") 

root = binary_tree(50)    # 50 is our root key and our object is root
elements = {20,56,3,4,7,10,17,20}   #adds values to the tree 
for i in elements:
    root.add(i)     #recursively adds values in the tree
root.search(10)
root.search(2)