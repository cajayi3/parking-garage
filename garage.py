class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate
        

class ParkingLot:
    def __init__(self, row, lane, level, car):
        self.row = row
        self.lane = lane
        self.level = level
        self.car = car

    def Available(self):
        self.car = None
    def park(self, vehicle):
        self.car = vehicle

    def removeVehicle(self):
        self.car = None

class Level:
    def __init__(self, rows, levelNumber):
        self.levelNumber = levelNumber
        self.rows =rows
        self.lotPerRow = 2
        self.parkingLot = []
        self.available = rows * self.lotsPerRow
    
    def findAvailableLot(self):
        if self.AvailableLot <= 0:
            return None
        else:
            if(len(self.parkingLot) == 0):
                return ParkingLot(0,0,0,None)
            else:
                lastCarParked = self.parkingLot[-1]
            if(lastCarParked.LotNumber<self.lotPerRow):
                return ParkingLot(lastCarParked.row, lastCarParked.lotNumber+1,self.levelNumber,None)
            if(lastCarParked.row<self.rows):
                return ParkingLot(lastCarParked.row+1,0,self.levelNumber, None)
            
            def park(self, vehicle):
                freeParkingLot = self.findAvailableLot()
                if(not(freeParkingLot)):
                    return False
                    
                else:
                    freeParkingLot.park(vehicle)
                    self.parkingLot.park(vehicle)