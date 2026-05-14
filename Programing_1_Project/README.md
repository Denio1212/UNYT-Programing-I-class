# Personal Expense Tracker

* Project that allows users to track their daily expenses using file handling.
  * The project will save, update and retrieve expense records from a text file called "expensen.txt".

> ### Features Required:
>> * Adding a new expense to the file.
>> 
>>
>> * Viewing all expenses.
>> 
>> 
>> * Searching for expenses.
>>   * Filtered by date, category or a given range.
>>   
>> 
>> * Update an expense.
>> 
>>
>> * Delete an expense.
>>
>>
>> * Error Handling
>>   * Ensure correct input formats and handle missing files.

###
File Format ("expenses.txt") :

Date, Category, Amount, Description

2025-03-20,Food,12.50,Lunch at a café

2025-03-21,Transport,5.00,Bus ticket

2025-03-22,Entertainment,20.00,Movie night
###

> ### Advanced Features
>> * Monthly Expense Summary:
>>   * Total Spending per month
>>   * Find the most expensive category.
>>
>>
>> * Sorting Options:
>>   * Allow users to sort expenses by date, amount, or category.
>> 
>>
>> * Export to CSV/JSON:
>>   * Give users the option to export data as CSV or JSON files.
>>
>>
>> * Graphical Analysis:
>>   * Use Matplotlib to generate a bar chart of expenses by category
>>
>>
>> * Budgeting Feature:
>>   * Allow users to set a monthly budget and display a warning if they exceed it.