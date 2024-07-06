from enum import IntEnum

class EnglandParties(IntEnum): # 3 seats per constituency
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6

class ScotlandParties(IntEnum):
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6
    SNP = 7

class WalesParties(IntEnum):
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green = 5
    Independant = 6
    Plaid_Cymru = 7

class NIrelandParties(IntEnum): # theres more
    Democratic_Unionist_Party = 1
    Traditional_Unionist_Voice = 2
    Sinn_Fein = 3
    Alliance_Party = 4
    Ulster_Unionist_Party = 5