def lca(root, v1, v2):

    #aseguramos que v1 es menor que v2
    v3 = 0
    if v1 > v2:
        v3 = v2
        v2 = v1
        v1 = v3
    
    if root is None:
        return None
        
    #viajar por el árbol
    while True:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root