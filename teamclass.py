from random import randint
class Team():
    def __init__(self, owner, name, formation, roster, fieldRoster, fieldFs, fieldOMs, fieldCMs, fieldOBs, fieldCBs, fieldGs):
        self.owner = owner
        self.name = name
        self.formation = formation
        #"451", "442", "433"
        #All below are arrays
        self.roster = roster
        self.fieldRoster = fieldRoster
        self.fieldFs = fieldFs
        self.fieldOMs = fieldOMs
        self.fieldCMs = fieldCMs
        self.fieldOBs = fieldOBs
        self.fieldCBs = fieldCBs
        self.fieldGs = fieldGs

    def playGame(self, otherTeam):
        #Function for chances B IS THE TEAM GETTING CHANCES
        def Chances(a, b, side):
            if (b.formation == "442") or (b.formation == "451"):
                for l in b.fieldOMs:
                    if (l.specificPosition == side):
                        chances = randint(1, 3) * (l.om.endurance + 3)
                        chances += l.om.passing
            elif (otherTeam.formation == "433"):
                for j in b.fieldFs:
                    if (j.specificPosition == "center"):
                        chances = randint(1, 3) * j.f.synergy
                for k in b.fieldFs:
                    if (k.specificPosition == side):
                        chances += (k.f.shot + 3)
            if (b.formation == "442") or (b.formation == "433"):
                for i in b.fieldFs:
                    if (i.specificPosition == side):
                        chances += i.f.synergy
            elif(b.formation == "451"):
                chances += b.fieldFs[0].f.synergy
            for m in b.fieldOBs:
                if (m.specificPosition == side):
                    chances += (m.ob.handling)
            for n in a.fieldOBs:
                if (n.specificPosition == side):
                    chances -= n.ob.defense
            return chances
        
        otherLeftChances = Chances(self, otherTeam, "left")
        otherRightChances = Chances(self, otherTeam, "right")
        ourRightChances = Chances(otherTeam, self, "right")
        ourLeftChances = Chances(otherTeam, self, "left")

        def midfield(a, b):
            #midfield modifier
            midMod = randint(1, 4)
            for o in a.fieldCMs:
                if (o.specificPosition == "attacking"):
                    midMod += o.speed
                    midMod += o.offense
            for p in b.fieldCMs:
                if (o.specificPosition == "defending"):
                    midMod -= p.speed
                    midMod -= p.defense
            return midMod
        
        ourMidMod = midfield(self, otherTeam)
        otherMidMod = midfield(otherTeam, self)

        #forward score
        def forwScore(a, b, side):
            score = 0
            for q in a.fieldFs:
                if (q.specificPosition == side):
                    score += (randint(1, 4) * (q.f.speed + 3))
            if (b.fieldCBs[0].specificPosition != "flat back"):
                for r in b.fieldCBs:
                    if (r.specificPosition == "stopper"):
                        score -= r.cb.speed
                        score -= r.cb.stopping
                    elif (r.specificPosition == "sweeper"):
                        score -= r.cb.speed
                        score -= r.cb.sweeping
            elif (b.fieldCBs[0].specificPosition == "flat back"):
                for s in b.fieldCBs:
                    score -= s.cb.speed
                    score -= round((s.cb.stopping + s.cb.sweeping) / 2)
            return score

        if (self.formation == "433") or (self.formation == "442"):
            ourLeftForwScore = forwScore(self, otherTeam, "left")
        elif (self.formation == "451"):
            ourLeftForwScore = 0

        if (self.formation == "433") or (self.formation == "442"):
            ourRightForwScore = forwScore(self, otherTeam, "right")
        elif (self.formation == "451"):
            ourRightForwScore = 0

        if (self.formation == "433") or (self.formation == "451"):
            ourCenterForwScore = forwScore(self, otherTeam, "center")
        elif (self.formation == "442"):
            ourCenterForwScore = 0

        if (otherTeam.formation == "433") or (otherTeam.formation == "442"):
            otherLeftForwScore = forwScore(otherTeam, self, "left")
        elif (otherTeam.formation == "451"):
            otherLeftForwScore = 0

        if (otherTeam.formation == "433") or (otherTeam.formation == "442"):
            otherRightForwScore = forwScore(otherTeam, self, "right")
        elif (otherTeam.formation == "451"):
            otherRightForwScore = 0

        if (otherTeam.formation == "433") or (otherTeam.formation == "451"):
            otherCenterForwScore = forwScore(otherTeam, self, "center")
        elif (otherTeam.formation == "442"):
            otherCenterForwScore = 0

        def shotmaker(chance, mm, fs):
            shots = 0
            shots += chance
            shots += round((mm * 0.5))
            shots += fs
            return shots
        
        ourLeftShots = shotmaker(ourLeftChances, ourMidMod, ourLeftForwScore)
        ourRightShots = shotmaker(ourRightChances, ourMidMod, ourRightForwScore)
        otherRightShots = shotmaker(otherRightChances, otherMidMod, otherRightForwScore)
        otherLeftShots = shotmaker(otherLeftChances, otherMidMod, otherLeftForwScore)

        ourGoals = 0
        otherGoals = 0

        if (self.formation == "433"):
            for t in range(round(ourLeftShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                    for v in self.fieldFs:
                        if (v.specificPosition == "left"):
                            shotScore += v.f.shot
                else:
                    shotScore -= otherTeam.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        ourGoals += 1
                        for w in self.fieldFs:
                            if (w.specificPosition == "left"):
                                w.goals += 1

            for u in range(round(ourLeftShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                    for v in self.fieldFs:
                        if (v.specificPosition == "center"):
                            shotScore += v.f.shot
                else:
                    shotScore -= otherTeam.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        ourGoals += 1
                        for w in self.fieldFs:
                            if (w.specificPosition == "center"):
                                w.goals += 1

            for t in range(round(ourRightShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                    for v in self.fieldFs:
                        if (v.specificPosition == "right"):
                            shotScore += v.f.shot
                else:
                    shotScore -= otherTeam.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        ourGoals += 1
                        for w in self.fieldFs:
                            if (w.specificPosition == "right"):
                                w.goals += 1
            for u in range(round(ourRightShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                    for v in self.fieldFs:
                        if (v.specificPosition == "center"):
                            shotScore += v.f.shot
                else:
                    shotScore -= otherTeam.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        ourGoals += 1
                        for w in self.fieldFs:
                            if (w.specificPosition == "center"):
                                w.goals += 1

        if (otherTeam.formation == "433"):
            for t in range(round(otherLeftShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                    for v in otherTeam.fieldFs:
                        if (v.specificPosition == "left"):
                            shotScore += v.f.shot
                else:
                    shotScore -= self.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        otherGoals += 1
                        for w in otherTeam.fieldFs:
                            if (w.specificPosition == "left"):
                                w.goals += 1

            for u in range(round(otherLeftShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                    for v in otherTeam.fieldFs:
                        if (v.specificPosition == "center"):
                            shotScore += v.f.shot
                else:
                    shotScore -= self.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        otherGoals += 1
                        for w in otherTeam.fieldFs:
                            if (w.specificPosition == "center"):
                                w.goals += 1

            for t in range(round(otherRightShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                    for v in otherTeam.fieldFs:
                        if (v.specificPosition == "right"):
                            shotScore += v.f.shot
                else:
                    shotScore -= self.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        otherGoals += 1
                        for w in otherTeam.fieldFs:
                            if (w.specificPosition == "right"):
                                w.goals += 1
            for u in range(round(otherRightShots / 2)):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                    for v in otherTeam.fieldFs:
                        if (v.specificPosition == "center"):
                            shotScore += v.f.shot
                else:
                    shotScore -= self.fieldGs[0].g.saving
                    if (shotScore >= 20):
                        otherGoals += 1
                        for w in otherTeam.fieldFs:
                            if (w.specificPosition == "center"):
                                w.goals += 1

        if (self.formation == "442"):
            for x in range(ourLeftShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                else:
                    for y in self.fieldFs:
                        if (y.specificPosition == "left"):
                            shotScore += y.f.shot
                            shotScore -= otherTeam.fieldGs[0].g.saving
                            if (shotScore >= 20):
                                        otherGoals += 1
                                        y.goals += 1
            
            for x in range(ourRightShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                else:
                    for y in self.fieldFs:
                        if (y.specificPosition == "right"):
                            shotScore += y.f.shot
                            shotScore -= otherTeam.fieldGs[0].g.saving
                            if (shotScore >= 20):
                                        otherGoals += 1
                                        y.goals += 1

        if (otherTeam.formation == "442"):
            for x in range(otherLeftShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                else:
                    for y in otherTeam.fieldFs:
                        if (y.specificPosition == "left"):
                            shotScore += y.f.shot
                            shotScore -= self.fieldGs[0].g.saving
                            if (shotScore >= 20):
                                        otherGoals += 1
                                        y.goals += 1
            
            for x in range(otherRightShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                else:
                    for y in otherTeam.fieldFs:
                        if (y.specificPosition == "right"):
                            shotScore += y.f.shot
                            shotScore -= self.fieldGs[0].g.saving
                            if (shotScore >= 20):
                                otherGoals += 1
                                y.goals += 1

        if (self.formation == "451"):
            for z in range(ourLeftShots + ourRightShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    ourGoals += 1
                    self.fieldFs[0].goals += 1
                else:
                    shotScore += self.fieldFs[0].f.shot
                    shotScore -= otherTeam.fieldGs[0]
                    if (shotScore == 20):
                        ourGoals += 1
                        self.fieldFs[0].goals += 1

        if (otherTeam.formation == "451"):
            for z in range(otherLeftShots + otherRightShots):
                shotScore = randint(1, 20)
                if (shotScore == 20):
                    otherGoals += 1
                    otherTeam.fieldFs[0].goals += 1
                else:
                    shotScore += otherTeam.fieldFs[0].f.shot
                    shotScore -= self.fieldGs[0]
                    if (shotScore == 20):
                        otherGoals += 1
                        otherTeam.fieldFs[0].goals += 1

        #Extra shots
        def extraShots(a, b):
            extraGoals = 0
            for e in a.fieldRoster:
                extraShot = randint(1, 20)
                if (extraShot == 20):
                    extraGoals += 1
            return extraGoals
        
        ourGoals += extraShots(self, otherTeam)
        otherGoals += extraShots(otherTeam, self)

        if (otherGoals == ourGoals):
            gameResult = "tie"
        elif (otherGoals > ourGoals):
            gameResult = "loss"
        elif (otherGoals < ourGoals):
            gameResult = "win"

        gameResults = [gameResult, ourGoals, otherGoals]
        return gameResults