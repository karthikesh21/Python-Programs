print("Example of break:")
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print(i)

print("\nExample of continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping", i)
        continue
    print(i)

print("\nExample of pass:")
for i in range(1, 4):
    if i == 2:
        pass  # does nothing, placeholder
        print("Pass executed for", i)
    print("Number:", i)
