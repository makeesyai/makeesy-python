# Package: a directory with collection of modules and __init__.py.
# import p1.p2.module
# CALL: p1.p2.module.func()
# from p1.p2 import module
# CALL module.func()
# from p1.p2.module import func
# CALL: func()
# from p1.p2.module import func as f
# CALL: f()