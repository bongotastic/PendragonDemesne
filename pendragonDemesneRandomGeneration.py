from random import randint
from typing import List, Any


def nDX(n, X, modifier=0):
    """
    General purpose dice roller
    :param n: number of dice
    :param X: sidedness of die
    :param modifier: modifier to roll
    :return: a random outcome as an integer
    """
    tally = modifier
    for i in range(n):
        tally += randint(1, X + 1)
    return tally

def nD6(n=1, modifier=0):
    """
    Convenience function to roll a D6
    :param n: Number of dice, defaults to 1
    :param modifier: defaults to 0
    :return: a random outcome
    """
    return nDX(n, 6, modifier)

def D20(modifier):
    """
    Convenience function to roll a single D20
    :param modifier:
    :return:
    """
    return nDX(1, 20, modifier)

class randomTableEntry:
    def __init__(self, lowerBound = None, upperBound = None, outcome = None):
        # Lowest possible value (inclusive)
        self.lowerBound = lowerBound
        
        # Highest possible value (includive)
        self.upperBound = upperBound
        
        # Returned outcome
        self.outcome = outcome

    def emitOutcome(self):
        """
        Base class method to return the content of the outcome.
        :return: Ultimately, should return a string.
        """
        return self.outcome
    
    def TestTarget(self, targetNumber):
        """
        Consider a target number and determine if it is falling in its range. If so, returns the outcome. Otherwise, 
        returns None
        :param targetNumber: 
        :return: None or an outcome.
        """
        # Are we under the lowerBound? 
        if self.lowerBound is not None:
            if self.lowerBound > targetNumber:
                return None
        
        # Are we over the upperBound
        if self.upperBound:
            if self.upperBound > targetNumber:
                return None
            
        return self.emitOutcome()
    
class randomTable:
    """
    General purpose table that has the flexibility to handle all random generation table.
    """
    numberOfDice: int
    outcomes: List[randomTableEntry]

    def __init__(self, tableName, nDice, sidedness):
        
        # Table name
        self.tableName = tableName
        
        # table dice definition
        self.numberOfDice = nDice
        
        # Sidedness
        self.sidedness = sidedness
        
        # Collection of outcomes
        self.outcomes = []
        
    def RollDice(self, modifier = 0):
        """
        Roll the correct random dice roll for this table
        :param modifier: 
        :return: an integer
        """
        return nDX(self.numberOfDice, self.sidedness, modifier)
    
    def Roll(self, modifer = 0):
        """
        Roll against the table
        :param modifer: 
        :return: 
        """
        # Generate a dice roll
        diceOutcome = self.RollDice(modifer)
        
        # Scan outcomes
        for outcomeObject in self.outcomes:
            outcome = outcomeObject.TestTarget(diceOutcome)
            if outcome is not None:
                return outcome
        
        return None