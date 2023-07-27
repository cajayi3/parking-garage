tickets = [10, 23, 14, 18, 12]
parkingSpaces = ['3a', '4b', '7f', '8h', '3e']
currentTicket = { 15.00:"Paid", 0.00:"Not Paid"}

class ParkingGarage:

    def __init__(self, tickets: int = 5):
        self.tickets = [i for i in range (tickets)]
        self.parkingSpaces = [i for i in range(tickets)]
        self.currentTicket = {}
        self.PayforParking = []
        
    def takeTicket(self):
        ticket_number = self.tickets.pop()
        parking_number = self.parkingSpaces.pop()
        self.active_tickets.insert(0,"ticket"+ str(ticket_number))
        self.currentTicket["ticket"+ str(ticket_number)] = 'Occupied'
        print(f"Your ticket number is {ticket_number}, your parking number is {parking_number} ")
      
    def PayforParking(self):
        parkingLot = input("Need to make a Payment?:")
        if len(parkingLot) >= 1:
            return (f"{self.ticket} has been Paid, you have 15 minutes to exist:")
        else:
            while len(parkingLot) < 1:
                parkingLot = input("Please make a current payment of 15 dollars:")

    def leaveGarage(self):
        if self.currentTicket["ticket"+str(len(self.tickets))] == "Paid":
            print("Thank you, have a marvelous day!:")
            self.tickets.append(len(self.tickets))
            self.parkingSpaces.append(len(self.parkingSpaces))

if __name__ == '__main__':
    customer1 = ParkingGarage(15.00, 'Troy', 'Robinson', '12', '4b')
    customer2 = ParkingGarage(15.00, 'Michael','Thompson', '10', '8h')
    customer3 = ParkingGarage(0.00, 'Monica', 'Jones', '14', '7f')

