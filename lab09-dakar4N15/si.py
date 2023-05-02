class SimpleInteger:

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        return a * b

    def isequal(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        if a == b:
            return True
        else:
            return False

    def isgreaterthan(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        if a > b:
            return True
        else:
            return False
