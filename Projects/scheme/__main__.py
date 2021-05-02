from scheme_reader import *
from scheme import *
from scheme_builtins import *
from buffer import  *

env = create_global_frame()
make_let_frame(read_line("((x 5))"), env)
