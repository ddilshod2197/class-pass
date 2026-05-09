class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 2

class C(A):
    def __init__(self):
        super().__init__()
        self.c = 3

class D(B, C):
    def __init__(self):
        super().__init__()

    def get_values(self):
        return self.a, self.b, self.c

d = D()
print(d.get_values())
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Klasslarni yaratib, ularning atributlarini belgilab bo'ling.
2. Klass D ni yaratib, unga B va C klasslaridan meros olishni kiritib bo'ling.
3. Klass D ning __init__ metodi orqali B va C klasslarining __init__ metodlarini chaqiring.
4. Klass D ga get_values metodi qo'shib, unga A klassining a, B klassining b va C klassining c atributlarini qaytarib bo'ling.
5. Klass D ning ob'ekti yaratib, get_values metodi orqali atributlarni konsolga chiqarib bo'ling.
