

currencies = {'usd': 1, 'jpy': 100.38, 'eur': 0.89, 'xbt': 0.0017, 'dd': 0.0000000000001}


class Money:

    def __init__(self, symbol, value):
        self.value = value
        self.symbol = symbol

    def convert_to_usd(self):
            return self.value / currencies[self.symbol]

    def __add__(self, other):
        print("added")
        return self.convert_to_usd() + other.convert_to_usd()

    def __sub__(self, other):
        print("subtracted")
        return self.convert_to_usd() + other.convert_to_usd()

    def __mul__(self, other):
        print("multiplied")
        return self.convert_to_usd() * other.convert_to_usd()

    def __eq__(self, other):
        print("is equal:")
        # is_equal = self.convert_to_usd() == other.convert_to_usd()
        # return is_equal
        return self.convert_to_usd() == other.convert_to_usd()

    def __ne__(self, other):
        print("is not equal:")
        return self.convert_to_usd() != other.convert_to_usd()

    def __lt__(self, other):
        print("is less than:")
        less_than = self.convert_to_usd() < other.convert_to_usd()
        return less_than

    def __gt__(self, other):
        print("is greater than:")
        return self.convert_to_usd() > other.convert_to_usd()

    def __le__(self, other):
        print("is less than or equal to:")
        return self.convert_to_usd() <= other.convert_to_usd()

    def __ge__(self, other):
        print("is greater than or equal to:")
        return self.convert_to_usd() >= other.convert_to_usd()

    def __str__(self):
        return "converted value: " + "NOOOOOOO"

# ge,>= gt,> le,<= lt,< add+ sub- eq,== ne,!= mul*

#
# usd = ("$", 1)
#
# jpy = ("€", 0.89)
#
# eur = ("¥", 1.3)
#
# xbt = ("Ƀ", 0.0017)
#
# dd = (":p", 0.0000)

# $
# €
# €
# Ƀ


jpy = Money('jpy', 100)
# jpy = jpy.convert_to_usd()
print(jpy.value)

usd = Money('usd', 1)
# usd = usd.convert_to_usd()

dd = Money('dd', 999999)

eur = Money('eur', 10)

print(usd.value)

print(jpy + usd)

print(usd - dd)

print(usd * eur)

print(usd == usd)

# print(dd + xbt)
