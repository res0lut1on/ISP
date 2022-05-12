import argparse

class ArgParcer:
    """Varbl from cmd line arg"""
    parcer = argparse.ArgumentParser(description="Great Description To Be Here")

    parcer.add_argument('l', '--load',
                        dest='load', nargs='+',
                        metavar='filename',
                        help='load obj from files')
    parcer.add_argument('d', '--dump',
                        dest='dump', nargs='+',
                        metavar='filename:object:filetype',
                        help='dump obj from files')
    parcer.add_argument('l', '--load',
                        dest='load', nargs='+',
                        metavar='filename',
                        help='load obj from files')