# **************************************************************************************************************************************************************************************************** #
# ******************************************************************************* 2.	To simulate Half-Adder Circuit  ****************************************************************************** #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Testings have been logged into the terminal for future debuggings.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



MSB = 1                                                         # For storing the MSB(Most Significant Bit) of the Input Signal
LSB = 1                                                         # For storing the LSB(Least Significant Bit) of the Input Signal
bits = [MSB, LSB]                                               # For storing the complete(both MSB and LSB bits) Input Signal



# **************************************************************************************** Section ends here **************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ****************************************************************************** Calculation of Half Binary Addition  ******************************************************************************* #



def halfAdder(bits):                                                         # For performing the Half-Binary Addition
    if str(bits[0]) + str(bits[1]) in ('00', '01', '10', '11'):
        return {'Carry': bits[0] & bits[1], 'Sum': bits[0] ^ bits[1]}
    else:
        print('Not a Valid Binary Number')

# Testing-
bin_add = halfAdder(bits)
print(f'Binary_Half_Addition({bits[0]}, {bits[1]}) =', bin_add)



# ********************************************************************************* Section ends here *********************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




