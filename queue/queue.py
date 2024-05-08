class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.rear = None
        self.front = None
        pass

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        if self.rear is None and self.front is None:
            newNode = self.Node(data)
            self.rear = newNode
            self.front = newNode
        else:
            newNode = self.Node(data)
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.rear is None and self.front is None:
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data
    def peek(self):
        if self.rear is None and self.front is None:
            return None
        else:
            return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def queue_print(self):
        current = self.front
        prt_str = "front => "
        while current is not None:
            prt_str += str(current.data) + " => "
            current = current.next
        prt_str += "rear"
        return prt_str


q = Queue()
print("Queue is empty:",q.is_empty()) # 큐에 넣기전이라 empty는 True
q.enqueue(1) # 큐에 1 넣기
q.enqueue(2) # 큐에 2 넣기
q.enqueue(3) # 큐에 3 넣기
print("Queue is empty:",q.is_empty()) # 큐에 넣은 후라 empty는 False
print("Size:", q.size())  # 입력수 3이므로 3출력
print("Peek:", q.peek())  # 1을 삭제하지않고 1반환
print("All data:", q.queue_print())  # 출력: 1,2,3
print("Dequeue:", q.dequeue())  # 1을 삭제하고 1반환
print("Size:", q.size())  # dequeue로 1이 삭제됫으므로 사이즈는 2
print("Peek:", q.peek())  # dequeue로 1이 삭제됫으므로 1다음에 입력한 2삭제하지않고 출력
print("All data:", q.queue_print())  # dequeue로 1이 삭제됫으므로 출력: 2,3