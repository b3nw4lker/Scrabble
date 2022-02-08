class Buttons:

    def __init__(self, height, width):
        pass
        # attributes that make a button. e.g. size, colour


class SwapButton(Buttons):

    def __init__(self, height, width):
        super().__init__(height, width)
    #     Super means we instantiate the parent class using the arguments passed to the child's
    #     class constructor (__init__)

    def some_other_swap_stuff(self):
        pass