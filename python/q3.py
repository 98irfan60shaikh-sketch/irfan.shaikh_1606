subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))

total = subject1 + subject2 + subject3
average = total / 3
percentage = (total / 300) * 100

print("\n--- Results ---")
print(f"Total Marks:{total} , Average Marks: {average} , Percentage: {percentage}%")