try:
    try:
        raise KeyError("Hello!")
    except Exception as e:
        raise RuntimeError("World!")
except Exception as e2:
    print(e2, (type(e2.__context__), e2.__context__), (type(e2.__cause__), e2.__cause__))
