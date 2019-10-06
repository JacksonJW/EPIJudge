from test_framework import generic_test


def inorder_traversal(tree):
    result = []
    if tree is None or tree.data is None:
        return result
    node_ptr = tree
    while True:
        while node_ptr.left and node_ptr.left.data is not None:
            node_ptr = node_ptr.left
        result.append(node_ptr.data)
        node_ptr.data = None
        if node_ptr.right and node_ptr.right.data is not None:
            node_ptr = node_ptr.right
            continue
        else:
            while node_ptr.parent and node_ptr.data is None:
                node_ptr = node_ptr.parent
            if node_ptr.data is not None:
                continue
            else:
                break
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
