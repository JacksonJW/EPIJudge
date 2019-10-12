import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    node0_ptr, node1_ptr = node0, node1
    node0_set, node1_set = set(), set()

    while node0_ptr or node1_ptr:
        if node0_ptr is node1_ptr:
            return node0_ptr
        elif node0_ptr and node0_ptr in node1_set:
            return node0_ptr
        elif node1_ptr and node1_ptr in node0_set:
            return node1_ptr
        else:
            if node0_ptr and node0_ptr not in node0_set:
                node0_set.add(node0_ptr)
            if node1_ptr and node1_ptr not in node1_set:
                node1_set.add(node1_ptr)
            if node0_ptr.parent:
                node0_ptr = node0_ptr.parent
            if node1_ptr.parent:
                node1_ptr = node1_ptr.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
