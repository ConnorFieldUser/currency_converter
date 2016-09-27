

currencies = {'usd': 1, 'jpy': 100.38, 'eur': 0.89, 'xbt': 0.0017, 'dd': 0.0000000000001}


class Money:

    def __init__(self, symbol, value):
        self.value = value
        self.symbol = symbol

    def convert_to_usd(self):
            print("usd_version:")
            return self.value / currencies[self.symbol]
            # return currencies(self.value) / Money(self.value)

    def __add__(self, other):
        print("added")
        # return Money("usd", (self.value + other.value))
        return Money('usd', self.value + other.value)

    # def __str__(self):
    #     return "converted value" + self.value
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


jpy = Money('jpy', 300)
# jpy = jpy.convert_to_usd()
print(jpy)

usd = Money('usd', 1)
# usd = usd.convert_to_usd()
print(usd)

print("added")
print(jpy + usd)

# print(dd + xbt)