import argparse

class ArgParser:
    """Varbl from cmd line arg"""
    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(description="Great Description To Be Here")

        parser.add_argument('l', '--load',
                            dest='load', nargs='+',
                            metavar='filename',
                            help='load obj from files')
        parser.add_argument('d', '--dump',
                            dest='dump', nargs='+',
                            metavar='filename:object:filetype',
                            help='dump obj from files')
        parser.add_argument('c', '--convert',
                            dest='convert', nargs='+',
                            metavar='filename filetype',
                            help='convert')
        return parser

    @staticmethod
    def parse():
        parser = ArgParser.get_parser()
        return parser.parse_args()

    @staticmethod
    def get_args():
        """Return command args."""
        args = ArgParser.parse()
        return (args.dump, args.load, args.convert)

    @staticmethod
    def print_help():
        """Print cmd help"""
        parser = ArgParser.get_parser()
        parser.print_help()
