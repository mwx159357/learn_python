import csv
import os
import time

# 监控CPU资源信息
class MonitoringCPUResources(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "cpustatus")]
    # 单次执行监控过程
    def monitoring(self):
        result = os.popen("adb shell dumpsys package com.adventure.live | findstr userId=")
        print(result)
        result = result.split("=")
        print(result)

        cpuvalue = result.readline().split("%")[0].strip()
        currenttime = self.getCurrentTime()
        print("current time is:"+currenttime)
        print("flow used is:" + cpuvalue)
        self.alldata.append([currenttime, cpuvalue])
    # 多次执行监控过程
    def run(self):
        while self.counter > 0:
            self.monitoring()
            self.counter = self.counter - 1
            time.sleep(3)
    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        return currentTime
    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = open('Traffic_statistics.csv', 'w',encoding='utf8',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == "__main__":
    # monitoringCPUResources = MonitoringCPUResources(20)
    # monitoringCPUResources.run()
    # monitoringCPUResources.SaveDataToCSV()


    odj =  MonitoringCPUResources(1)
    odj.monitoring()