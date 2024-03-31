"""
Author: Dinh Le
Created Date: 2024-03-29

About: String functionality for Maya object paths
"""


def generateReprString(cls, name):
    """
    Generates the string representation for the __repr__ dunder method.

    Args:
        cls (str): The cls.__name__ of the class.
        name (str): The node used

    Returns:
        str: The string representation for the __repr__ special method.

    Example:
          __repr__ = generateReprString(
            self.__class__.__name__,
            self.fullPath
          )
          Output: Dep_Node('sphere_GRP')
    """
    return "{cls}('{node}')".format(cls=cls, node=rootName(name))


def rootName(name):
    """
        Strips grouping information from a given full path.

        Args:
            name (str): The name containing group info

        Returns:
            str: The name without group info

        Example:
              name = "base_GRP|sub_GRP|namespace:sphere_GEO"
              rootName(name)
              Output: "namespace:sphere_GEO"
    """
    if not name:
        return name

    return name.rpartition("|")[-1]


def baseName(name):
    """
        This function strips the namespaces and grouping info of a name.
        Useful when working with full paths but needing the base for naming.

        Args:
            name (str): The name containing group info

        Returns:
            str: The name without group info or namespace information

        Example:
              name = "namespace:baseGRP|namespace:subGRP|namespace:sphere_GEO"
              baseName(name)
              Output: "sphere_GEO"
    """
    if not name:
        return name

    return name.rpartition("|")[-1].rpartition(":")[-1]


def namespace(name):
    """
        Returns the namespace if any exists.

        Args:
            name (str): The name containing namespace information

        Returns:
            str: The namespace

        Example:
              name = "namespace:baseGRP|namespace:subGRP|namespace:sphere_GEO"
              namespace(name)
              Output: "namespace"
    """
    if not name:
        return name

    root = rootName(name)
    if ":" in root:
        return root.partition(":")[0]

    return ""
