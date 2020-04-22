import csv
import random
import operator
import numpy as np
class Gases:
    def __init__(self, sample=None, ammonia = None ,cyclohexanone= None,acetone = None,ethanol = None,methanol =None ,sensor_1 = None,
                 sensor_2 = None,sensor_3 = None,sensor_4 = None):
        self.sample = sample
        self.ammonia = ammonia
        self.cyclohexanone = cyclohexanone
        self.acetone =acetone
        self.ethanol = ethanol
        self.methanol = methanol
        self.sensor_1 = sensor_1
        self.sensor_2 = sensor_2
        self.sensor_3 = sensor_3
        self.sensor_4 = sensor_4

def read_file():
    sensor_1 = []
    sensor_2 =[]
    sensor_3 =[]
    sensor_4 =[]
    gas_list =[]
    gas_sensor_1 =[]
    gas_sensor_2 =[]
    gas_sensor_3 =[]
    gas_sensor_4 =[]
    gas_conc=[]


    with open('combined.txt', 'r') as data:
        header = next(data)
        header =header.strip()
        for reading in csv.reader(data, delimiter=","):
            reading = [float(i) for i in reading]
            gas_list.append(Gases(reading[0],reading[1],reading[2],reading[3],reading[4],reading[5],reading[6]
                                  ,reading[7],reading[8],reading[9]))
            sensor_1.append(reading[6])
            sensor_2.append(reading[7])
            sensor_3.append(reading[8])
            sensor_4.append(reading[9])
        print(header)
        count_1 = 0
        for entry in gas_list:
            if entry.sample == 1.0 or  entry.sample ==  2.0 or entry.sample ==  3.0 or entry.sample ==  4.0 or \
            entry.sample ==  6.0 or entry.sample == 10.0:
                gas_sensor_1.append(entry.sensor_1)
                gas_sensor_2.append(entry.sensor_2)
                gas_sensor_3.append(entry.sensor_3)
                gas_sensor_4.append(entry.sensor_4)
                gas_conc.append(entry.ammonia)
                count_1 += 1
        sensor_main = gas_sensor_1 + gas_sensor_2 + gas_sensor_3 + gas_sensor_4
        gas_main = gas_conc
        gas_sensor_1 =[]
        gas_sensor_2=[]
        gas_sensor_3 =[]
        gas_sensor_4=[]
        gas_conc = []
        count =0
        for entry in gas_list:
            if entry.sample == 1.0 or entry.sample == 7.0 or  entry.sample == 10.0:
                gas_sensor_1.append(entry.sensor_1)
                gas_sensor_2.append(entry.sensor_2)
                gas_sensor_3.append(entry.sensor_3)
                gas_sensor_4.append(entry.sensor_4)
                gas_conc.append(entry.cyclohexanone)
                count += 1
        sensor_main =  sensor_main + gas_sensor_1 + gas_sensor_2 + gas_sensor_3 + gas_sensor_4



        gas_main = gas_main + gas_conc
        index = count_1 * 4
        gas1_sensor = sensor_main[:index]
        gas2_sensor = sensor_main[index:]
        gas_1= gas_main[:count_1]
        gas_2 =gas_main[count_1:]
        gas_2  = np.array(gas_2)
        gas_1 = np.array(gas_1)
        gas1_sensor = np.array_split(np.array(gas1_sensor), 4)
        gas2_sensor = np.array_split(np.array(gas2_sensor), 4)
        for i in range(4):
            print(np.corrcoef(gas1_sensor[i],gas_1)[0,1])
        for i in range(4):
            print(np.corrcoef(gas2_sensor[i],gas_2)[0,1])





















class Report:
     def __init__(self, g=None, s = None ,status= None,r = None,sig =
    None ,m = None,c = None,):
         self.g = g
         self.s = s
         self.status = status
         self.r = r
         self.sig = sig
         self.m = m
         self.c = c



def populate():
    with open("gas_Sensor.csv", "w") as file:
        writer = csv.writer(file)
        for s in range(100):
            for g in range(100):
                r = 0.4 + random.random()/2
                rand = random.random()
                if rand < 0.1:
                    writer.writerow (("{}{}".format("Gas", g), "{}{}".format("Sensor", s), "Yes",r,0.001,
                                      random.random()/500,20*random.random()))

                elif rand < 0.5:
                    writer.writerow(("{}{}".format("Gas", g), "{}{}".format("Sensor", s), "No", 0, 0, 0, 0))
    file.close()


def load_report():
    r_lst = []
    with open("gas_Sensor.csv", "r",) as report:
        r_reader = csv.reader(report, delimiter=',')
        sort = sorted(r_reader,reverse=True, key=operator.itemgetter(3))
        for row in sort:
            r_lst.append(Report(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    report.close()
    return r_lst


def report():
    sensor_list=[]
    desired_gas =input("Enter Desired Gas")
    with open("Sensor_report.csv", 'w') as new_gas_report:
        r_writer = csv.writer(new_gas_report)
        gas_list =load_report()
        for item in gas_list:
            if  item.g == desired_gas and item.status == "Yes":
                r_writer.writerow([item.g, item.s, item.status,item.r,item.sig,item.m,item.c])
                sensor_list.append(Report(item.g, item.s, item.status,item.r, item.sig, item.m,item.c))
    return sensor_list


def find_sensor(sensor_list):
        unwanted_gas = [(x) for x in
                        input("Enter Unwanted Gases' name and include a space if adding multiple.: ").split()]
        gas_X = sensor_list
        bad_gases =load_report()
        for item in bad_gases:
            for gases in unwanted_gas:
                for items in gas_X:
                    if item.g == gases and item.status == "Yes" and item.s == items.s:
                        gas_X.remove(items)

        return sensor_list






def write_report():
    with open("Sensor_with_no_unwanted_gases_Report.csv", 'w') as new_gas_report3:
        r_writer = csv.writer(new_gas_report3)
        sensor_list = report()
        sensor_list = find_sensor(sensor_list)
        for item in sensor_list:
            r_writer.writerow([item.g, item.s, item.status, item.r, item.sig, item.m, item.c])



def y_value(sensor_list):
    m =[]
    c =[]
    r =[]
    y = []
    y_max =[]
    s = ["Sensor6","Sensor45","Sensor46"]
    g =["Gas69"]
    for sensors in s:
        for gases in g:
            for i in sensor_list:
                if i.s == sensors and i.g == gases:
                    m.append(i.m)
                    c.append(i.c)
                    r.append(i.r)
    m_f = [float(x) for x in m]
    c_f = [float(z) for z in c]
    r_f = [float(a) for a in r]
    for i, x in zip( m_f, c_f):
        y.append(i * 2 + x)
    for i, z in zip(y,r_f):
        y_max.append(i + z)

def test_correlation():
    x_array = [56, 56, 65, 65, 50, 25, 87, 44, 45]
    y_array = [87, 91, 85, 91, 75, 28, 122, 66, 58]
    print(np.corrcoef(x_array, y_array)[0, 1])

s = load_report()
hello = y_value(s)
read_file()













































def high_low(sensor_value):
    high = 0
    low = 1000000000000000
    for i in sensor_value:
        if i > high:
            high = i
        if i < low:
            low = i
    return high,low


def test_h_l(lst):
    highest_value , _ = high_low(lst)
    _, lowest_value = high_low(lst)
    print( "Max is:" + str(highest_value), "Min is:" + str(lowest_value))



