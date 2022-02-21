import datetime
import random

class GreedyScheduler:
    def __init__(self, individuals, unscheduledM):
        self.individuals = individuals
        self.meetings = unscheduledM

    def getMeetings(self):
        return self.meetings

    def generateSchedule(self):

        for meeting in self.meetings:
            print("Meeting: \n%s\n") % (meeting)
            # Pick earliest time:

            #startTime = datetime.datetime.now()
            startTime = datetime.datetime(2021, 12,10,8) # Mock Current Time For Testing
            hours = datetime.timedelta(hours=meeting.l)
            endTime = startTime + hours

            # Check for Clashes (check for each individual):
            clash = True
            while (clash or endTime > meeting.d):
                clash = False
                for a in meeting.A:
                    print("Checking clashes with %s's calendar\n") % (a)
                    for attendeeMeeting in a.M:
                        print ("Checking for clash with %s\n") % (attendeeMeeting)
                        aMStartTime = attendeeMeeting.t
                        hours = datetime.timedelta(hours=attendeeMeeting.l)
                        aMEndTime = aMStartTime + hours
                        clash = self.isClash(startTime, endTime, aMStartTime, aMEndTime)
                        if clash:
                            print("CLASH")
                            startTime = attendeeMeeting.t + datetime.timedelta(hours=attendeeMeeting.l)
                            hours = datetime.timedelta(hours=meeting.l)
                            endTime = startTime + hours
                            print("\nChanging startTime to %s and endTime to %s\n") % (startTime, endTime)
                            break
                        else:
                            print("NO CLASH")
                    if clash:
                        break
                

        return True
    
    def isClash(self, start1, end1, start2, end2):
        maxStart = max(start1, start2)
        minEnd = min(end1, end2)

        return (minEnd-maxStart).days + 1 > 0


# Individual:
class Individual:

    def __init__(self, name, M):
        self.name = name
        self.M = M

    def __str__(self):
        return "%s" % (self.name)

    def addMeetings(self, newM):
        self.M += newM

# Meeting (Unscheduled Meetings will have null t):
class Meeting:

    def __init__(self, A, h, l, w, d, t):
        self.A = A
        self.h = h
        self.l = l
        self.w = w
        self.d = d
        self.t = t

    def __str__(self):
        out = "(Attendees: ["
        for i in self.A:
            out+="%s," % (i)
        out = out[:-1] + "],\n"

        return out + "Host: %s,\nLength: %s,\nWeight: %s,\nDeadline: %s,\nStart Time: %s)" % (self.h, self.l, self.w, self.d, self.t)

# Example:
i1 = Individual("i1", [])
i2 = Individual("i2", [])
i3 = Individual("i3", [])
i4 = Individual("i4", [])
i5 = Individual("i5", [])

m1 = Meeting([i1,i3,i5], i1, 1, 1.0, datetime.datetime(2021,12,10,18), None)
m2 = Meeting([i1,i3,i4,i5], i5, 2, 1.0, datetime.datetime(2021,12,10,18), None)
m3 = Meeting([i1,i2,i4], i2, 1, 1.0, datetime.datetime(2021,12,10,18), None)

m4 = Meeting([i1,i3,i4,i5], i1, 1, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,9))
m5 = Meeting([i1,i3,i4,i5], i3, 1, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,11))
m6 = Meeting([i4,i5], i4, 2, 1.0, datetime.datetime(2021,12,10,18),  datetime.datetime(2021,12,10,16))

i1.addMeetings([m4,m5])
i3.addMeetings([m4,m5])
i4.addMeetings([m4,m5,m6])
i5.addMeetings([m4,m5,m6])

individuals = [i1,i2,i3,i4,i5]
unscheduledMeetings = [m1,m2,m3]

scheduler = GreedyScheduler(individuals, unscheduledMeetings)

currDate = scheduler.generateSchedule()
print(currDate)