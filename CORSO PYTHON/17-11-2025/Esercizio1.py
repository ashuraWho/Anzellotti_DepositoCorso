class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

x = float(input("\nInserisci l'ascissa (x) del punto di partenza: "))
y = float(input("\nInserisci l'ordinata (y) del punto di partenza: "))
p = Punto(x, y)

dx = float(input("\nInserisci di quanto vuoi spostarti lungo l'ascissa (dx): "))
dy = float(input("\nInserisci di quanto vuoi spostarti lungo l'ordinata (dy): "))
p.muovi(dx, dy)

print("\nIl punto di arrivo è: ", p.x, p.y)
print("\n", p.distanza_da_origine())