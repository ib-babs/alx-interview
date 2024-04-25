# PASCAL TRIANGLE
Useful in Binomial coefficient for solving problems such as Quadratic Expression etc. 
*ALX Interview*

## Structure
Addition of each element in the previous/above array with the next element
1   
1   1   
1   2   1
1   3   3   1
1   4   6   4   1
1   5   10  10  5   1  
...

## ALGORITHM
*n* is the number to process Pascal Triangle 
- Preloop variables and condition
    + Check *n > 0* return empty list if *false* 
    + lpd = [[] loop in range of n to created empty lists of n length]

1- Loop *i* in range of *n* 
    Use *i* to traverse *lpd* sublists and append *1*
    + Loop *j* in range of *(i-1)*: 
        _i will be equal to 2 here_ 
        + Use ith to traverse *lpd* sublists and append *(lpd_previous_sublist\[i-1][j] + lpd_previous_sublist\[i-1][j+1])*
        - If *i* is greater than 0:
            _So that the first sublist in lpd won't have two values_
            + Append int *1* to other sublists 

Author: *Babatunde Ibrahim*