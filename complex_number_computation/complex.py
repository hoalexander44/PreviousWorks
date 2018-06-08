
            
class complex_number():
    #inital attributes and string representation
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def __str__(self):
        sign = "+"
        if self.__y < 0:
            sign = ""
        elif self.__y>=0:
            sign = "+"
        return(str(self.__x) + sign +str(self.__y)+"i")
#methods of complex_number object returns string so in order to further manipulate the result, they must be turned back into complex_number objects
    def output_to_complex(self,st_out):
        convert_string = []
        record_keeper = "-"
        #If there is a negative sign in front
        if ("-") == st_out[0]:
            convert_string = st_out.split("-")
            del convert_string[0]
            if ("+") in convert_string[0]:
                record_keeper = "+"
                convert_string[0] = convert_string[0].split("+")
                convert_string = convert_string[0]
            convert_string[0] = "-" + convert_string[0]
            convert_string[1] = convert_string[1].split("i")
            convert_string[1]=convert_string[1][0]
            if record_keeper == "-":
                convert_string[1] = "-"+ convert_string[1]
        #if there are only plus signs
        elif ("+") in st_out:
            convert_string = st_out.split("+")
            convert_string[1] = convert_string[1].split("i")
            convert_string[1]=convert_string[1][0]
        #if there is a minus sign in the middle
        else:
            convert_string = st_out.split("-")
            convert_string[1] = convert_string[1].split("i")
            convert_string[1]=convert_string[1][0]
            if record_keeper == "-":
                convert_string[1] = "-"+ convert_string[1]
        #creates a new object based on the components of the convert_string list
        output_object = complex_number(int(convert_string[0]),int(convert_string[1]))
        return(complex_number(int(convert_string[0]),int(convert_string[1])))
    #accessor methods
    def getReal(self):
        return(self.__x)
    def getImaginary(self):
        return(self.__y)
    #math methods
    def __add__(self,other):
        real_number = (self.__x + other.__x)
        imaginary_number = (self.__y + other.__y)
        sign = "+"
        #section where the middle plus or minus sign will be changed according to the negative or positive quality of the imaginary number
        #this repeats for each math method
        if imaginary_number < 0:
            sign = ""
        elif imaginary_number >=0:
            sign = "+"
        return (str("%d"+sign+"%di") %(real_number,imaginary_number))
    def __sub__(self,other):
        real_number = (self.__x - other.__x)
        imaginary_number = (self.__y - other.__y)
        sign = "+"
        if imaginary_number < 0:
            sign = ""
        elif imaginary_number >=0:
            sign = "+"
        return (str("%d"+sign+"%di") %(real_number,imaginary_number))
    def __mul__(self,other):
        real_number = (self.__x * other.__x) - (self.__y*other.__y)
        imaginary_number = (self.__x * other.__y) + (self.__y*other.__x)
        sign = "+"
        if imaginary_number < 0:
            sign = ""
        elif imaginary_number >=0:
            sign = "+"
        return (str("%d"+sign+"%di") %(real_number,imaginary_number))
    def __truediv__(self, other):
        division_number = (((self.__x *other.__x) + (self.__y*other.__y))/((other.__x*other.__x)+(other.__y*other.__y)))
        imaginary_number = ((-(self.__x *other.__y) + (self.__y*other.__x))/((other.__x*other.__x)+(other.__y*other.__y)))
        sign = "+"
        if imaginary_number < 0:
            sign = ""
        elif imaginary_number >=0:
            sign = "+"
        return (str("%.2f"+sign+"%.2fi") %(division_number,imaginary_number))
    #unlike the other methods, pow actually returns an object that represents the result of the power
    def __pow__(self,other):
        og_num = self
        new_num =""
        empty_object = og_num
        #if raised to the 0 power
        if (other ==0):
            return ("1")
        #if raised to the 1st power
        elif (other ==1):
            return(og_num)
        #if raised to the 2nd power OR HIGHER
        elif (other ==2):
            return(self.output_to_complex(og_num*og_num))
        else:
            for x in range(0,other-1):
                new_num = empty_object * og_num
                empty_object = self.output_to_complex(new_num)
            
        return(empty_object)

#if main file test
if __name__=="__main__":
    a = complex_number(4,3)
    b = complex_number(2,8)
    print(a)
    print(a+b)
    print(a*b)
    print(a/b)
    print((a**3))
