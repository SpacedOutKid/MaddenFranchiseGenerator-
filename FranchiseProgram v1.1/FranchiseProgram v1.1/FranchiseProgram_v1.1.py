import random

#This is a list for the madden teams to be located, a list for the  relocation cities
showFranchiseHistory = input(f'Would you like to display the franchise history enter yes or no: ')
if showFranchiseHistory == 'yes':
    #A list of all the National Football League Teams 
    nflTeams = """
    Indianapolis Colts, Jacksonville Jaguars, Houston Texans,
    Denver Broncos, Las Vegas Raiders, San Diego Chargers, Cleveland Browns,
    Cincinnati Bengals, Baltimore Ravens, Pittsburgh Steelers,
    New England Patriots, Buffalo Bills, Miami Dolphins, New York Jets,
    Los Angeles Rams, San Fransisco 49ers, Sacramento Condors, Seatle Seahawks
    Atlanta Falcons, Carolina Panthers, New Orleans Saints, Tampa Bay Buccaneers, Dallas Cowboys,
    New York Giants, Washington Redskins, Philadelphia Eagles, Green Bay Packers,
    Detroit Lions, Chicago Bears, Minnesota Vikins, Kansas City Chiefs"""

    #A list of the teams in the American Football Conference 
    afcConference = """
    Indianapolis Colts, Tennessee Titans, Jacksonville Jaguars, Houston Texans,
    Denver Broncos, Las Vegas Raiders, San Diego Chargers, Cleveland Browns,
    Cincinnati Bengals, Baltimore Ravens , Pittsburgh Steelers, Kansas City Chiefs
    New England Patriots, Buffalo Bills, Miami Dolphins, New York Jets"""
    #A list of the teams in the National Football Conference 
    nfcConference = """
    Los Angeles Rams, San Fransisco 49ers,  Sacramento Condors, Seatle Seahawks
    Atlanta Falcons, Carolina Panthers, New Orleans Saints, Tampa Bay Buccaneers, Dallas Cowboys,
    New York Giants, Washington Redskins, Philadelphia Eagles, Green Bay Packers,
    Detroit Lions, Chicago Bears, Minnesota Vikins"""

    #A list for the NFL teams seperated by divisions 
    afcSouth ="""
    Indianapolis Colts, Tennessee Titans ,Jacksonville Jaguars, Houston Texans"""

    afcWest = """
    Kansas City Chiefs, Denver Broncos, Las Vegas Raiders, San Diego Chargers"""

    afcNorth = """
    Cleveland Browns, Cincinnati Bengals, Baltimore Ravens, Pittsburgh Steelers"""

    afcEast = """
    New England Patriots, Buffalo Bills, Miami Dolphins, New York Jets"""

    nfcWest = """Los Angeles Rams, San Fransisco 49ers, Sacramento Condors, Seatle Seahawks"""

    nfcSouth = """
    Atlanta Falcons, Carolina Panthers, New Orleans Saints, Tampa Bay Buccaneers"""

    nfcEast = """
    Dallas Cowboys, New York Giants, Washington Redskins, Philadelphia Eagles"""

    nfcNorth = """
    Green Bay Packers, Detroit Lions, Chicago Bears, Minnesota Vikins""" 

    #A list for all of the Mvps during the franchise 2020 - (Current) 
    mvpWinners = """
                    Joe Burrow 2021"""

    #A list for all of the records set during the franchise 2020 - (Current) 
    recordsSet ="""
                   2020 Amari Cooper (WR) - (Colts) - Receiving Yards in a Game ~ 351
                   2020 Amari Cooper (WR) - (Colts) - Receiving Yards in a Season ~ 2439
                   2020 Jalen Reagor (WR) - (Condors) - Receiving TDs in a Season ~ 29
                   2021 Joe Burrow (QB) - (Colts) - Passing Yards in a Game ~ 657  
                   2021 Joe Burrow (QB) - (Colts) - Passing Touchdowns in a Game ~ 9
                   2021 T.Y Hilton (WR) - (Colts) - Receiving Yards in a Game ~ 437
                   2021 T.Y Hilton (WR) - (Colts) - Receiving TDs in a Game ~ 7
                   2021 Joe Burrow (QB) - (Colts) - Passing Yards in a Season ~ 5601
                   2021 Joe Burrow (QB) - (Colts) - Passing TDs in a Season ~ 57
                   2021 Amari Cooper (WR) - (Colts) - Receiving TDs in a Season ~ 29"""

   #Prints the franchise's information 
    print(f'The NFL Teams in the franchise are: {nflTeams}\n\n')
    print(f'The NFL Teams in the AFC Conference are: {afcConference}\n\n')
    print(f'The NFL Teams in the NFC Conference are: {nfcConference}\n\n')
    print(f'The NFL Team in the AFC South Division are the: {afcSouth}\n\n')
    print(f'The NFL Team in the AFC West Division are the: {afcWest}\n\n')
    print(f'The NFL Team in the AFC East Division are the: {afcEast}\n\n')
    print(f'The NFL Team in the AFC North Division are the: {afcNorth}\n\n')
    print(f'The NFL Team in the NFC South Division are the: {nfcSouth}\n\n')               
    print(f'The NFL Team in the NFC West Division are the: {nfcWest}\n\n') 
    print(f'The NFL Team in the NFC East Division are the: {nfcEast}\n\n')             
    print(f'The NFL Team in the NFC North Division are the: {nfcNorth}\n\n')
    print(f'The Most Valuable Players for the franchise are: {mvpWinners}\n\n')
    print(f'The records that were broken during the franchise were: {recordsSet}\n\n')

    #Goes through the generation method for the loop if the user would like
    generateRelocation = input(f'Would you like to generate a relocation?: ').lower()
    if generateRelocation == 'yes':
        maddenTeams = ['Jets','Packers','Lions','Cowboys','Falcons','Texans','Browns', 'Ravens',
               'Panthers','Bengals','Titans','Saints','Buccaneers','49ers','Dolphins','Chargers','Chiefs','Patriots','Bears',
               'Redskins','Bills','Vikins','Eagles','Broncos','Seahwaks']

        relocationCities = ['Mexico City','Dublin','Brooklyn','Memphis','Orlando','Chicago','San Diego','Portland',
                  'Austin','Houston','Columbus','Oklahoma City']

        #These are list for the  teams choices 
        teamName = ['1','2','3']
        teamUniform = ['1','2','3']
        stadiumType = ['Basic','Deluxe']
        stadiumChoice = ['1','2','3','4','5']


        #This is the choices that will be generated 
        teamToRelocate = random.choice(maddenTeams)
        relocationCity = random.choice(relocationCities)
        newTeamName = random.choice(teamName)
        newTeamUniform = random.choice(teamUniform)
        newStadiumType = random.choice(stadiumType)
        newStadiumChoice = random.choice(stadiumChoice)

        print(f"""
        The team to relocate will be {teamToRelocate} & they will relocate to {relocationCity}. 
        Their team name choice is option {newTeamName} their uniform option is option {newTeamUniform}, 
        their new stadium will be a {newStadiumType} type and option {newStadiumChoice}""")

