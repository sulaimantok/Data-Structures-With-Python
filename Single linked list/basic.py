class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

#Deleting by value
    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

#Deleting by Position
    def delete_node_at_pos(self,pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

#Lenght or len Iterative
        def len_iterative(self):
            count = 0
            cur_node = self.head
            while cur_node:
                count += 1
                cur_node = cur_node.next
            return count

#Len Recursive
        def len_recursive(self,node):
            if node is None:
                None
            return 1 + self.len_recursive(node.next)

#Node Swap
        def swap_nodes(self,key_1,key_2):
            if key_1 == key_2:
                return

            prev_1 = None
            curr_1 = self.head
            while curr_1 and curr_1.data != key_1:
                prev_1 = curr_1
                curr_1 = curr_1.next

            prev_2 = None
            curr_2 = self.head
            while curr_2 and curr_2.data != key_2:
                prev_2 = curr_2
                curr_2 = curr_2.next

            if not curr_1 or not curr_2:
                return
            if prev_1:
                prev_1.next = curr_2
            else:
                self.head = curr_2

            if prev_2:
                prev_2.next = curr_1
            else:
                self.head = curr_1
            curr_1.next,curr_2.next = curr_2.next,curr_1.next

        def print_helper(self,node,name):
            if node is None:
                print(name + ": None")
            else:
                print(name + ":" + node.data)

        def reverse_iterative(self):

            prev = None
            cur = self.head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            self.head = prev

        def reverse_recursive(self):

            def _reverse_recursive(cur,prev):
                if not cur:
                    return prev

                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                return _reverse_recursive(cur,prev)
            self.head = _reverse_recursive(cur=self.head,prev=None)

#Two Merge Sorted
        def merge_sorted(self, llist):
            

                p = self.head 
                q = llist.head
                s = None
            

                if not p:
                    return q
                if not q:
                    return p
            if p and q:
                    if p.data <= q.data:
                        s = p 
                        p = s.next
                    else:
                        s = q
                        q = s.next
                    new_head = s 
                while p and q:
                    if p.data <= q.data:
                        s.next = p 
                        s = p 
                        p = s.next
                    else:
                        s.next = q
                        s = q
                        q = s.next
                if not p:
                    s.next = q 
                if not q:
                    s.next = p 
                return new_head

#Removing duplicate
        def remove_duplicates(self):
          cur = self.head
          prev = None
          dup_values = dict()

          while cur:
            if cur.data in dup_values:
              # Remove node:
              prev.next = cur.next
              cur = None
            else:
              # Have not encountered element before.
              dup_values[cur.data] = 1
              prev = cur
            cur = prev.next
#nth to Last node version 1
        def print_nth_from_last(self, n):
          total_len = self.len_iterative()
          
          cur = self.head 
          while cur:
            if total_len == n:
              print(cur.data)
              return cur.data
            total_len -= 1
            cur = cur.next
          if cur is None:
            return  

#nth to last node version 2
        def print_nth_from_last(self, n):
            p = self.head
            q = self.head

            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
                
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data

        def count_occurences_iterative(self, data):
          count = 0
          cur = self.head
          while cur:
              if cur.data == data:
                  count += 1
              cur = cur.next
          return count 

        def count_occurences_recursive(self, node, data):
          if not node:
              return 0 
          if node.data == data:
              return 1 + self.count_occurences_recursive(node.next, data)
          else:
              return self.count_occurences_recursive(node.next, data)
#Rotate
        def rotate(self,k):
            if self.head and self.head.next:
                p = self.head
                q = self.head
                prev = None
                count = 0

                while p and count < k:
                    prev = p
                    p = p.next
                    q = q.next
                    count += 1
                p = prev
                while q:
                    prev = q
                    q = q.next
                q = prev

                q.next = self.head
                self.head = p.next
                p.next = None