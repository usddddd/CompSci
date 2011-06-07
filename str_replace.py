def replace(s, old, new):
    s_without_old = s.split(old)
    s_with_new = new.join(s_without_old)
    return s_with_new
