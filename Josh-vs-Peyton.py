#This is Josh Code
Deposit = int(input("Enter Jonh Deposit :"))
Rate = int(input("Enter Bank rate :"))
Time = int(input("Time that invest in the Company :"))
print("\n{:<10} {:<20} {:<25} ".format("Time", "Rate", "Total")) 
print("="*15) 
counter = 0
for Time in range(Time):
  Time = Time+1
  Deposit = 250000
  Rate = 10
  Total = Deposit*(1+(Rate/100))**Time
  print("{:2}".format(Time),"{:14.2f}".format(Rate),"{:18.2f}".format(Total))
  print("="*15)
