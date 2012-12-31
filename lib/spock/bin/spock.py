""" spock.bin.spock
"""

def entry():
    namespace={}
    exec('from spock import *', namespace)
    print 'publishing these names: ', namespace.keys()
    try:
        from IPython import Shell; Shell.IPShellEmbed(user_ns =namespace, argv=['-noconfirm_exit'])()
    except ImportError:
        raise SystemExit("spock's shell reuqires IPython to be installed.")
