"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
#d = 33000000000 #elons debt
p = 33000000000 #principle amount
n = 10 #years
r1 = 0.0396 #10-year interest rate
r2 = 0.0432 #20-year interest rate


ten_year_final = p * (1 + r1) ** n
n += 10
print(ten_year_final)

twenty_year_final = p * (1 + r2) ** n
print(twenty_year_final)


# final answer for 10-year
ten_year_final = ten_year_final
#print('10-year final value:', ten_year_final)

# final answer for 20-year
twenty_year_final = twenty_year_final
#print('20-year final value:', twenty_year_final)

n -= 10

def compound_interest(p, r, n):

    amount = p * (1 + r) ** n
    return amount

val1 = compound_interest(p, r1, n)

print("10y value: ", val1)

val2 = compound_interest(p, r2, n + 10)

print("20y value: ", val2)