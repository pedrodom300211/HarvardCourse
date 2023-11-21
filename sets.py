#Create an empty set
s=set()
#Set can save the same number it can only appear once
#add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)
print(s)
s.remove(2)
print(s)
print(f"Elements in set: {len(s)}")