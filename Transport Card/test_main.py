#!/usr/bin/env python
# coding: utf-8
#
#

import unittest
import main

# Definición:
# TDD: Test-driven development is a software development process relying on software 
# requirements being converted to test cases before software is fully developed, and 
# tracking all software development by repeatedly testing the software against all test cases

VALID_NAME = 'Julius Brown'
VALID_ID = 65546508
VALID_INITIAL_BALANCE = 0.00

class TestTrips(unittest.TestCase):
    def testBusTrip(self):
        """
        Test bus trip
        """
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        c.passInBarrier(transport='bus')
        self.assertEqual(c.balance, round(initialBalance - main.Card.BUS_TICKET, 2))

    def testMetroTripOneZoneOutside1(self):
        """
        Test metro trip / one zone trip / outside zone 1 / Cost = 2.00
        """

        expectedCost = 2.00
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Callao')
        c.passExitBarrier(station='Atocha')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))

    def testMetroTripOneZoneInside1(self):
        """
        Test trip in metro / one zone trip / inside zone 1 / Cost = 2.50
        """

        expectedCost = 2.50
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Retiro')
        c.passExitBarrier(station='Atocha')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))

    def testMetroTripTwoZonesInclude1(self):
        """
        Test trip in metro / two zones trip / include zone 1 / Cost = 3.00
        """

        expectedCost = 3.00
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Barajas')
        c.passExitBarrier(station='Retiro')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))

    def testMetroTripTwoZonesExclude1(self):
        """
        Test trip in metro / two zones trip / exclude zone 1 / Cost = 2.25
        """

        expectedCost = 2.25
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Barajas')
        c.passExitBarrier(station='Callao')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))

    def testMetroTripThreeZones(self):
        """
        Test trip in metro / three zones trip / Cost = 3.20
        """

        expectedCost = 3.20
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Barajas')
        c.passExitBarrier(station='Atocha')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))

    def testNoClosedTrip(self):
        """
        Test no closed trip / Cost: 3.20 + Other trip cost = 3.20 + 2.00 = 5.20
        """

        expectedCost = 5.20
        initialBalance = 100
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)

        c.passInBarrier(transport='metro', station='Retiro')
        c.passInBarrier(transport='metro', station='Callao')
        c.passExitBarrier(station='Atocha')
        self.assertEqual(c.balance, round(initialBalance - expectedCost, 2))


class TestAddCredit(unittest.TestCase):
    def testPositiveValueStartingFromZero(self):
        """
        Test adding positive credit to the card
        """
        initialBalance = 0
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testPositiveDecimalValueStartingFromZero(self):
        """
        ...
        """
        initialBalance = 0
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10.3
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testPositiveValueStartingFromNegative(self):
        """
        ...
        """
        initialBalance = -10
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testPositiveDecimalValueStartingFromNegative(self):
        """
        ...
        """
        initialBalance = -10
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10.3
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testPositiveValueStartingFromNegativeDecimal(self):
        """
        ..
        """
        initialBalance = -10.78
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testPositiveDecimalValueStartingFromNegativeDecimal(self):
        """
        ...
        """
        initialBalance = -10.78
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = 10.3
        c.addCredit(balanceToAdd)
        self.assertEqual(c.balance, round(balanceToAdd + initialBalance, 2))

    def testNegativeValueStartingFromZero(self):
        """
        Check error report trying to add a negative balance to the card
        """
        initialBalance = 0
        c = main.Card(name=VALID_NAME, id=VALID_ID, initialBalance=initialBalance)
        balanceToAdd = -10

        # 3 different ways to check Raises:
        # 1.
        self.assertRaises(ValueError, c.addCredit, balanceToAdd)
        # 2.
        with self.assertRaises(ValueError):
            c.addCredit(balanceToAdd)
        # 3.
        self.assertRaises(ValueError, lambda: c.addCredit(balanceToAdd))


if __name__ == '__main__':
    unittest.main()