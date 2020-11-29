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