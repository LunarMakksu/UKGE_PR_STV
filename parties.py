from enum import IntEnum

class EnglandParties(IntEnum): # 3 seats per constituency
    Conservative = 1
    Labour = 2
    Liberal_Democrats = 3
    Reform_UK = 4
    Green_Party = 5
    Independant = 6

class ScotlandParties(IntEnum):
    Scottish_Conservative = 1
    Scottish_Labour = 2
    Scottish_Liberal_Democrats = 3
    Scottish_Reform_UK = 4
    Scottish_Green_Party = 5
    Scottish_Independant = 6
    SNP = 7

class WalesParties(IntEnum):
    Welsh_Conservative = 1
    Welsh_Labour = 2
    Welsh_Liberal_Democrats = 3
    Welsh_Reform_UK = 4
    Welsh_Green_Party = 5
    Welsh_Independant = 6
    Plaid_Cymru = 7

class NIrelandParties(IntEnum): # theres more
    Democratic_Unionist_Party = 1
    Traditional_Unionist_Voice = 2
    Sinn_Fein = 3
    Alliance_Party = 4
    Ulster_Unionist_Party = 5