
import time
import datetime
import webbrowser
import os
import urllib.request as req

#from common.constants import liveEngageConstants
#from common import passDecrypt
#from datetime import datetime, timezone

def convertToEpoch(dateToConvert):
    pattern = '%Y-%m-%d %H:%M:%S'
    epStartDateTime = int(time.mktime(time.strptime(str(dateToConvert), pattern)) ) *1000
    return epStartDateTime

def epochStartDate(nowMinusStart):
    startDate =  datetime.date.today() - datetime.timedelta(days=nowMinusStart)
    startTime = datetime.time(0 ,0 ,0)
    startDateTime = convertToEpoch(datetime.datetime.combine(startDate, startTime))
    return startDateTime

def epochEndDate(nowMinusEnd):
    endDate =  datetime.date.today() - datetime.timedelta(days=nowMinusEnd)
    endTime = datetime.time(23 ,59 ,59)
    endDateTime = convertToEpoch(datetime.datetime.combine(endDate, endTime))
    return endDateTime


def getEndTime(runDateTime):
    endTime = (runDateTime - datetime.timedelta(minutes=1440)).isoformat()
    endTime = endTime[0:19] + '+00:00'
    return endTime

def getStartTime(runDateTime):
    startTime = (runDateTime).isoformat()
    startTime = startTime[0:19] + '+00:00'
    return startTime



# old proxyauth scipt that only seems to work at certain times of the day
# def proxyAuth():
#    webbrowser.open(liveEngageConstants.proxyURL, new=1)
#    time.sleep(10)
#    browserExe = "iexplore.exe"
#    os.system("taskkill /f /im "+browserExe)

def fileIDString(start ,end):
    strDate =  str(datetime.date.today())
    fileIDString = strDate + "_" + str(start) + "_" + str(end)
    return fileIDString

def queryDate(todayMinus):
    strDate = str(datetime.date.today() - datetime.timedelta(days=todayMinus))
    return strDate

def proxyAuth():
    proxyString = r'http://' + os.getlogin() + ':' + passDecrypt.proxyPass() + '@dia2.santanderuk.gs.corp:80'
    # proxyString = proxyString.encode('unicode_escape').decode().replace('\\\\', '\\')
    proxy = req.ProxyHandler({'http': proxyString})
    auth = req.HTTPBasicAuthHandler()
    opener = req.build_opener(proxy, auth, req.HTTPHandler)
    req.install_opener(opener)
    conn = req.urlopen('http://google.com')
    return_str = conn.read()

# proxyString = r'http://' + os.getlogin() + ':' + passDecrypt.proxyPass() + '@dia2.santanderuk.gs.corp:80'
# print(proxyString)

print(getEndTime(datetime.datetime.utcnow()))
print(getStartTime(datetime.datetime.utcnow()))

#endTime = (datetime.datetime.now() - datetime.timedelta(minutes=15)).isoformat()

#print(endTime)