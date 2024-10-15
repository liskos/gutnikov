def f(x):
    while "01" in x or "02" in x or "03" in x:
        if "01" in x:
            x = x.replace("01", "30", 1)
        elif "02" in x:
            x = x.replace("02", "3103", 1)
        else:
            x = x.replace("03", "1201", 1)
        return x


