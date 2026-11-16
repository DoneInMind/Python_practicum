class E(Exception):
    pass

class F(E):
    pass

class G(F):
    pass

for exc in (E, F, G, None, IndexError):
    try:
        if (exc):
            raise exc
    except E:
        print(E)
    except F:
        print(F)
    except G:
        print(G)
    except Exception as Exc:
        print("!!!", Exc.args)
