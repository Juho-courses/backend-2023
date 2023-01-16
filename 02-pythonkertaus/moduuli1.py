def func1():
    print('moduuli 1 func 1')


class Viiva:
    luku: int

    def __init__(self, luku) -> None:
        self.luku = luku

    def tulostaLuku(self) -> None:
        print(self.luku)

    def palautaLuku(self) -> int:
        return self.luku


v1 = Viiva(123)
v1.tulostaLuku()
print(v1.palautaLuku() * 2)
