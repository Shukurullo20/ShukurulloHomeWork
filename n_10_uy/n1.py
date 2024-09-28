class x:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class re(x):
    def __init__(self, surname, position, salary, rt):
        super().__init__(surname, position, salary)
        self.rt = rt
xs = [
    re("Aliyev", "Muhandis", 50000, 65),
    re("Siddiqov", "Meneger", 60000, 80),
    re("Jalilov", "Dasturchi", 55000, 90),
    re("Rahimov", "Analitik", 52000, 75),
    re("Zokirov", "Moliya", 58000, 95)
]

for x in xs:
    if 60 <= x.rt < 75:
        x.salary *= 1.20
    elif 75 <= x.rt < 90:
        x.salary *= 1.40
    elif 90 <= x.rt <= 100:
        x.salary *= 1.60

for x in xs:
    print(f"Familiya: {x.surname}, Ishi: {x.position}, Oylik: {x.salary}, Reyting: {x.rt}")
