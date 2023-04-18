text1 = input()
text2 = input()
text3 = input()

if "зайка" in text1:
    sl = len(text1)
    text = text1
if ("зайка" in text2) and (len(text2) < sl):
    sl = len(text2)
    text = text2
if "зайка" in text3 and (len(text3) < sl):
    sl = len(text3)
    text = text3

print(text + " " + str(sl))
