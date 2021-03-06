from collections import defaultdict
import math


def path_exists(graph, a, b, verbose=False):
    a.visited = True
    queue = [a]

    while queue:
        current = queue.pop(0)

        if verbose:
            print('----------', current.data, '----------')

        if current is b:
            return True

        for i in current.adjacent:
            node = graph.nodes[i]

            if not node.visited:

                if verbose:
                    print(node.data)

                node.visited = True
                queue.append(node)

    return False


def minimal_tree(arr, low, high):
    mid = (high + low) // 2

    if high < low:
        return

    print(arr[mid])
    minimal_tree(arr, low, mid - 1)
    minimal_tree(arr, mid + 1, high)


def level_lists(bst):
    levels = []
    current_level = [bst.root]

    while current_level:
        levels.append(current_level)
        parents = current_level
        current_level = []

        for parent in parents:
            if parent.left:
                current_level.append(parent.left)
            if parent.right:
                current_level.append(parent.right)

    return levels


def check_balance(root):
    if not root:
        return -1

    left_height = check_balance(root.left)
    if left_height == 'error':
        return 'error'
    left_height += 1

    right_height = check_balance(root.right)
    if right_height == 'error':
        return 'error'
    right_height += 1

    if abs(left_height - right_height) > 1:
        return 'error'

    return left_height + right_height


def validate_bst(root, prev=[None]):
    if not root:
        return True

    if not validate_bst(root.left, prev):
        return False

    if prev[0] and prev[0].data > root.data:
        return False

    prev[0] = root

    if not validate_bst(root.right, prev):
        return False

    return True


def successor(node, level=0):
    if not node:
        return None

    if not level:
        if node.right:
            return successor(node.right, level + 1)
        else:
            runner = node

            while(runner.parent):
                runner = runner.parent

                if runner.data > node.data:
                    return runner

            return None
    else:
        left = successor(node.left, level + 1)

        if left is not None:
            return left

        return node
        successor(node.right, level + 1)


def build_order(projects, dependencies):
    builds_remaining = len(projects)

    while builds_remaining:
        for (a, b) in dependencies:
            if b.status is type(b).BLANK and a not in b.adjacent:
                b.adjacent.add(a)
                a.incoming_edges += 1

        built_something = False
        for project in projects:
            if not project.incoming_edges and project.status is not type(project).COMPLETED:
                print(project)

                for dependent in project.adjacent:
                    dependent.incoming_edges -= 1

                project.status = type(project).COMPLETED
                builds_remaining -= 1
                built_something = True

        if not built_something:
            return False  # circular dependency!


def covers(node, target):
    if node is None:
        return False

    if node is target:
        return True

    return covers(node.left, target) or covers(node.right, target)


def get_sibling(node):
    if not node or not node.parent:
        return None

    return node.parent.left if node.parent.right is node else node.parent.right


def first_common_ancestor(root, a, b):
    if not covers(root, a) and not covers(root, b):
        return None
    elif covers(a, b):
        return a
    elif covers(b, a):
        return b

    sibling = get_sibling(a)
    parent = a.parent

    while not covers(sibling, b):
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent


def bst_sequences(levels, sequence=[]):
    if not levels:
        print(sequence)
        return

    for possible_sequence in levels[0]:
        sequence.append(possible_sequence)
        bst_sequences(levels[1:])
        sequence.pop()


def same_tree(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1.data != t2.data:
        return False

    return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)


def check_subtree(t1, t2):
    if not t1:
        return False

    if t1.data == t2.data:
        return same_tree(t1, t2)

    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)


def path_sums(root, target, sums=defaultdict(int), running_total=0):
    if root is None:
        return 0

    running_total += root.data
    sums[running_total] += 1
    count = sums[running_total - target]

    count += path_sums(root.left, target, sums, running_total)
    count += path_sums(root.right, target, sums, running_total)

    sums[running_total] -= 1
    
    return count
