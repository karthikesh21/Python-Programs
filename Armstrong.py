num = int(input("Enter a number: "))
order = len(str(num))
sum = sum(int(d)**order for d in str(num))
print("Armstrong Number" if sum == num else "Not an Armstrong Number")
