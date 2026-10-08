sentence=input("Enter a sentence: ")
charcaters=len(sentence)
words=len(sentence.split())
vowels=0
spaces=0
digits=0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch==" ":
        spaces+=1
    elif ch.isdigit():
        digits+=1

print("Characters: ",charcaters)
print("words: ",words)
print("vowels: ",vowels)
print("spaces: ",spaces)
print("Digits: ",digits)


    
    