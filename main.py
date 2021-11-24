from Demesne import Infrastructure

if __name__ == '__main__':
    # Tes infrastructure
    myInfrastructure = Infrastructure()
    myInfrastructure.incomeBase = 2
    myInfrastructure.incomeDie = 3
    myInfrastructure.incomeNumberOfDice = 1

    print(myInfrastructure.GenerateIncome())

