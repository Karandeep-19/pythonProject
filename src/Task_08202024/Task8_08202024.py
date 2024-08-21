s1 = float(input("Enter 1st side of the triangle: "))
s2 = float(input("Enter 2nd side of the triangle: "))
s3 = float(input("Enter 3rd side of the triangle: "))

if s1==s2 and s2==s3 and s3==s1:
    print("All Sides are equal")
elif (s1==s2) or (s2==s3) or (s1==s3):
    print("Two sides are equal")
else:
    print("No sides are equal")

