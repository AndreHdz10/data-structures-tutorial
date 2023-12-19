# Stack Problem Solution

def reverse_string(input_string):
    stack = []
    # Push each character onto the stack
    for char in input_string:
        stack.append(char)

    reversed_string = ''
    # Pop each character from the stack to reverse the string
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Example usage:
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "!dlroW ,olleH"


# Linked List Problem Solution


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def find_middle(head):
    # Initialize two pointers, 'slow' and 'fast', both pointing to the head of the linked list
    slow = fast = head

    # Traverse the linked list using 'fast' pointer moving two steps at a time and 'slow' moving one step at a time
    while fast and fast.next:
        slow = slow.next  # Move 'slow' one step forward
        fast = fast.next.next  # Move 'fast' two steps forward

    # 'slow' pointer will be at the middle node when 'fast' reaches the end of the list
    return slow  # Return the node(s) at the middle of the linked list


# Tree Problem Solution


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Function to find all nodes at a given level in a tree


def nodes_at_level(root, level):
    # List to store nodes at the given level
    nodes_at_given_level = []

    # Helper function to traverse the tree nodes at a specific level
    def traverse(node, current_level):
        # Base case: If node is None, return
        if not node:
            return

        # If the current level matches the given level, add the node to the list
        if current_level == level:
            nodes_at_given_level.append(node.value)
        # Recursively traverse children nodes, increasing the level by 1
        else:
            for child in node.children:
                traverse(child, current_level + 1)

    # Start traversing the tree from the root at level 1
    traverse(root, 1)

    # Return the list of nodes at the given level
    return nodes_at_given_level


# Example tree creation
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6)]

# Find nodes at level 2 in the example tree
nodes_level_2 = nodes_at_level(root, 2)
print("Nodes at level 2:", nodes_level_2)
