isa = True

while isa == True:
  isa = bool(input("Are you eligible True/False:   "))

  if isa == True:
    print("You are eligible")
    continue
  
  else:
    print("You are not eligible")
    break
