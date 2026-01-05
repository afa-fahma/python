def disply_info(a, *args, **kwargs):
    print("positional arguments:", a)
    print("positional arguments:", args)
    print("keyword arguments:",kwargs)
disply_info(1,2,3, name="afa", age=20)    

