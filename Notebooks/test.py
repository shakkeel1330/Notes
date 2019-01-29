my_func = " 
def function(a,b):
   constant = {input_var}
   return a*b + constant
"
my_func.format(input_var = 5)

exec(my_func)
function(1,2)