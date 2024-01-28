class X:
    def __repr__(self):
        return "X"
    
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div)) else repr(self.p2)
        return left + " * " + right
    

    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    

    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return left + " / " + right
    

    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)

    

# poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
# poly = Add(X(), Int(10))
# poly = Add(Int(-2), Int(7))
# poly = Sub(Int(4), Int(9))
# poly = Sub(X(), Int(5))
# poly = Mul(Int(0), Int(5))
# poly = Mul(X(), Int(3))
# poly = Div(Int(9), Int(1))
# poly = Div(X(), Int(4))

# print(poly)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))