class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
    
class linked_list:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def insert_at(self,index,data):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begin(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1

    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head=self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        
        itr=self.head

        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

l1 = linked_list()
l1.insert_at_begin(1)
l1.insert_at(1,2)
l1.insert_at(2,3)
l1.insert_at_end(4)
print("length:",l1.get_length())
l1.print()

