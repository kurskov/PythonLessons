s1 = float(input())
s2 = float(input())
s3 = float(input())

if ((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s2 + s3) > s1):
    print("YES")
else:
    print("NO") 
