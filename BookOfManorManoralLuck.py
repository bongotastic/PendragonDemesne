from typing import Dict, Any

from pendragonDemesneRandomGeneration import randomTable, randomTableEntry, nDX, randomTableEntryFate, \
    randomTableEntryMoney, randomTableEntryStewardship


class ManoralLuck:
    luckTables: Dict[int, randomTable]

    def __init__(self):
        # Tables indexed by upper year of use
        self.luckTables = {}
        self.calamityTable = randomTable("Calamity", 1, 20)
        self.benefitTable = randomTable("Benefit", 1, 20)
        self.BuildTables()

        self.weather = 0


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

        self.calamityTable.AddOutcome(randomTableEntryMoney(1, 2, "Your liege visits and drains your funds.", -6))
        self.calamityTable.AddOutcome(randomTableEntry(3, 3, "Unusual dispute in course (Challenge 30)"))
        self.calamityTable.AddOutcome(randomTableEntryFate(4, 4, "Bandit raid!", 1, 6, -1))
        self.calamityTable.AddOutcome(randomTableEntry(5, 5, "Hired Steward died."))
        self.calamityTable.AddOutcome(randomTableEntryFate(6, 6, "A wandering faery curse the land.", 0, 0, 12))
        self.calamityTable.AddOutcome(randomTableEntryFate(7, 7, "Fabulous animal raid!.", 0, 0, 6)) # Subtable
        self.calamityTable.AddOutcome(randomTableEntryFate(8, 8, "Pestilence in the Manor", 0, 0, 5))
        self.calamityTable.AddOutcome(randomTableEntry(9, 15, "Property destruction")) # Subtable
        self.calamityTable.AddOutcome(randomTableEntry(16, 16, "Most important investment burns"))
        self.calamityTable.AddOutcome(randomTableEntryFate(17, 17, "Bad year for livestock.", 0, 0, 6))
        self.calamityTable.AddOutcome(randomTableEntry(18, 19, "Member of your retinue dies."))
        self.calamityTable.AddOutcome(randomTableEntryFate(20, 20, "Horrifying disease in the grain", 0, 0, 10))

        self.benefitTable.AddOutcome(randomTableEntryMoney(1,3, "Liege lord gives you favours", 2))
        self.benefitTable.AddOutcome(randomTableEntryMoney(4, 4, "Good year for the hunt", 1))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(5, 5, "Steward has an epiphany!", None))
        self.benefitTable.AddOutcome(randomTableEntryFate(6, 6, "Minor faery blessing", 0, 0, -2))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(7, 7, "Magical bull impregnates all cows.", 3))
        self.benefitTable.AddOutcome(randomTableEntryFate(8, 8, "Great year for peasants", 0, 0, -3))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(9, 9, "Great year for turnips!", 2))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(10, 10, "Great year for pigs!", 5))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(11, 11, "Great year for cows!", 4))
        self.benefitTable.AddOutcome(randomTableEntryStewardship(12, 12, "Great year for sheeps!", 3))
        self.benefitTable.AddOutcome(randomTableEntry(13, 13, "Wandering merchant sells rare tapestry for cheap."))
        self.benefitTable.AddOutcome(randomTableEntry(14, 15, "Excellent horse trained (extra)")) #subtable
        self.benefitTable.AddOutcome(randomTableEntryFate(16, 16, "Little crop pest this year", 0, 0, -2))
        self.benefitTable.AddOutcome(randomTableEntryMoney(17, 18, "Extra construction", 2))
        self.benefitTable.AddOutcome(randomTableEntryMoney(19, 19, "Boon in construction", 5))
        self.benefitTable.AddOutcome(randomTableEntry(20, 20, "New spring bring plenty of irrigation forever."))



    def GenerateWeather(self):
        self.weather = nDX(3,6, 5)

    def Compute(self, year, demesneYear):
        # Set weather
        demesneYear.misfortune = self.weather + demesneYear.demesne.baseFate

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

        outcome = table.Roll(demesneYear)

        if outcome.outcome == "Benefit":
            #outcome = self.benefitTable.Roll(demesneYear)
            pass
        elif outcome.outcome == "Calamity":
            outcome = self.calamityTable.Roll(demesneYear)

        # Catch flags instead of crating derived classes for everything
        if "Wandering merchant" in outcome.outcome:
            demesneYear.wanderingMerchant = True
        elif "irrigation forever" in outcome.outcome:
            demesneYear.demesne.baseFate -= 1

        return outcome
