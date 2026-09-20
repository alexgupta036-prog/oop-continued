class I0String:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = str(input("Enter a string value: "))
    def print_string(self):
        print(f"Result is {self.str1.upper()}")

object = I0String()
object.get_string()
object.print_string()