class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self , name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(4)

people = ["Han Tun Zaw", "May Kyi Nue","Lone Lone ", "Thel Tone ly","Sayar Gyi"]
for person in people:
             if flight.add_passenger(person):
                 print(f"The Person {person} is sucessful")
             else:
                 print(f"The Person {person} Cannot be add ")
