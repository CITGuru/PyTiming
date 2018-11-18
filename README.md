*****
PyTiming
*****

A Python module for timing your python scripts execution time

*****
Installation
*****

PyPI (PIP)
######

::
    $ pip install pytiming

GitHub (Git)
######

::
    $ git clone https://github.com/CITGuru/PyTiming.git
    $ cd PyTiming
    $ python setup.py install


*****
Usage
*****

All you need to do is importing it in the script you want to time. Once the script stops, it prints out
the stop and elasped time.

Example ::
    import pytiming

    max_count = 100
    for x in range(0, max_count):
        print("Count: {}".format(x))

Output ::
    ========================================
    ('0:00:00.069', '-', 'End Program')
    ('Elapsed time:', '0:00:00.027')
    ========================================

*****
Contribution
*****

Send in your PRs

*****
Author
*****

Oyetoke Toby `http://medium.com/@oyetoketoby80 <http://medium.com/@oyetoketoby80/>``_