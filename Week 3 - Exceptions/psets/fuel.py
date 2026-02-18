while(True):
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if x < 0 or x > y:
            raise ValueError 
        
        result = (x / y) * 100

        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{round(result)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass