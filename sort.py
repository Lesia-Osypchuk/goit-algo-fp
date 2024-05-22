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

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

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
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

     # Функція сортування вставками для однозв'язного списку
    def insertion_sort(self):
        sorted_head = None  # Початково відсортований список порожній
        current = self.head  # Поточний вузол, який треба вставити у відсортований список

        while current:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            sorted_head = self.sorted_insert(sorted_head, current)  # Вставляємо поточний вузол у відсортований список
            current = next_node  # Переходимо до наступного вузла

        self.head = sorted_head  # Оновлюємо голову списку

    # Допоміжна функція для вставки вузла у відсортований список
    def sorted_insert(self, head, node):
        if head is None or head.data >= node.data:
            node.next = head
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            return head


    # Функція для отримання середини списку
    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Функція злиття двох відсортованих списків
    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    # Функція сортування списку злиттям
    def merge_sorted_lists(self, other):
        result = LinkedList()  # створюємо новий список для результату
        result_head = None
        current1 = self.head
        current2 = other.head

        # базовий випадок: один зі списків пустий
        if current1 is None:
            return other
        if current2 is None:
            return self

        # визначаємо початок результату
        if current1.data <= current2.data:
            result_head = current1
            current1 = current1.next
        else:
            result_head = current2
            current2 = current2.next

        # починаємо злиття списків
        current = result_head
        while current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        # додаємо залишок першого списку
        if current1 is not None:
            current.next = current1

        # додаємо залишок другого списку
        if current2 is not None:
            current.next = current2

        result.head = result_head
        return result

# Демонстрація
llist1 = LinkedList()
llist1.insert_at_end(10)
llist1.insert_at_beginning(30)
llist1.insert_at_end(50)

llist2 = LinkedList()
llist2.insert_at_beginning(20)
llist2.insert_at_end(40)
llist2.insert_at_end(60)

# Реверсування списку
print("Список перед реверсуванням:")
llist1.print_list()
llist1.reverse()
print("Список після реверсування:")
llist1.print_list()

# Сортування списку
llist3 = LinkedList()
llist3.insert_at_end(3)
llist3.insert_at_beginning(1)
llist3.insert_at_end(2)
llist3.insert_at_beginning(5)
llist3.insert_at_end(4)
print("Список перед сортуванням:")
llist3.print_list()
llist3.insertion_sort()
print("Список після сортування:")
llist3.print_list()

# Об'єднання двох відсортованих списків
merged_list = llist1.merge_sorted_lists(llist2)
merged_list.insertion_sort()  # Сортуємо об'єднаний список
print("Об'єднаний відсортований список:")
merged_list.print_list()
