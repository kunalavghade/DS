# node stucture
class node:
    def __init__(self,rs,name):
        self.rs = rs
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def createNode(self,rs,name):
        new = node(rs,name)
        if(self.head==None):
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail = self.tail.next

    def remove(self,key):
        tmp = self.head
        if(tmp != None):
            if(tmp.name == key):
                self.head = tmp.next 
                tmp=None
                return

        while(tmp != None):
            if(tmp.name == key):
                break
            prev = tmp
            tmp=tmp.next

        if(tmp==None): 
            return

        prev.next=tmp.next
        tmp=None

    def get_list(self):
        arr = []
        tmp = self.head 
        while(tmp != None):
            col=[]
            col.append(int(tmp.rs))
            col.append(tmp.name)
            arr.append(col)
            tmp=tmp.next
        return arr

