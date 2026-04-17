"""
  Estructura que contiene la información a guardar en una ``nodo`` de un árbol binario
"""


def new_node(key, value):
    """
    Crea una nueva entrada (de tipo :ref:`bst_node<bst-node>`) de un árbol binario con una llave y un valor dados.

    Se crea un nodo con los siguientes atributos:
    - **key**: Llave del nodo
    - **value**: Valor del nodo
    - **size**: Tamaño del nodo. Inicializado en 1
    - **left**: Hijo izquierdo del nodo. Inicializado en ``None``
    - **right**: Hijo derecho del nodo. Inicializado en ``None``
    - **type**: Tipo de árbol. Inicializado en "BST"

    :param key: Llave del nodo
    :type key: any
    :param value: Valor del nodo
    :type value: any

    :returns: Nodo creado
    :rtype: bst_node
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "type": "BST",
    }
    return node


def get_value(my_node):
    """
    Obtiene el valor ``value`` de un nodo recibido.

    :param my_node: El nodo con la iformación
    :type my_node: bst_node

    :returns: El valor almacenado en el nodo
    :rtype: any
    """
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    """
    Obtiene la llave ``key`` de un nodo recibido.

    :param my_node: El nodo con la información
    :type my_node: bst_node

    :returns: La llave almacenada en el nodo
    :rtype: any
    """
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key

def insert_node(root, key, value):
    if root is None:
        return new_node(key, value)
    
    if key < root['key']:
        root['left'] = insert_node(root['left'], key, value)
    
    elif key > root['key']:
        root['right'] = insert_node(root['right'], key, value)
    
    else:
        root['value'] = value
    
    left_size = root['left']['size'] if root['left'] is not None else 0
    right_size = root['right']['size'] if root['right'] is not None else 0
    root['size'] = 1 + left_size + right_size
    
    return root
    
def get_node(root, key):
    if root is None:
        return None
    
    if key < root['key']:
        return get_node(root['left'], key)
        
    elif key > root['key']:
        return get_node(root['right'], key)
        
    else: 
        return root   

def size_tree(root):
    
    if root is None:
        return 0
    
    return root['size']

def height_tree(root):
    if root is None:
        return -1
    
    left_h = height_tree(root['left'])
    right_h = height_tree(root['right'])
    
    return 1 + max(left_h, right_h)

def get_min_node(root):
    if root is None:
        return None
    
    if root['left'] is None:
        return root
    
    return get_min_node(root['left'])

def get_max_node(root):
    if root is None:
        return None
    
    if root['right'] is None:
        return root
    
    return get_max_node(root['right'])

def delete_min_tree(root):
    if root is None:
        return None
    
    if root['left'] is None:
        return root['right']
    
    root['left'] = delete_min_tree(root['left'])
    
    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size
    
    return root

def delete_max_tree(root):
    if root is None:
        return None
    
    if root['right'] is None:
        return root['left']
    
    root['right'] = delete_max_tree(root['right'])
    
    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size
    
    return root

def key_set_tree(root, result):
    if root is None:
        return
    
    key_set_tree(root['left'], result)
    result.append(root['key'])
    key_set_tree(root['right'], result)
    
def value_set_tree(root, result):
    if root is None:
        return
    
    value_set_tree(root['left'], result)
    result.append(root['value'])
    value_set_tree(root['right'], result)
    
def keys_range(root, result, low, high):
    if root is None:
        return
    
    if low < root['key']:
        keys_range(root['left'], result, low, high)
    
    if low <= root['key'] <= high:
        result.append(root['key'])
    
    if high > root['key']:
        keys_range(root['right'], result, low, high)

def values_range(root, result, low, high):
    if root is None:
        return
    
    if low < root['key']:
        values_range(root['left'], result, low, high)
    
    if low <= root['key'] <= high:
        result.append(root['value'])
    
    if high > root['key']:
        values_range(root['right'], result, low, high)