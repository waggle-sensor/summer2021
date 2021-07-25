from enum import Enum
from job import Job 
# Create an enumeration for our states. This seems a bit more elegant than just using hard-coded strings. Might delete later if this complicates things
class State(Enum):
    IDLE = 1
    UPDATING = 2
    STOPPED = 3
    UNINITIALIZED = 4


# maintain a list of jobs, or pending updates
class hc_manager:

# maintaining a 'state' across the manager allows for transparency of operations in the bigger picture# 

    def __init__(self):
        self.__state = State.IDLE
        self.__jobs = []

    def getState(self):
        return self.__state

    def setState(self, newState):
        self.__state = newState


# addJob has an optional parameter to make the new job LIFO, instead of FIFO
    def addJob(self, manifest, LIFO=False): 
        
        if LIFO == True:
            self.__jobs.insert(0, manifest)
        else:
            self.__jobs.append(manifest)

    def getJobs(self):
        return self.__jobs


