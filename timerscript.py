import time
from timeit import default_timer as timer
print( "hej")
text=input("Skriv in tal: ")
text2=input("Skriv in intervall: ")
timetorun=int(text)
intervall=int(text2)
start = timer()
difference=0
while(difference < timetorun):
    end = timer()
    difference=end-start
    if( int(difference)%int(intervall)==0):
        print("ping")
print(int(end - start)) 