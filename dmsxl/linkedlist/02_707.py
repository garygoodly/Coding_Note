class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0     

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size == 0:
            self.head = self.tail = ListNode(val)
        else:
            self.head = ListNode(val, self.head)
        self.size += 1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size == 0:
            self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        
        self.size += 1
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        curr.next = ListNode(val, curr.next)
        return
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size or self.size == 0:
            return
        elif index == 0:
            self.deleteAtHead()
            return
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        if index == self.size - 1:
            self.tail = curr
        self.size -= 1
        return
    
    def deleteAtHead(self):
        self.head = self.head.next
        if self.size == 1:
            self.tail = None
        self.size -= 1
        return
    
    def print(self):
        if self.size == 0:
            print("Empty LinkedList")
            return
        print(f"Head: {self.head.val}, {self.head}")
        print(f"Tail: {self.tail.val}, {self.tail}")
        print(f"size: {self.size}")
        curr = self.head
        while (curr != None):
            print(curr.val, end = " ")
            curr = curr.next
        print()
        return
    
if __name__ == "__main__":
    # commands = ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
    # arguments = [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

    # commands = ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
    # arguments = [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]

    # commands = ["MyLinkedList","addAtHead","addAtIndex","addAtIndex","addAtHead","deleteAtIndex","addAtIndex","addAtHead","addAtTail","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtHead","addAtTail","addAtHead","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","get","addAtIndex","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtIndex","get","addAtTail","get","addAtTail","deleteAtIndex","get","addAtTail","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtHead","deleteAtIndex","addAtTail","addAtIndex","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","addAtTail","get","addAtHead","addAtTail","addAtHead","addAtHead"]
    # arguments = [[],[86],[1,54],[1,14],[83],[4],[3,18],[46],[3],[76],[5],[79],[74],[7,28],[68],[16],[82],[24],[30],[96],[21],[79],[66],[2],[2],[7,57],[59],[21],[19],[55],[46],[17],[16,41],[97],[85],[63],[30],[11],[16],[91],[29],[47],[20],[12],[80],[15],[12,8],[21],[30],[11],[54],[51],[41],[8,88],[62],[7],[59],[73],[73],[55],[9],[7],[49],[99],[17],[44],[11],[26,86],[10,99],[19],[71],[29],[32],[2],[3],[16],[2],[83],[31],[3],[23],[64],[96],[27],[81],[12,78],[21],[69],[5,35],[8,72],[60],[19,73],[55],[83],[86],[31,70],[49],[19],[64],[22],[25],[13]]

    commands = ["MyLinkedList","addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]
    arguments = [[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]


    obj = None
    results = []

    for cmd, args in zip(commands, arguments):
        print(f"{cmd}, {args}")
        if cmd == "MyLinkedList":
            obj = MyLinkedList()
            results.append(None)
            obj.print()
        elif cmd == "addAtHead":
            obj.addAtHead(*args)
            results.append(None)
            obj.print()
        elif cmd == "addAtTail":
            obj.addAtTail(*args)
            results.append(None)
            obj.print()
        elif cmd == "addAtIndex":
            obj.addAtIndex(*args)
            results.append(None)
            obj.print()
        elif cmd == "deleteAtIndex":
            obj.deleteAtIndex(*args)
            results.append(None)
            obj.print()
        elif cmd == "get":
            result = obj.get(*args)
            results.append(result)
            print(f"Get: {result}")
            obj.print()

    print("Results:", results)
