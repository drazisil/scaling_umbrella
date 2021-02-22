from defusedxml.ElementTree import parse


class BaseReport:
    def __init__(self):
        pass

    def report_from_file(self, file_path):
        self.xml_tree = parse(file_path)
        lines = self.xml_tree.find("./packages/package/classes/class/lines")
        if not lines:
            raise ValueError("Empty lines object")
        lines_list = list(lines)
        print(
            "{} has {} lines.".format(
                file_path,
                len(lines_list),
            )
        )
        return self.xml_tree
