import argparse
from xml.etree.ElementTree import parse

parser = argparse.ArgumentParser()


def xml_from_file(file_path):
    tree = parse(file_path)
    print(
        "{} has {} lines.".format(
            file_path,
            len(list(tree.find("./packages/package/classes/class/lines"))),
        )
    )
    return tree


if __name__ == "__main__":
    parser.add_argument("file1", help="first file to check")
    parser.add_argument("file2", help="second file to check")
    args = parser.parse_args()
    print("Hello, PyCharm")
    xml1 = xml_from_file(args.file1)
    print("{}".format(args.file1))
    xml2 = xml_from_file(args.file2)
    print("{}".format(args.file2))
