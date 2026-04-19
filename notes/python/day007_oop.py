# s = "Hello World Python"
# #Reverse the string
# print("Reversed string:", s[::-1])
# #Count how many times l appears
# print("Count of 'l':", s.count('l'))
# #Replace World with your name
# s = s.replace("World", "Alice")
# print("Modified string:", s)
# #Split into list of words
# words = s.split()
# print("List of words:", words)
# #Check if string starts with Hello
# print("Starts with 'Hello':", s.startswith("Hello"))

def fibonnaci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonnaci(n-1) + fibonnaci(n-2)

print("Fibonacci of 5:", fibonnaci(5))