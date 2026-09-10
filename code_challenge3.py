name = input("What is your name:  ")
Type_item = input("What is the item you wanted to buy:   ")
is_frag = input("input the fragile True/False:    ")
w = float(input("input the weight kg:   "))
d = float(input("input the distance  km:  "))
is_express = input("is it express True/False;   ")
is_international = input("is it international True/False? :  ")
base_cost = (w * 2.50) + (d * 0.15)

print("=======> Summary of the item <========")    
print("sender:", name)
print("Item:", Type_item)
print("weight:", w)
print("distance", d)
if is_express == "True":
    print("express: True")
else: 
    print("express: False")
if is_international == "True":
    print("international: True")
else:
    print("international: False")
if is_frag == "True":
    print("Fragile: True")
else:
    print("Fragile: False")
    
if w <= 2 and d <= 100 and not is_express and not is_international:
    print("Free shipping")
    print("the total cost; 0.00 $ \n")
elif is_express == "yes" and is_international == "yes":
    print("Shipping rate international express" )
    print("the total cost:", (base_cost * 1.40) + 50 )
elif is_express or (is_international and w > 20):
    print("shipping rate; Heavy Size")
    print("the total cost:", (base_cost * 1.20)+ 25 )
elif w > 30 or d > 1000: 
    print("shipping rate: Oversized")
    print("the total cost:", base_cost + 30 )
elif is_frag == True:
    print("the frag is true \n")
else:
    print("Shipping rate: Standard")
    print("the total cost:", base_cost)
    
