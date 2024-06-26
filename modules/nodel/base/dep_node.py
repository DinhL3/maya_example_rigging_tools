"""
Author: Dinh Le
Created Date: 2024-03-30

About: Dep Node functionality to deal with Maya base Nodes
    with no object dependency.
"""

from maya import cmds as m

from modules.utils import open_maya_api, path


class Dep_Node(object):
    """
        Class based way of calling all the info that we need to deal with
        in Maya from base nodes with no object dependency.

        Args:
            node (node/str): Takes either a ready-made base node or the name of one to create.
            nodeType (str): Used for creating a specified node type. (optional)

        Returns:
            object: The OpenMaya Dependency Object.

        Example:
              dep = Dep_Node("node_001")
              dep.rename("node_002")
                dep.delete()
    """
    def __init__(self, node, nodeType=None):
        self._dep = None
        self.node = node

        # Create on initiate if nodeType is passed
        if nodeType and not self.exists():
            self.create(nodeType)

    # ------------------------------------------------------------------

    def __str__(self):
        fullPath = self.fullPath
        if not fullPath:
            return "INVALID OBJECT"
        return fullPath

    def __repr__(self):
        return path.generateReprString(
            self.__class__.__name__,
            self.fullPath
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fullPath == other.fullPath
        elif self.fullPath == other:
            return True
        elif self.path == other:
            return True
        return False

    # ------------------------------------------------------------------

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, node):
        self._dep = None
        self._node = str(node) if node != None else None

        if not self.node or not m.objExists(self.node):
            return False

        self._dep = open_maya_api.toDependencyNode(self.node)
        return True

    # ------------------------------------------------------------------

    @property
    def dep(self):
        return self._dep

    @property
    def path(self):
        if self.dep:
            return self.dep.name()

    @property
    def fullPath(self):
        return self.path

    # ------------------------------------------------------------------

    def isReference(self):
        return m.referenceQuery(self.fullPath, isNodeReference=True)

    # ------------------------------------------------------------------

    def exists(self):
        if self.fullPath and m.objExists(self.fullPath):
            return True
        return False

    # ------------------------------------------------------------------

    @property
    def type(self):
        return self.dep.typeName()

    @property
    def typ(self):
        return self.type

    @property
    def name(self):
        return path.baseName(self.fullPath)

    @property
    def namespace(self):
        return path.namespace(self.fullPath)

    # ------------------------------------------------------------------

    def rename(self, name):
        m.rename(self, name)
        return self

    def lock(self, state=True):
        m.lockNode(self.fullPath, lock=state)

    @property
    def isLocked(self):
        return m.lockNode(self.fullPath, query=True, lock=True)[0]

    # ------------------------------------------------------------------

    def delete(self):
        if self.fullPath and m.objExists(self.fullPath):
            m.delete(self.fullPath)
        self._dep = None

    def create(self, nodeType):
        if self.fullPath:
            txt = ">>> This node already exists: \n\tName: \"{}\"\n\tType: {}".format(
                self.node,
                nodeType
            )
            raise ValueError(txt)

        self._dep = m.createNode(nodeType, n=self.node)
        return self

