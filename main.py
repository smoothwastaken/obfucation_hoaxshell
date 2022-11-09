import argparse


class Obfuscator(object):

    def __init__(self, args: list) -> None:
        self.args = args

    def chimera_obfucation(self) -> None:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Optional argument flag which defaults to False
    parser.add_argument("-l", "--level", action="store_true", default="4")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-f", "--file_path", action="store", dest="file")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()

    obfucator = Obfuscator("")
