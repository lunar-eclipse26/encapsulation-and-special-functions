class OPPOSITION:
    def __init__(self, s=""):    
        self.s = s
    def reverse_text(self):
        return self.s[::-1]
word = input("Enter a word: ")
reverse = OPPOSITION(word)
print("Reversed string:", reverse.reverse_text())