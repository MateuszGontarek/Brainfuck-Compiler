tab = ["+","-",">",'<',".",",","[","]"]
indeks = [0] * 10000
Indeks = 0
text = input()
i = 0
while i < len(text):
    mark = text[i]
    if not mark in self.tab: mark = ""
    elif mark == "+": indeks[Indeks] += 1
    elif mark == "-": indeks[Indeks] -= 1
    elif mark == ">": Indeks += 1
    elif mark == "<": Indeks -= 1
    elif mark == ",": indeks[Indeks] += input()
    elif mark == ".": print(chr(indeks[Indeks]), end="")
    elif mark == "[": 
        if indeks[Indeks] == 0:
            while text[i] != "]":
                i += 1
    elif mark == "]": 
        if indeks[Indeks] != 0:
            while text[i] != "[":
                i -= 1
    i += 1
