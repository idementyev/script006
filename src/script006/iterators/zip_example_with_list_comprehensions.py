import cProfile
from zip_example import with_list_comprehensions, process

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    result3 = with_list_comprehensions()
    for value in result3:
        process(value)
    profiler.disable()
    profiler.print_stats()



"""
(venv) [12:02:45]mkoshel@Mkoshel-lws ~/BACKUPSFROMMINT/home/mkoshel/dev/script006.git/src/script006/iterators [master]$ /usr/bin/time -v python zip_example_with_list_comprehensions.py 
         50000003 function calls in 13.723 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.832   10.832 zip_example.py:16(with_list_comprehensions)
        1   10.832   10.832   10.832   10.832 zip_example.py:18(<listcomp>)
 50000000    2.891    0.000    2.891    0.000 zip_example.py:20(process)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


        Command being timed: "python zip_example_with_list_comprehensions.py"
        User time (seconds): 22.49
        System time (seconds): 1.92
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:24.43
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 6750788
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 1686485
        Voluntary context switches: 2
        Involuntary context switches: 124
        Swaps: 0
        File system inputs: 48
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

"""

