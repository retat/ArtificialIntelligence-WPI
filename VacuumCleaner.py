import random


class Environment(object):
    def __init__(self, a, b):
        self.locationCondition = {'A': a, 'B': b}


class SimpleReflexVacuumAgent(Environment):
    performanceMeasure = 0

    def __init__(self, environment, location):
        print(environment.locationCondition)
        score = 0
        vacuumLocation = location
        if vacuumLocation == 0:
            print("Vacuum is placed at Location A.")
            if environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
                environment.locationCondition['A'] = 0;
                score += 1
                print("Location A has been Cleaned.")
                print("Moving to Location B...")
                score -= 1
                if environment.locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                    environment.locationCondition['B'] = 0;
                    score += 1
                    print("Location B has been Cleaned.")
            else:
                score -= 1
                print("Moving to Location B...")
                if environment.locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                    environment.locationCondition['B'] = 0;
                    score += 1
                    print("Location B has been Cleaned.")
        elif vacuumLocation == 1:
            print("Vacuum placed at Location B.")
            if environment.locationCondition['B'] == 1:
                print("Location B is Dirty.")
                environment.locationCondition['B'] = 0;
                score += 1
                print("Location B has been Cleaned.")
                score -= 1
                print("Moving to Location A...")
                if environment.locationCondition['A'] == 1:
                    print("Location A is Dirty.")
                    environment.locationCondition['A'] = 0;
                    score += 1
                    print("Location A has been Cleaned.")
            else:
                print("Moving to Location A...")
                score -= 1
                if environment.locationCondition['A'] == 1:
                    print("Location A is Dirty.")
                    environment.locationCondition['A'] = 0;
                    score += 1
                    print("Location A has been Cleaned.")
        print(environment.locationCondition)
        print("Performance Measurement: " + str(score))
        SimpleReflexVacuumAgent.performanceMeasure += score


SimpleReflexVacuumAgent(Environment(0, 0), 0)
SimpleReflexVacuumAgent(Environment(0, 0), 1)

SimpleReflexVacuumAgent(Environment(1, 1), 0)
SimpleReflexVacuumAgent(Environment(1, 1), 1)

SimpleReflexVacuumAgent(Environment(1, 0), 0)
SimpleReflexVacuumAgent(Environment(1, 0), 1)

SimpleReflexVacuumAgent(Environment(0, 1), 0)
SimpleReflexVacuumAgent(Environment(0, 1), 1)

print("Average Performance measure:")
print("--------------")
print(SimpleReflexVacuumAgent.performanceMeasure/8)
print("--------------")
