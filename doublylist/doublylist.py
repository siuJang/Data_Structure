class DoublyList:

    # Node 클래스
    class Node:
        def __init__(self, data=None):
            self.lnext = None
            self.data = data
            self.rnext = None

    ## doublelinked 클래스 정의
    def __init__(self):
        self.head = None
        self.tail = None

     ## Head, Taile Node 생성
    def create_ht(self):
        if self.head is not None:
           return print("Head-Node already exists...")

        self.head = self.Node()
        self.tail = self.Node()
        return print("Successfully!!! Created HEAD, TAIL NODE")

    ### 마지막 위치에 Node 추가
    def node_append(self, data):
        if self.head is None:
           return 99, "Error : Head Node is not Create..."

        # current = self.head
        # while current.next is not None:
        #     current = current.next
        current = self.tail

        newNode = self.Node(data)
        ## if self.tail.lnext == None
        if self.head.rnext == None:   ### 첫번째 데이터인 경우
            self.head.rnext = newNode
            self.tail.lnext = newNode
            newNode.lnext = self.head
            newNode.rnext = self.tail
        else:
            newNode.lnext = self.tail.lnext
            newNode.rnext = self.taile.lnext.rnext
            self.tail.lnext.rnext = newNode
            self.tail.lnext = newNode

        return 100, "Successfully, appended data!!"

     ### Which data insert
    # def node_insert(self, data, insertData):
    #     if self.head is None:
    #         print("Error : Head Node is not Create...")
    #         return
    #
    #     current = self.head
    #     while current.next is not None:
    #         current = current.next
    #         if current.data == data:
    #             newNode = self.Node(insertData)
    #             newNode.next = current.next
    #             current.next = newNode
    #             return 100, "Successfully, Inserted data!!"
    #
    #     return 99, "Warning: not Found Data"

    ### Head ~ Last node Print
    def order_print(self):
        current = self.head
        if current.next is None:
            return 99, "Warning: Data Empty...."

        print("In-Order Data List")
        while current.next is not None:
            if current.data is not None:
                print(current.data, end=" >> ")
            current = current.next

        print("[None]")

    #역방향
    def reverse_print(self):
        current = self.tail
        if current.lnext is None:
            print("Warning: Data Empty....")
            return

        print("Reverse Data List")
        while current is not None:
            if current.data is not None:
                print(current.data, end = " >> ")
            current = current.lnext

        print("[None]")