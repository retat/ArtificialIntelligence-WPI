class Environment(object):
    def __init__(self, a, b):
        self.dirtlocation = {'A': a, 'B': b}


class VacuumAgent:
    performanceMeasure = 0

    def __init__(self, environment, location):
        print("--------------")
        print("Start environment: " + str(environment.dirtlocation))
        score = 0
        vacuumlocation = location
        print("Vacuum starting on A" if vacuumlocation == 0 else "Vacuum starting on B")
        if vacuumlocation == 0:
            if environment.dirtlocation['A'] == 1:
                score += 1
                score -= 1
                if environment.dirtlocation['B'] == 1:
                    score += 1
            else:
                score -= 1
                if environment.dirtlocation['B'] == 1:
                    score += 1
        elif vacuumlocation == 1:
            if environment.dirtlocation['B'] == 1:
                score += 1
                score -= 1
                if environment.dirtlocation['A'] == 1:
                    score += 1
            else:
                score -= 1
                if environment.dirtlocation['A'] == 1:
                    score += 1
        print("Performance Measurement: " + str(score))
        VacuumAgent.performanceMeasure += score


VacuumAgent(Environment(0, 0), 0)
VacuumAgent(Environment(0, 0), 1)
VacuumAgent(Environment(1, 1), 0)
VacuumAgent(Environment(1, 1), 1)
VacuumAgent(Environment(1, 0), 0)
VacuumAgent(Environment(1, 0), 1)
VacuumAgent(Environment(0, 1), 0)
VacuumAgent(Environment(0, 1), 1)
print("--------------")
print("Average Performance measure:")
print(VacuumAgent.performanceMeasure / 8)
print("--------------")
