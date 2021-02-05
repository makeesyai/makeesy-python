# Package: is a directory with collection of modules and __init__.py.

# Add resources in __init__.py
# 3.3+ there is no need to have __init__.py to make a dir package

# import p1.module
# CALL: p1.module.func()
# from p1.p2 import module
# CALL module.func()
# from p1.p2.module import func
# CALL: func()
# from p1.p2.module import func as f
# CALL: f()
