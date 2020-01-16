x=0
def outher():
    x=1
    def inther():
        nonlocal x
        x=2
        print("inther:",x)
    inther()
    print("outher:",x)
    outher()
    print("global:",x)