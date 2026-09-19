class Animal:
    def __init__(self, name, species="animal", sound="hi"):
        self.name=name
        self.species=species
        self.sound=sound

    def speak(self):
        return (f"{self.name}, a {self.species}, says {self.sound}!")

    def __repr__(self):
        return (f"Animal({self.name}, {self.species}, {self.sound})")


class Dog(Animal):
    def __init__(self, name, species="animal", sound="hi", is_good_boy=True):
        super().__init__(name, species, sound)
        self.species="dog"
        self.sound="ruff"
        self.is_good_boy=is_good_boy

    def __repr__(self):
        return f"Dog({self.name})"


class Cat(Animal):
    def __repr__(self):
        return f"Cat({self.name}, {self.species}, {self.sound})"

    