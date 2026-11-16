#interest per month
interest = 0.1 

#time in months
time = 12 

#debt
debt = 15000

for i in range(1, time+1):
    debt = debt + (debt * interest)
    print(f"Month {i}: {debt:.2f}")
