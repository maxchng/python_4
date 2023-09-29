def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print out statistics"""
    if len(args) == 0:
        for item in kwargs:
            print("ERROR")
        return
    for item in args:
        if isinstance(item, str):
            return
    mean = sum(args) / len(args)
    median = sorted(args)[len(args) // 2]
    percentile_25 = 25 / 100 * len(args)
    percentile_75 = 75 / 100 * len(args)
    quartile = [sorted(args)[int(percentile_25)],
                sorted(args)[int(percentile_75)]]
    quartile = [float(num) for num in quartile]
    if kwargs.get("toto") is not None:
        print(f"{kwargs['toto']} : {mean}")
    if kwargs.get("tutu") is not None:
        print(f"{kwargs['tutu']} : {median}")
    if kwargs.get("tata") is not None:
        print(f"{kwargs['tata']} : {quartile}")

    var = sum(((item - mean) ** 2 for item in sorted(args)))
    var = var / len(args)
    std = var ** 0.5
    if kwargs.get("hello") is not None:
        print(f"{kwargs['hello']} : {std}")
    if kwargs.get("world") is not None:
        print(f"{kwargs['world']} : {var}")
