class CircleList:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.next = None
            self.data = data

    ## doublelinked 클래스 정의
    def __init__(self):
        self.head = None

     ## Head, Taile Node 생성
    def create_node(self):
        if self.head is not None:
           return print("Head-Node already exists...")

        self.head = self.Node()
        return print("Successfully!!! Created HEAD, TAIL NODE")

    ### 마지막 위치에 Node 추가
    def node_append(self, data):
        if self.head is None:
           return 99, "Error : Head Node is not Create..."

        current = self.head
        last = self.head

        while True:
            current = current.next
            if current == None:
                newNode = self.Node(data)
                self.head.next = newNode
                newNode.next = newNode
                return 100, "Successfully, appended data!!"

            if current.next == last.next:
                break

        newNode = self.Node(data)
        newNode.next = current.next
        current.next = newNode

        return 100, "Successfully, appended data!!"


    def all_print(self):
        current = self.head
        last = self.head
        if current.next is None:
            print("Warning: Data Empty....")
            return

        print("All Data List")
        while True:
            current = current.next
            print(current.data, end=" >> ")
            if current.next == last.next:
                break

        print("[None]")