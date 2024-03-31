"""
Author: Dinh Le
Created Date: 2024-03-30

About: A utility function that facilitates the conversion of
    Maya Nodes into various API objects like "MObject" and "MDagPath".
"""

from maya import OpenMaya


def toDependencyNode(node):
    """
        Convert a node into an OpenMay Dependency Node

        Args:
            node (str): The maya node.

        Returns:
            object: The OpenMaya Dependency Object.

        Example:
              name = "L_hand_JNT"
              obj = toDependencyNode(name)
              print(obj.typeName())
              # Output: joint
    """
    obj = toMObject(node)
    return OpenMaya.MFnDependencyNode(obj)


def toMObject(node):
    """
        Convert a node into an OpenMaya Object.

        Args:
            node (str): The maya node.

        Returns:
            object: The OpenMaya Object.

        Example:
                name = "L_hand_JNT"
                obj = toMObject(name)
                print(obj.fullPathName())
                # Output: |BASE_GRP|SUB_GRP|L_hand_JNT
    """
    selectionList = OpenMaya.MSelectionList()
    selectionList.add(node)
    obj = OpenMaya.MObject()
    selectionList.getDependNode(0, obj)
    return obj
