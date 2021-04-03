import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

file = '../resources/py_bank.csv'

total_month =[]
profit_loss = []
row_count = 0
Profit = 0
previous_profit = 0
current_profit = 0
max_profit_increase = 0
max_profit_decrease = 0
increase_month = 0
decrease_month = 0
average = 0



with open(file,encoding="utf-8") as py_bank:
    
    csvreader = csv.reader(py_bank, delimiter=',')

    header = next(csvreader)
    first_row = next(csvreader)
    Profit += int(first_row[1])
    row_count= row_count + 1
    previous_profit = int(first_row[1])
    current_loss = 0
    previous_loss = 0

    #print(header)

    for row in csvreader:
        total_month.append(row[0])
        profit_loss.append(row[1])
        Profit += int(row[1])
        row_count= row_count + 1
        current_profit = int(row[1])

        x = current_profit - previous_profit
        average = (average + x)
        
        if x > max_profit_increase:
            max_profit_increase = x
            increase_month = row[0]
        previous_profit = current_profit

        if x < max_profit_decrease:
            max_profit_decrease = x
            decrease_month = row[0]
        previous_loss = current_loss

average = average/row_count

print("Financial Analysis")
print("__________________________")

print(f"Total Month: {Profit}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {increase_month} ${max_profit_increase}")
print(f"Greatest Decrease in Profits: {decrease_month} ${max_profit_decrease}")



cleaned_py_bank = zip(total_month,profit_loss)
output_file = os.path.join("jordan_pybank.csv")

with open(output_file,"w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["data", "Profit/Loss"])

    writer.writerows(cleaned_py_bank)

