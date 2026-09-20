class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructer called")


def create_obj():
    print("making object")
    obj = Employee()
    print("funtion end")
    return obj

print("Calling create obj funtion")
obj = create_obj()
