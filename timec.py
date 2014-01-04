#!/usr/bin/python
import argparse
from os         import path, devnull
from sys        import argv, stderr, stdout
from subprocess import call
from time       import time
from numpy      import mean, std, linspace
from math       import floor

COMPILER = "gcc"

DESCRIP_PROG = "Time your C program."

HELP_NUMTRIALS = """
the number of execution time trials you would like to run (default: 100)
"""

HELP_OPTIMIZE = """
desired GCC optimization flag level (0, 1, 2, or 3)
(default: 0, i.e. non-existent)
"""

IS_VERBOSE = False

def compile_c(prog_name, prog_path, optimize_lvl):
    if int(optimize_lvl)==0:
        call([COMPILER, "-o", prog_name, prog_path])
    else:
        call([COMPILER, "-O"+str(optimize_lvl), "-o", prog_name, prog_path])

def retrieve_exec_time_stats(prog_name, prog_path, num_trials, optimize_lvl):
    prog_basename = path.splitext(path.basename(prog_name))[0]
    
    compile_c(prog_basename, prog_path, optimize_lvl)
    
    exec_times = []
    for i in range(num_trials):
        # TODO: make this verbosity set-able from timec_stats
        if IS_VERBOSE:
            stdout.flush()
            stdout.write("\rTrial number: " + str(i+1)) # ticker

        begin_time   =  time()        
        call(["./"+prog_basename], stdout=open(devnull, "w"))
        end_time     =  time()

        exec_times.append((end_time - begin_time)*1000)
    stdout.write("\n")
        
    call(["rm", prog_basename])
    
    return {"mean": mean(exec_times), "stdev": std(exec_times)}
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIP_PROG)
    parser.add_argument("-n", type=int, default=100, help=HELP_NUMTRIALS,
                        dest="num_trials") 
    parser.add_argument("-o", type=int, default=0, help=HELP_OPTIMIZE,
                        choices=[0,1,2,3], dest="optimize_lvl")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true")
    parser.add_argument("sourcepath", metavar="<source path>")

    args = parser.parse_args()
    if args.verbose:
        IS_VERBOSE = True
        
    print(retrieve_exec_time_stats(path.basename(args.sourcepath),
                                   args.sourcepath, args.num_trials,
                                   args.optimize_lvl))
