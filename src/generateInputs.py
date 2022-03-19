from scheduler import *
from scheduler import Individual, Meeting
from datetime import datetime, timedelta
import random
from faker import Faker
fake = Faker()

class InputGenerator:

    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)

    def __init__(self, maxComplexity):
        self.maxComplexity = maxComplexity


    def generateInputs(self):
        inputs = []
        for i in range(1, self.maxComplexity+1, 10):
            inputs.append(self.generateInput(i))
        
        return inputs

    def generateInput(self, complexity):
        I = self.generateIndividuals()
        M = self.generateMeetings(I, complexity)
        return (I, M)

    def generateIndividuals(self):
        I = []
        for i in range(100):
            I.append(Individual("i"+str(i)))
        return I

    def generateMeetings(self, I, complexity):
        M = []
        for i in range(50):
            name = "m"+str(i)
            A = random.sample(I, random.randint(1,len(I)))
            h = random.choice(A)
            l = random.randint(1, 5)
            w = random.randint(1, 10)
            d = fake.date_time_between(start_date=self.now, end_date=self.now+timedelta(hours=250-complexity)).replace(microsecond=0, second=0, minute=0)
            t = None

            M.append(Meeting(name, A, h, l, w, d, t))
        return M
