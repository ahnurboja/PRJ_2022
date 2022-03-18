from scheduler import *
from scheduler import Individual, Meeting
from datetime import datetime, timedelta
import random
from faker import Faker
fake = Faker()

class InputGenerator:

    # now = datetime.now().replace(microsecond=0, second=0, minute=0)
    now = datetime(2021,12,10,5)

    def generateInputs(self):
        inputs = []
        for i in range(1, 4):
            inputs.append(self.generateInput(i))
        print(inputs)

    def generateInput(self, complexity):
        I = self.generateIndividuals(complexity)
        M = self.generateMeetings(I, complexity)

        return (I, M)

    def generateIndividuals(self, complexity):
        I = []
        for i in range(complexity*5):
            I.append(Individual("i"+str(i)))
        return I

    def generateMeetings(self, I, complexity):
        M = []
        for i in range(complexity*5):
            name = "m"+str(i)
            A = random.sample(I, random.randint(1,complexity*5))
            h = random.choice(A)
            l = random.randint(1, 5)
            w = random.randint(1, 10)
            d = fake.date_time_between(start_date=self.now, end_date=self.now+timedelta(hours=50)).replace(microsecond=0, second=0, minute=0)
            t = None

            M.append(Meeting(name, A, h, l, w, d, t))
        return M
