from . import bst_node as bst

def put(my_bst, key, value):
    my_bst['root'] = bst.insert_node(my_bst['root'], key, value)
    my_bst['size'] = bst.size_tree(my_bst['root'])
    return my_bst
    
def get(my_bst, key):
    node = bst.get_node(my_bst['root'], key)
    return None if node is None else node['value']

def size(my_bst):
    return bst.size_tree(my_bst['root'])

def contains(tree, key):
    return get(tree, key) is not None

def is_empty(tree):
    return tree["size"] == 0

def key_set(tree):
    result = []
    bst.key_set_tree(tree["root"], result)
    return result
    
def value_set(tree):
    result = []
    bst.value_set_tree(tree["root"], result)
    return result
    
def get_min(tree):
    node = bst.get_min_node(tree["root"])
    return None if node is None else node["key"]


def get_max(tree):
    node = bst.get_max_node(tree["root"])
    return None if node is None else node["key"]


def delete_min(tree):
    if tree["root"] is not None:
        tree["root"] = bst.delete_min_tree(tree["root"])
        tree["size"] -= 1

def delete_max(tree):
    if tree["root"] is not None:
        tree["root"] = bst.delete_max_tree(tree["root"])
        tree["size"] -= 1
        
def height(tree):
    return bst.height_tree(tree["root"])

def keys(tree, low, high):
    result = []
    bst.keys_range(tree["root"], result, low, high)
    return result

def values(tree, low, high):
    result = []
    bst.values_range(tree["root"], result, low, high)
    return result