import copyreg


def copyright(func):
    def new_func():
        print("@ copyright by jaekwanee")
        func()

    return new_func


@copyright
def smile():
    print("^.^")


"""
def smile():
    print("!.!")

smile = copyright(smile)
"""


@copyright
def angry():
    print("!.!")


@copyright
def love():
    print("*.*")


smile()
