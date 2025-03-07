"""

Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
 

A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

The result format is in the following example.


Example 1:

Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+

Output: 
+-----+
| num |
+-----+
| 6   |
+-----+

Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.

Example 2:

Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+

Output: 
+------+
| num  |
+------+
| null |
+------+

Explanation: There are no single numbers in the input table so we return null.

"""

# First, group the numbers and filter out those that appear more than once.
# Next, identify the maximum value among the remaining unique numbers.
# Finally, return the result as a DataFrame with a single column.


import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:

    # 1. Filter numbers that appear only once
    unique_numbers = my_numbers.groupby('num').filter(lambda x: len(x) == 1)
    
    # 2. Find the maximum of those numbers
    max_value = unique_numbers['num'].max()
    
    return pd.DataFrame({'num': [max_value]})

