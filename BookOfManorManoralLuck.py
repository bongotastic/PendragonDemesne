from typing import Dict, Any

from pendragonDemesneRandomGeneration import randomTable, randomTableEntry, nDX


class rteCalamityLiegeVisit(randomTableEntry):
    def __init__(self, lowerBound, upperBound):
        randomTableEntry.__init__(self, 1,2, "Liege Lord Visit drains your funds.")

    def emitOutcome(self, demesneYear):
        demesneYear.storyElements.append(self.outcome)
        demesneYear.AddExpenses(6)

class rteCalamityFateAdjust(randomTableEntry):
    def __init__(self, lowerBound, upperBound, outcome, nDice, die, modifier):
        randomTableEntry.__init__(self, lowerBound, upperBound, outcome)
        self.nDice = nDice
        self.die = die
        self.modifier = modifier

    def emitOutcome(self, demesneYear):
        fate = nDX(self.nDice, self.die, self.modifier)
        self.outcome += " (%d)"%(fate)
        demesneYear.AdjustFate(fate)

class ManoralLuck:
    luckTables: Dict[int, randomTable]

    def __init__(self):
        # Tables indexed by upper year of use
        self.luckTables = {}
        self.calamityTable = randomTable("Calamity", 1, 20)
        self.benefitTable = randomTable("Benefit", 1, 20)
        self.BuildTables()


    def BuildTables(self):
        # Core tables
        table = randomTable("Luck 485-518", 1, 6)
        table.AddOutcome(randomTableEntry(1,3,"Calamity"))
        table.AddOutcome(randomTableEntry(4,5,"No result"))
        table.AddOutcome(randomTableEntry(6, 6, "Benefit"))
        self.luckTables[518] = table

        table = randomTable("Luck 519-539", 1, 6)
        table.AddOutcome(randomTableEntry(1, 2, "Calamity"))
        table.AddOutcome(randomTableEntry(3, 4, "No result"))
        table.AddOutcome(randomTableEntry(5, 6, "Benefit"))
        self.luckTables[539] = table

        table = randomTable("Luck 540-553", 1, 6)
        table.AddOutcome(randomTableEntry(1, 1, "Calamity"))
        table.AddOutcome(randomTableEntry(2, 3, "No result"))
        table.AddOutcome(randomTableEntry(4, 6, "Benefit"))
        self.luckTables[539] = table

        table = randomTable("Luck 554-557", 1, 6)
        table.AddOutcome(randomTableEntry(1, 3, "Calamity"))
        table.AddOutcome(randomTableEntry(4, 4, "No result"))
        table.AddOutcome(randomTableEntry(5, 6, "Benefit"))
        self.luckTables[539] = table

        table = randomTable("Luck 558-566", 1, 6)
        table.AddOutcome(randomTableEntry(1, 2, "Calamity"))
        table.AddOutcome(randomTableEntry(3, 4, "No result"))
        table.AddOutcome(randomTableEntry(5, 6, "Benefit"))
        self.luckTables[539] = table

        self.calamityTable.AddOutcome(rteCalamityLiegeVisit(1,2))
        self.calamityTable.AddOutcome(randomTableEntry(3,3, "Unusual dispute in course (Challenge 30)"))
        self.calamityTable.AddOutcome(rteCalamityFateAdjust(4,4, "Bandit raid!", 1, 6, -1))
        self.calamityTable.AddOutcome(randomTableEntry(5,20, "Hired Steward died."))

    def Compute(self, year, demesneYear):
        # Select at table
        if year <= 518:
            table = self.luckTables[518]
        elif year <= 539:
            table = self.luckTables[539]
        elif year <= 553:
            table = self.luckTables[553]
        elif year <= 557:
            table = self.luckTables[557]
        elif year <= 566:
            table = self.luckTables[566]

        table.Roll(demesneYear)
