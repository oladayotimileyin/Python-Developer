class SuperList(list):
    def __init__(self):
        print(1000)

SuperList1 = SuperList()

print(len(SuperList1))
SuperList1.append(5)

print(SuperList1[0])

print(issubclass(SuperList, list))