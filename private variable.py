class team1:
    __privatevariable = 67;
    def __privatemethod(self):
        print("im in team 1")
    def hello(self):
        print("private variable value: ", team1.__privatevariable)
foo = team1()
foo.hello()
foo.__privatemethod