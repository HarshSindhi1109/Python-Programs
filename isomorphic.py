def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):
        if c1 in mapping_s_t and mapping_s_t[c1] != c2:
            return False
        
        if c2 in mapping_t_s and mapping_t_s[c2] != c1:
            return False
        
        mapping_s_t[c1] = c2
        mapping_t_s[c2] = c1

    return True

s1, t1 = "egg", "add"
print(is_isomorphic(s1, t1))