from defusedxml.ElementTree import parse


def report_from_file(file_path):
    xml_tree = parse(file_path)
    lines = xml_tree.find("./packages/package/classes/class/lines")
    if not lines:
        raise Exception("Empty lines object")
    lines_list = list(lines)
    print(
        "{} has {} lines.".format(
            file_path,
            len(lines_list),
        )
    )
    return xml_tree
