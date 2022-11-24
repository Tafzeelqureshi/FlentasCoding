import csv
from datetime import timedelta
def getTime(time):
  newTime = time.strip().split(":")
  delta = timedelta(hours=int(newTime[0]), minutes=int(newTime[1]), seconds=int(newTime[2]))
  return delta.total_seconds()

def PrintOuput(formNumbers,freePlanNumbers,totalTime,cost):
    print("-----------------------Unique from Numbers--------")
    [print(i) for i in formNumbers]
    print("-----------------------Unique Free plan from Numbers--------")
    [print(i) for i in freePlanNumbers]
    print("-----------------------Total call time of from numbers--------")
    for i,j in totalTime.items():
      print(i,timedelta(seconds=int(j)))
    print("-----------------------Total Cost in rupees--------")
    print(cost/100)

def getCost(time):
  cost =0
  minutes = int(time//60)
  if(minutes>0):
    time = time//60
    if(time>0):
      minutes +=1
    cost = minutes*30
  return cost

if __name__ == "__main__":
  fileNme= input("Entert the name of the call log file")
  formNumbers=[]
  freePlanNumbers=[]
  totalTime={}
  cost=0
  f = open(fileNme)
  for row in csv.reader(f):
    time=getTime(row[2])
    if(row[0] in totalTime):
      totalTime[row[0]] +=time
    else:
      totalTime[row[0]] =time

    if(row[0] in formNumbers):
      minutes=int(time//60)
      if(minutes<=0):
            if(row[0] not in freePlanNumbers):
              freePlanNumbers.append(row[0])
    else:
       formNumbers.append(row[0])
       minutes=int(time//60)
       if(minutes<=0):
        if(row[0] not in freePlanNumbers):
          freePlanNumbers.append(row[0])
    cost +=getCost(getTime(row[2]))  
  PrintOuput(formNumbers,freePlanNumbers,totalTime,cost)

f = open("data.txt")
  for row in csv.reader(f):
    print(row)