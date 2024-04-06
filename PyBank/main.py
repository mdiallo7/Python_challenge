import os
import csv

#set the path to the csv file
file_path = os.path.join("..","resources","election_data.csv")

#initializing variables to store finanacialanalysis results
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes_in_profit_losses = []
dates = []

#reading the csv file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skiping the header
    header = next(csvreader)

    # iterate hrough each row in the csv file
    for row in csvreader:
        # extrait date and profit (loss) values
        date = row[0]
        profit_loss = int(row[1])
        
        # calculate total profit/loss over the entire period
        total_profit_losses += profit_loss

        #calculate the change in profit/loss from the previous monthe
        if total_months > 0:
            change = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change)
            dates.append(date)

    #update the previous profit/loss for the next iteration
    previous_profit_loss = profit_loss
    
    # count the total number of months
    total_months += 1

    #calculate the average change in profit/loss
    average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

    #find the greatest increase and decrease in profit
    greatest_increase = max(changes_in_profit_losses)
    greatest_increase_date = dates[changes_in_profit_losses.index(greatest_increase)]       #

    gratest_decrease = min(changes_in_profit_losses)
    greatest_decrease_date = dates[changes_in_profit_losses.index(greatest_increase)]


# print the financial analysis result
print("financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f'Greatest Increase In Profit: {greatest_increase_date} ${greatest_increase}')
print(f"Greatest Decrease In Profit: {greatest_decrease_date} ${gratest_decrease}")

#printing to text file
with open(file_path, "w") as text_file:
    output = (
"Financial analysis\n"
"---------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit_losses}\n"
f"Average change: ${round(average_change, 2)}\n"
f"Greatest Increse In Profits: {greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrese In Profits: {greatest_decrease_date} (${gratest_decrease})\n")










































































   