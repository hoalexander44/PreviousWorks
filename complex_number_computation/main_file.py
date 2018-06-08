#This program allows for the computation of complex number (ones that include the imaginary number i )
from complex import complex_number
import sys

#the first function
def a(c,k):
    temp_output = complex_number(1,0)
    a=""
    summation_list = []
    original_object = c
    store_object = complex_number(1,0)
    a = ""
    for exp in range (1,k+1):
        temp_output = original_object ** exp
        a = temp_output + store_object
        store_object = store_object.output_to_complex(a)
    return (a)

#The second function
def b(c,k):
    one_value = complex_number(1,0)
    tophalf = c**(k+1)
    final_top_half = one_value - tophalf
    object_top_half = complex_number(1,0)
    object_top_half = object_top_half.output_to_complex(final_top_half)
    final_bottom_half = one_value - c
    object_bottom_half = complex_number(1,0)
    object_bottom_half = object_bottom_half.output_to_complex(final_bottom_half)
    return (object_top_half/object_bottom_half)
        
        
k = int(sys.argv[3])
real_number = int(sys.argv[1])
imaginary_number = int(sys.argv[2])

num = complex_number(real_number,imaginary_number)
print(a(num,k))
print(b(num,k))