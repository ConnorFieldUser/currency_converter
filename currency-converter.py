

currencies = {'usd': 1, 'jpy': 100.38, 'eur': 0.89, 'xbt': 0.0017, 'dd': 0.0000000000001}


class Money:

    def __init__(self, symbol, value):
        self.value = value
        self.symbol = symbol

    def convert_to_usd(self):
            # print("usd_version:")
            return self.value / currencies[self.symbol]
            # return currencies(self.value) / Money(self.value)

    def __add__(self, other):
        print("added")
        added = self.convert_to_usd() + other.convert_to_usd()
        return added
        # return Money("usd", (self.value + other.value))
        # return Money('usd', self.value + other.value)

    def __sub__(self, other):
        print("subtracted")
        subtracted = self.convert_to_usd() + other.convert_to_usd()
        return subtracted

    def __mul__(self, other):
        print("multiplied")
        multiplied = self.convert_to_usd() * other.convert_to_usd()
        return multiplied

    def __eq__(self, other):
        print("is equal:")
        is_equal = self.convert_to_usd() == other.convert_to_usd()
        return is_equal

    def __ne__(self, other):
        print("is not equal:")
        is_not_equal = self.convert_to_usd() != other.convert_to_usd()
        return is_not_equal

    def __lt__(self, other):
        print("is less than:")
        less_than = self.convert_to_usd() < other.convert_to_usd()
        return less_than

    def __gt__(self, other):
        print("is greater than:")
        greater_than = self.convert_to_usd() > other.convert_to_usd()
        return greater_than

    def __le__(self, other):
        print("is less than or equal to:")
        less_than = self.convert_to_usd() <= other.convert_to_usd()
        return less_than

    def __ge__(self, other):
        print("is greater than or equal to:")
        greater_than = self.convert_to_usd() >= other.convert_to_usd()
        return greater_than

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
