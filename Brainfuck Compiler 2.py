class nie:
    def __init__(self):
        self.tab = ["+","-",">",'<',".",",","[","]"]
        self.indeks = [0] * 10000
        self.Indeks = 0
    def funkcja(self):
        text = input()
        i = 0
        while i < len(text):
            mark = text[i]
            if not mark in self.tab: mark = ""
            elif mark == "+":   self.indeks[self.Indeks] += 1
            elif mark == "-": self.indeks[self.Indeks] -= 1
            elif mark == ">": self.Indeks += 1
            elif mark == "<": self.Indeks -= 1
            elif mark == ",": self.indeks[self.Indeks] += input()
            elif mark == ".": print(chr(self.indeks[self.Indeks]), end="")
            elif mark == "[": 
                if self.indeks[self.Indeks] == 0:
                    while text[i] != "]":
                        i += 1
            elif mark == "]": 
                if self.indeks[self.Indeks] != 0:
                    while text[i] != "[":
                        i -= 1
            i += 1
n = nie()
n.funkcja()