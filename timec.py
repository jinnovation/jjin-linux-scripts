#!/usr/bin/python
import argparse
from os         import path, devnull
from sys        import argv, stderr, stdout
from subprocess import call
from time       import time
from numpy      import mean, std, linspace
from math       import floor

def compile_c(prog_name, prog_path, optimize_lvl):
    if int(optimize_lvl)==0:
        call(["gcc", "-o", prog_name, prog_path])
    else:
        call(["gcc", "-O"+str(optimize_lvl), "-o", prog_name, prog_path])

def retrieve_exec_time_stats(prog_name, prog_path, num_trials, optimize_lvl):
    prog_basename = path.splitext(path.basename(prog_name))[0]
    
    compile_c(prog_basename, prog_path, optimize_lvl)
    
    exec_times = []
    for i in range(num_trials):
        # TODO: move this out to verbosity
        stdout.flush()
        stdout.write("\rTrial number: " + str(i+1)) # ticker

        begin_time   =  time()        
        call(["./"+prog_basename], stdout=open(devnull, "w"))
        end_time     =  time()

        exec_times.append((end_time - begin_time)*1000)
    stdout.write("\n")
        
    call(["rm", prog_basename])
    
    return {"mean": mean(exec_times), "stdev": std(exec_times)}
    
# if __name__ == "__main__":
#     help_num_trials = """
#     the number of execution time trials you would like to run (default: 100)
#     """
#     help_optimizelevel = """
#     desired GCC optimization flag level (default: 0, i.e. non-existent)
#     """

#     parser = argparse.ArgumentParser(description="Time your C program.")
#     parser.add_argument("-n", type=int, default=100, help=help_num_trials,
#                         dest="num_trials") 
#     parser.add_argument("-o", type=int, default=0, help=help_optimizelevel,
#                         dest="optimize_lvl")
#     parser.add_argument("-v", "--verbose", dest="verbose", action="store_true")
#     parser.add_argument("sourcepath", metavar="<source path>")

#     args = parser.parse_args()
#     if args.verbose:
#         pass # TODO
        
#     print(retrieve_exec_time_stats(path.basename(args.sourcepath),
#                                    args.sourcepath, args.num_trials,
#                                    args.optimize_lvl))
