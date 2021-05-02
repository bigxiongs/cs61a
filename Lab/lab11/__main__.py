from reader import read
from expr import  *
add_lambda = read('lambda x, y: add(x, y)').eval(global_env)
add_lambda.apply([Number(1), Number(2)])