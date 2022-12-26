



import time
#from modle_1 import *
#from time import *
#import time
import math
import sys

print("путь: "+str(sys.path))

print("Введите что нибуть!!!")
i1 = sys.stdin.readline()
print("Вы ввели: %s" % i1)

print("Введите что нибуть!!!")
i1 = sys.stdin.readline()
print("Вы ввели: %s" % i1)

#print("путь: "+str(time.path))
#print(i)


#altzone

print ("Значение time.altzone : ", time.altzone)

#asctime

t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))

#ctime

print(time.ctime())

#daylight

print(time.daylight)

if(time.daylight):
        print('DST defined')#летнее время
else:
        print('DST not defined')#не летнее время


print(time.get_clock_info)

if __name__=="__main__":
        clock_name = ['monotonic','perf_counter','process_time','thread_time','time']     
for x in clock_name:
        clock_info = time.get_clock_info(x)
        print("\nInformation on '% s':" % x)
        print(clock_info)

#sleep

time.sleep(1)  # import time
print("Before the sleep statement")
time.sleep(1)
print("After the sleep statement")#statement =? утверждение

#gmtime

print("gmtime :", time.gmtime(1535376132.41552))#Для системы Unix January 1, 1970, 00:00:00в UTC есть эпоха (точка начала времени)
print("gmtime :", time.gmtime(1668952172.7150295))
print("gmtime :", time.gmtime(1668952172))
print("gmtime :", time.gmtime(0))

#localtime

seconds = time.time()
print("Seconds since epoch = ",  seconds)
time.sleep(1)
seconds2 = time.time()
print("Seconds since epoch = ",  seconds2)	

print("gmtime :", time.gmtime(seconds2))

local_time = time.ctime(seconds)
print("Local time:", local_time)

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_mday:", result.tm_mday)
print("tm_min:", result.tm_min)
print("tm_sec:", result.tm_sec)
print("tm_yday:", result.tm_yday)

t = (2022, 11, 20, 20, 10, 40, 6, 324, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)

result = time.asctime(t)
print("Result:", result)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

time_string = "21 June, 2019"
result = time.strptime(time_string, "%d %B, %Y")

print(result)



 
# when x is NaN
x = float('nan')
print(math.ulp(x))
 
# when x is positive infinity
x = float('inf')
print(math.ulp(x))
 
# when x is negative infinity
print(math.ulp(-x))
 
# when x = 0
x = 0.0
print(math.ulp(x))
 
# when x is maximum representable float
x = sys.float_info.max
print(math.ulp(x))
 
# x is a positive finite number
x = 5
print(math.ulp(x))
 
# when x is a negative number
x = -5
print(math.ulp(x))

#when argument is 0.0
print(math.ulp(0.0))

#when argument is positive finite
print(math.ulp(10.0))

#when argument is negative finite
print(math.ulp(-10.0))

#when argument is maximum representable float 
x = sys.float_info.max
print(math.ulp(x),"\n") 

#when argument is positive infinite
print(math.ulp(float('inf')))

#when argument is negative infinite
print(math.ulp(-float('inf')))

#when argument is NaN
print(math.ulp(float('nan')))

print(dir(sys))