def thisIsDecorator(func):
    def executor():
        print("b4")
        func()
        print("after")
    return executor

def timer(func):
    from datetime import datetime

    class color:
        PURPLE = "\033[1;35;48m"
        CYAN = "\033[1;36;48m"
        BOLD = "\033[1;37;48m"
        BLUE = "\033[1;34;48m"
        GREEN = "\033[1;32;48m"
        YELLOW = "\033[1;33;48m"
        RED = "\033[1;31;48m"
        BLACK = "\033[1;30;48m"
        UNDERLINE = "\033[4;37;48m"
        END = "\033[1;37;0m"

    def executor(*args, **kwargs):
        print(color.BOLD + "\n-----------------------------------")
        print("Function name: " + func.__name__ + color.END)
        start = datetime.now()
        print("Started at ", start.time())
        print(color.GREEN + "Function: ", func.__name__, " output start\n" + color.END)
        result = func(*args, **kwargs)
        end = datetime.now()
        print(color.YELLOW + "\nFunction: ", func.__name__, " output end" + color.END)
        print("Ended at ", end.time())
        print(
            color.CYAN
            + "Time taken: "
            + str(end - start)
            + "\n-----------------------------------"
            + color.END
        )
        print()
        return result

    return executor

@thisIsDecorator
def thisIsFunction():
    print("this is function has a decorator.")

@timer
def thisIsTimed():
    print("This function is timed.")


if __name__ == "__main__":
    thisIsTimed()
