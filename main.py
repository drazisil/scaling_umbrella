import argparse

from scaling_umbrella import BaseReport

parser = argparse.ArgumentParser()

if __name__ == "__main__":
    parser.add_argument("file1", help="first file to check")
    parser.add_argument("file2", help="second file to check")
    args = parser.parse_args()
    print("Hello, PyCharm")
    b1 = BaseReport()
    xml1 = b1.report_from_file(args.file1)
    print("{}".format(args.file1))
    b2 = BaseReport()
    xml2 = b2.report_from_file(args.file2)
    print("{}".format(args.file2))
