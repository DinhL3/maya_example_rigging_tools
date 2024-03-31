"""
Author: Dinh Le
Created Date: 2024-03-31

About: Tests for the Dep Node functionality.
"""

import unittest

from maya import cmds as m

from modules.nodel import Dep_Node


class Test_Dep_Node(unittest.TestCase):
    def setUp(self) -> None:
        self.sphereName = "sphere_GEO"
        self.jointName = "sphere_JNT"

        # Add the nodeType argument when creating Dep_Node instances
        self.sphere = Dep_Node(m.polySphere(n=self.sphereName)[0])
        self.object = Dep_Node(self.sphereName)

        m.select(cl=1)

        self.joint = Dep_Node(m.joint(n=self.jointName))

    def tearDown(self) -> None:
        if m.objExists(self.sphereName):
            m.delete(self.sphereName)

        if m.objExists(self.jointName):
            m.delete(self.jointName)

    def test_dep_node__str__(self):
        self.assertEqual(str(self.sphere), self.sphereName)

    def test_dep_node__repr__(self):
        self.assertEqual(
            self.sphere.__repr__(),
            "Dep_Node('sphere_GEO')"
        )

    def test_dep_node__eq__(self):
        self.assertEqual(self.sphere, self.object)
        self.assertEqual(self.sphere.fullPath, self.object.fullPath)
        self.assertEqual(self.sphere.path, self.object.path)

    def test_dep_node_node_getter(self):
        self.assertEqual(self.sphere.node, self.sphereName)
        self.assertEqual(self.joint.node, self.jointName)
        self.assertNotEqual(self.joint.node, self.sphereName)

    def test_dep_node_setter(self):
        self.sphere.node = self.jointName
        self.assertEqual(self.sphere.node, self.jointName)


if __name__ == "__main__":
    unittest.main()
