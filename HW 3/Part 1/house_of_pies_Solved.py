# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = input("Which would you like? ")
    #print (pie_choice)

    # Get index of the pie from the selected number
    pie_pick = int(pie_choice)-1

    # Add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases[pie_pick] += 1

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[pie_pick] + " right out for you.")

    # Provide exit option
    leave = input("Do you want to abandon your purchase? (y/n)")

    if leave == "y":
        pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        break
    else:

    #    Prompt the user if they would like to make another purchase
        shopping = input("Would you like to make another purchase (y)es or (n)o?")
        

# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
# Gather the count of each pie in the pie list and print them alongside the pies
length = len(pie_list)
for i in range(length):
    print(pie_list[i] + "   " + str(pie_purchases[i]))

