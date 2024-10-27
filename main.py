class Currency:
    currencies = {
        'CHF': 0.930023,  # Swiss franc
        'CAD': 1.264553,  # Canadian dollar
        'GBP': 0.737414,  # British pound
        'JPY': 111.019919,  # Japanese yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0  # US dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __repr__(self):
        return f"Currency({self.value}, '{self.unit}')"

    def changeTo(self, new_unit):
        """Convert the currency value to a new unit."""
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(self.value + x, self.unit)

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        res = self + other
        if self.unit != "USD":
            res.changeTo("USD")
        return res

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        return self - other

    def __rsub__(self, other):
        res = other - self.value
        res = Currency(res, self.unit)
        if self.unit != "USD":
            res.changeTo("USD")
        return res

# Example usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)  # An int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3)  # An int or a float is considered to be a USD value
print(30 - v2)
