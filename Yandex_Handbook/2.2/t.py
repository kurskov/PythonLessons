text1 = input()
text2 = input()
text3 = input()

text = ""
sl = len(text)

if "зайка" in text1:
    sl = len(text1)
    text = text1

if "зайка" in text2:
    if sl == 0 or text2 < text:
        sl = len(text2)
        text = text2
    
if "зайка" in text3:
    if sl == 0 or text3 < text:
        sl = len(text3)
        text = text3

print(text, str(sl))
