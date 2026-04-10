from Tree import bst_node as bst

def put(my_bst, key, value):
    my_bst['root'] = bst.insert_node(my_bst['root'], key, value)
    return my_bst
    
def get(my_bst, key):
    return bst.get_node(my_bst['root'], key)

def size(my_bst):
    return bst.size_tree(my_bst['root'])