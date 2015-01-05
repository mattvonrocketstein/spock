""" spock.bin.spock
"""

def entry():
    namespace={}
    exec('from spock import *', namespace)
    print 'publishing these names: ', namespace.keys()
    try:
        from IPython import start_ipython
        start_ipython(user_ns=namespace)
    except ImportError:
        raise SystemExit("ERROR: spock's shell requires IPython to be installed.")
