class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur.next:
            if cur.data == data:
                return cur
            cur = cur.next
        
        return None
    
    def reverse(self):
        cur = self.head
        prev, next = None, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def sortList(self):
        list_of_nodes = []
        current = self.head
        while current:
            list_of_nodes.append(current.data)
            current = current.next
        return list_to_llist(merge_sort(list_of_nodes))
    
    def merge_llists(self, llist):
        current = self.head
        while current.next:
            current = current.next
        current.next = llist.head
        return self.sortList()
    
    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end='')
            current = current.next
        print('')

def list_to_llist(list):
    llist = LinkedList()
    for elem in list:
        llist.insert_at_end(elem)
    return llist

def merge_sort(list_of_nodes):
    if list_of_nodes:
        if len(list_of_nodes) <= 1:
            return list_of_nodes
        mid = len(list_of_nodes) // 2
        left = list_of_nodes[:mid]
        right = list_of_nodes[mid:]

        return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

llist.reverse()
print("Зв'язний список реверсований:")
llist.print_list()

llist = llist.sortList()
print("Зв'язний список відсортований:")
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_end(40)
llist2.insert_at_end(7)
print("Об'єднання двох зв'язних списків:")
llist = llist.merge_llists(llist2)
llist.print_list()
