class SingleList:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    # SigleList 클래스 정의
    def __init__(self):
        self.head = None

     ## Head Node 생성
    def create_head(self):
        if self.head is not None:
            return print("Head Node already exists...")

        self.head = self.Node()
        return print("Successfully!!! Created HEAD_NODE")

    ### 마지막 위치에 Node 추가
    def node_append(self, data=None):
        if self.head is None:
            return print("Error : Head Node is not Create...")

        current = self.head
        while current.next is not None:
            current = current.next

        newNode = self.Node(data)
        current.next = newNode
        return print("Succesfully, appended data!!")

    ### Which data insert
    def node_insert(self, data, insertData):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.next is not None:
            current = current.next
            if current.data == data:
                newNode = self.Node(insertData)
                newNode.next = current.next
                current.next = newNode
                return 100, "Succesfully, inserted data!!"

        return 99, "Warning : not Found Data"

    ### Head ~ Last node Print
    def all_print(self):
        current = self.head
        if current.next is None:
            print("Warning: Data Empty....")
            return

        print("All Data List")
        while current.next is not None:
            current = current.next
            print(current.data, end = " >> ")

        print("[None]")

    def node_modifi(self, data, insertData):
        if self.head is None:
            print("Error : Head Node is not Create...")
            return

        current = self.head
        while current.next is not None:
            current = current.next
            if current.data == data:
                newNode = self.Node(insertData)
                newNode.next = current.next
                current.data = newNode.data
                return

        print("Warning : not Found Data")

    def node_del(self, data):
        if self.head is None:
            print("Error : Head Node is not Created...")
            return
        current = self.head
        while current is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Warning : not Found Data")
    def node_find(self, data):
        if self.head is None:
            print("Error : Head Node is not Created...")
            return
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                print("position is", position)
            current = current.next
            position +=1