class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        if len(self.items) > 0:
            return False
        else:
            return True   

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

   

queue1 = Queue()
queue1.enqueue("thing")
queue1.enqueue("thingymabob")
queue1.enqueue("item thing")
queue1.enqueue("bag of items")
queue1.enqueue("stuff")

print(queue1.items)
print("Removed", queue1.dequeue(), "from the front of the list")
print(queue1.items)
print("Removed", queue1.dequeue(), "from the front of the list")
print(queue1.items)
print("Removed", queue1.dequeue(), "from the front of the list")
print(queue1.items)
print("Removed", queue1.dequeue(), "from the front of the list")
print(queue1.items)
print("Removed", queue1.dequeue(), "from the front of the list")