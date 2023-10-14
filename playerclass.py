from random import randint
class Player:
    def __init__(self, number, position, specificPosition, benchStatus, year="1", goals="0", injury="no", team="Unaffiliated", name=""):
        self.number = number
        self.position = position
        self.specificPosition = specificPosition
        #"center", "left", "right", "attacking", "defending", "sweeper", "stopper", "flat back"
        self.benchStatus = benchStatus
        #"on field" or "on bench"
        self.year = year
        #integer, 1-5
        self.goals = goals
        #integer
        self.injury = injury
        #"yes" or "no"
        self.team = team
        self.name = name
        if (self.position == "F"):
            self.f = self.F()
        elif (self.position == "OM"):
            self.om = self.OM()
        elif (self.position == "CM"):
            self.cm = self.CM()
        elif (self.position == "OB"):
            self.ob = self.OB()
        elif (self.position == "CB"):
            self.cb = self.CB()
        elif (self.position == "G"):
            self.g = self.G()

    def joinTeam(self, newTeam):
        self.team = newTeam
        if (self.name == ""):
            newTeam.roster.append(self.number)
        else:
            newTeam.roster.append(self.name)

    def changeName(self, newName):
        self.name = newName
        self.team.roster.remove(self.number)
        self.team.roster.append(self.name)

    def afterGameImprove(self, stat):
        #For improving stats.  Make sure to check no one is going above +3
        if (self.position == "F"):
            if (stat == "shot") and (self.f.shot != 3):
                self.f.shot += 1
            elif (stat == "synergy") and (self.f.synergy != 3):
                self.f.synergy += 1
            elif (stat == "speed") and (self.f.speed != 3):
                self.f.speed += 1
        elif (self.position == "OM"):
            if (stat == "passing") and (self.om.passing != 3):
                self.om.passing += 1
            elif (stat == "endurance") and (self.om.endurance != 3):
                self.om.endurance += 1
            elif (stat == "speed") and (self.om.speed != 3):
                self.om.speed += 1
        elif (self.position == "CM"):
            if (stat == "offense") and (self.cm.offense != 3):
                self.cm.offense += 1
            elif (stat == "defense") and (self.cm.defense != 3):
                self.cm.defense += 1
            elif (stat == "speed") and (self.cm.speed != 3):
                self.cm.speed += 1
        elif (self.position == "OB"):
            if (stat == "defense") and (self.ob.defense != 3):
                self.ob.defense += 1
            elif (stat == "handling") and (self.ob.handling != 3):
                self.ob.handling += 1
            elif (stat == "speed") and (self.ob.speed != 3):
                self.ob.speed += 1
        elif (self.position == "CB"):
            if (stat == "stopping") and (self.cb.stopping != 3):
                self.cb.stopping += 1
            elif (stat == "sweeping") and (self.cb.sweeping != 3):
                self.cb.sweeping += 1
            elif (stat == "speed") and (self.cb.speed != 3):
                self.cb.speed += 1
        elif (self.position == "G"):
            if (stat == "saving") and (self.g.saving != 3):
                self.g.saving += 1
            elif (stat == "control") and (self.g.control != 3):
                self.g.control += 1
            elif (stat == "lead") and (self.g.lead != 3):
                self.g.lead += 1
        #Need message for "Nuh uh you can't do that" if == 3

    def afterSeasonImprove(self):
        improvements = []
        #Give possible after season improvement

    def extraShot(self):
        if (self.benchStatus == "on field"):
            roll = randint(1, 20)
            if (roll == 20):
                self.goals += 1
            elif (roll == 1):
                self.injury = "yes"
                self.benchStatus == "on bench"
    
    class F:
        def __init__(self):
            self.shot = randint(-3, 3)
            self.synergy = randint(-3, 3)
            self.speed = randint(-3, 3)

    class OM:
        def __init__(self):
            self.passing = randint(-3, 3)
            self.endurance = randint(-3, 3)
            self.speed = randint(-3, 3)

    class CM:
        def __init__(self):
            self.offense = randint(-3, 3)
            self.defense = randint(-3, 3)
            self.speed = randint(-3, 3)

    class OB:
        def __init__(self):
            self.defense = randint(-3, 3)
            self.handling = randint(-3, 3)
            self.speed = randint(-3, 3)

    class CB:
        def __init__(self):
            self.stopping = randint(-3, 3)
            self.sweeping = randint(-3, 3)
            self.speed = randint(-3, 3)

    class G:
        def __init__(self):
            self.saving = randint(-3, 3)
            self.control = randint(-3, 3)
            self.lead = randint(-3, 3)