#Name Lists
name = ["Han Tun Zaw" , "May Kyi Nue", "Lone Lone" ,"Thel Tone ly"]
name.append("Chee pay")
name.sort()
print(name)

#Number Lists
number = [60,59,48,20,54,54]
number.append(100)
number.count(100)
number.sort()
print(number)

#set Example

h = set()

h.add("Han Tun Zaw")
h.add(1)
h.add(20)
h.add(50)
h.add(60)
h.add(70)
h.add("May Kyi Nue")
h.remove("Han Tun Zaw")
print(h)
print(f"Here Is The Length Of H {len(h)}")

#looping
for i in [0,1,2,3,4,5,6,7,8]:
    print(i)

#dic

apple = {"Iphone":"Iphone 11 Pro Max", "Ipad":"Ipad Air ", "MAC":"Macbook Pro (2020"}
apple = {"Iversion":"IOS 14 Version"}
print(apple["Iversion"])

#functions 

def square (x):
    return x * x