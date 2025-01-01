def find_modified_max_argmax(l, f):
    l = [f(i) for i in l if type(i) == int]
    return (m := max(l), l.index(m)) if l else ()