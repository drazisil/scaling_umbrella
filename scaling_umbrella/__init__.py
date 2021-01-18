from defusedxml.ElementTree import parse

from scaling_umbrella.BaseReport import BaseReport


def report_from_file(file_path):
    xml_tree = parse(file_path)
    lines = list(xml_tree.find("./packages/package/classes/class/lines"))
    if not lines:
        raise Exception("Empty lines object")
    print(
        "{} has {} lines.".format(
            file_path,
            len(lines),
        )
    )
    return xml_tree
