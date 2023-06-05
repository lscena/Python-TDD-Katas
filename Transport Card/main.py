#!/usr/bin/env python
# coding: utf-8
#
#

# Functions:
def hasNumbers(text):
    return any(char.isdigit() for char in text)


def isIntNumber(text):
    text = str(text)
    return text.isdigit()


def isFloatNumber(text):
    text = str(text)
    try:
        float(text)
        return True
    except:
        return False


class Card:
    MAXIMUM_FARE = 3.20
    BUS_TICKET = 1.80

    METRO_STATIONS = [
        "Retiro",
        "Atocha",
        "Barajas",
        "Callao",
    ]
    METRO_STATIONS_ZONES = {
        "Retiro":[1],
        "Atocha":[1, 2],
        "Barajas":[3],
        "Callao":[2],
    }

    # Create the card
    def __init__(self, name, initialBalance, id) -> None:
        self.name = name # calls the setter
        self.balance = initialBalance # calls the setter
        self.id = id # calls the setter
        self.__lastInStation = None

    # add credit to the card
    def addCredit(self, creditToAdd):
        creditToAdd = self.validEURAmount(creditToAdd, positive=True)
        self.balance = self.__balance + creditToAdd

    # Card passed through an in barrier at the station:
    def passInBarrier(self, transport, station=None):
        # Bus trip:
        if transport == 'bus':
            # charge bus ticket:
            self.balance = self.__balance - self.BUS_TICKET
            return
        # Metro trip:
        else:
            if transport != 'metro':
                raise ValueError('Invalid transport type')
            if station not in self.METRO_STATIONS:
                raise ValueError('Invalid station')
            if self.__balance < self.MAXIMUM_FARE:
                raise ValueError('Insufficient Credit.')
            # charge metro ticket:
            self.balance = self.__balance - self.MAXIMUM_FARE
            self.__lastInStation = station

    # Card passed through an exit barrier at the station:
    def passExitBarrier(self, station):
        if station not in self.METRO_STATIONS:
            raise ValueError('Invalid station')

        # calculate the cost of the trip:
        tripCost = self.calculateMetroTripCost(
            stationIn=self.__lastInStation,
            stationExit=station,
        )

        # return the difference respect the max fare:
        self.balance = self.__balance + (self.MAXIMUM_FARE - tripCost)

        # reset last in station:
        self.__lastInStation = None

    # getters:
    @property
    def name(self):
        return self.__name
    @property
    def balance(self):
        return self.__balance
    @property
    def id(self):
        return self.__id

    # Str return:
    def __str__(self) -> str:
        return f'Card ID: {self.__id} belonging to {self.__name} has a balance of {self.__balance} EUR'

    # setters:
    @name.setter
    def name(self, name):
        name = name.strip()
        if len(name) <= 3:
            raise ValueError('Invalid Name')
        if hasNumbers(name):
            raise ValueError('Invalid Name')
        # Valid name:
        self.__name = name

    @balance.setter
    def balance(self, balance):
        self.__balance = self.validEURAmount(balance)

    @id.setter
    def id(self, id):
        if not isIntNumber(id):
            raise ValueError('Invalid Id')
        # Valid id:
        self.__id = int(id)

    @staticmethod
    def validEURAmount(credit, positive=False):
        if not isFloatNumber(credit):
            raise ValueError('Invalid EUR amount')
        # Valid balance:
        # transform to float:
        credit = float(credit)        
        if positive:
            if credit < 0:
                raise ValueError('Invalid EUR amount')  

        # Change format:
        # format to 2 decimals:
        credit = "%0.2f" % credit
        # transform again to float:
        credit = float(credit)  

        # return EUR value
        return credit

    @classmethod
    def calculateMetroTripCost(cls, stationIn, stationExit):
        zonesIn = cls.METRO_STATIONS_ZONES[stationIn]
        zonesExit = cls.METRO_STATIONS_ZONES[stationExit]

        # common zones:
        commonZones = list(set(zonesIn) & set(zonesExit))
        if commonZones:
            tripZones = commonZones
        else:
            tripZones = zonesIn + zonesExit
            # remove duplicastes:
            tripZones = list(set(tripZones))

        # quantity of zones traveled in:
        qZones = len(tripZones)

        # for debugging:
        # print(tripZones)

        # trip in one zone, outside zone 1:
        if qZones == 1 and 1 not in tripZones:
            return 2.0 # trip cost

        # trip in any two zones excluding zone 1 
        if qZones == 2 and 1 not in tripZones:
            return 2.25 # cost

        # trip inside zone 1 (both, in and exit should be in zone 1 // some stations have more than one zone)
        if qZones == 1 and 1 in tripZones:
            return 2.50 # cost

        # trip in Any two zones including zone 1 
        if qZones == 2 and 1 in tripZones:
            return 3.00 # cost

        # trip in Any three zones
        if qZones == 3:
            return 3.20 # cost

        raise ValueError('Invalid trip.')


if __name__ == '__main__':
    # initiate the card
    c1 = Card(
        name='Julius Brown',
        id='65546508',
        initialBalance=0,
    )

    # add 30 EUR of credit:
    c1.addCredit(30.0)
    # check initial balance
    print(c1)

    # Make some trips:
    # 1. Tube Retiro to Atocha
    c1.passInBarrier(transport='metro', station='Retiro')
    c1.passExitBarrier(station='Atocha')
    # 2. 27 bus from "Atocha" to "Puerto Chico".
    c1.passInBarrier(transport='bus')
    # 3. Tube Atocha to Callao
    c1.passInBarrier(transport='metro', station='Atocha')
    c1.passExitBarrier(station='Callao')

    # check final balance
    print(c1)