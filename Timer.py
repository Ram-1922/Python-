# Timer
import time

hrs=int(input("Enter Hour : "))
min=int(input("Enter Minute : "))
sec=int(input("Enter Second : "))
n=(hrs*3600)+(min*60)+sec
for i in range(n,0,-1):
    seconds = i%60
    minutes = int(i/60)%60
    hours = int(i/3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("All done...")