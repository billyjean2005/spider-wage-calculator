# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# variable_declaration 
number_of_hours=32
hourly_rate=200
total_wage=0
overtime_wage=0
overtime_hours=12


# calculating total wage 

total_wage=hourly_rate*number_of_hours 

# displaying results 

print('gross wage;',total_wage)

# calculating overtime wage
overtime_wage=overtime_hours*2*hourly_rate 
# calculating total wage 

total_wage=hourly_rate*number_of_hours + overtime_wage

#displaying results
print('overtime wage;',overtime_wage)
print('gross wage;', total_wage)



