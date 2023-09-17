import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

if(timestamp<12 and timestamp>=5):
  print("Good Morning")
elif(timestamp>=0 and timestamp<5):
  print("Good Night")
elif(timestamp>=12 and timestamp<17):
  print("Good Afternoon")
else:
  print("Good Evening")