#The method to generate a relocation and bypass the franchise history 
if showFranchiseHistory == 'no':
    generateRelocation = input(f'Would you like to generate a relocation?: ').lower()
    if generateRelocation == 'yes':
        maddenTeams = ['Jets','Packers','Lions','Cowboys','Falcons','Texans','Browns', 'Ravens',
               'Panthers','Bengals','Titans','Saints','Buccaneers','49ers','Dolphins','Chargers','Chiefs','Patriots','Bears',
               'Redskins','Bills','Vikins','Eagles','Broncos','Seahwaks']

        relocationCities = ['Mexico City','Dublin','Brooklyn','Memphis','Orlando','Chicago','San Diego','Portland',
                  'Austin','Houston','Columbus','Oklahoma City']

        #These are list for the  teams choices 
        teamName = ['1','2','3']
        teamUniform = ['1','2','3']
        stadiumType = ['Basic','Deluxe']
        stadiumChoice = ['1','2','3','4','5']


        #This is the choices that will be generated 
        teamToRelocate = random.choice(maddenTeams)
        relocationCity = random.choice(relocationCities)
        newTeamName = random.choice(teamName)
        newTeamUniform = random.choice(teamUniform)
        newStadiumType = random.choice(stadiumType)
        newStadiumChoice = random.choice(stadiumChoice)

        print(f"""
        The team to relocate will be {teamToRelocate} & they will relocate to {relocationCity}. 
        Their team name choice is option {newTeamName} their uniform option is option {newTeamUniform}, 
        their new stadium will be a {newStadiumType} type and option {newStadiumChoice}""")