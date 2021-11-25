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
        tally += randint(1, X)
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


    def emitOutcome(self, demesneYear):
        """
        Base class method to return the content of the outcome.
        :return: Ultimately, should return a string.
        """
        demesneYear.storyElements.append(self.outcome)
        return self
    
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
                return False
        
        # Are we over the upperBound
        if self.upperBound:
            if self.upperBound < targetNumber:
                return False
            
        return True

class randomTableEntryMoney(randomTableEntry):
    def __init__(self, lowerBound, upperBound, outcome, costAdjustment):
        randomTableEntry.__init__(self, lowerBound, upperBound, outcome)
        self.costAdjustment = 0

    def emitOutcome(self, demesneYear):
        randomTableEntry.emitOutcome(self, demesneYear)
        demesneYear.AdjustCashFlow(self.costAdjustment)
        return self

class randomTableEntryFate(randomTableEntry):
    def __init__(self, lowerBound, upperBound, outcome, nDice, die, modifier):
        randomTableEntry.__init__(self, lowerBound, upperBound, outcome)
        self.nDice = nDice
        self.die = die
        self.modifier = modifier

    def emitOutcome(self, demesneYear):
        fate = nDX(self.nDice, self.die, self.modifier)
        self.outcome += " (%d)"%(fate)
        randomTableEntry.emitOutcome(self, demesneYear)
        demesneYear.AdjustFate(fate)
        return self

class randomTableEntryStewardship(randomTableEntry):
    def __init__(self, lowerBound, upperBound, outcome, delta):
        randomTableEntry.__init__(self, lowerBound, upperBound, outcome)
        self.deltaStewardship = delta

    def emitOutcome(self, demesneYear):
        randomTableEntry.emitOutcome(self, demesneYear)
        if self.deltaStewardship is None:
            demesneYear.stewardshipEpiphany = True
        else:
            demesneYear.stewardshipDelta += self.deltaStewardship
        return self
    
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

    def AddOutcome(self, newEntry):
        """
        Add an entry to the table when building it.
        :param newEntry:
        :return:
        """
        self.outcomes.append(newEntry)
        
    def RollDice(self, modifier = 0):
        """
        Roll the correct random dice roll for this table
        :param modifier: 
        :return: an integer
        """
        return nDX(self.numberOfDice, self.sidedness, modifier)
    
    def Roll(self, demesneYear, modifer = 0):
        """
        Roll against the table
        :param modifer: 
        :return: 
        """
        # Generate a dice roll
        diceOutcome = self.RollDice(modifer)
        
        # Scan outcomes
        for outcomeObject in self.outcomes:
            if outcomeObject.TestTarget(diceOutcome):
                return outcomeObject.emitOutcome(demesneYear)
