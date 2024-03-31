"""
Author: Dinh Le
Created Date: 2024-03-31

About: Tests for Open Maya API functionality.
"""

import unittest

from maya import cmds as m

from modules.utils.open_maya_api import toMObject, toDependencyNode

from maya import OpenMaya

class Test_OpenMayaAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.jointName = "L_hand_JNT"
        self.joint = m.joint(n=self.jointName)

        self.baseGrp = m.group(n="base_GRP", em=1)
        self.subGrp = m.group(n="sub_GRP", em=1)
        m.parent(self.subGrp, self.baseGrp)
        m.parent(self.joint, self.subGrp)

    def tearDown(self) -> None:
        m.delete(self.baseGrp)

    def test_toDependencyNode(self):
        expectedResult = "joint"

        result = toDependencyNode(self.jointName)
        nodeTypeName = result.typeName()

        self.assertEqual(nodeTypeName, expectedResult)

    def test_toMObject(self):
        expectedResult = "|base_GRP|sub_GRP|L_hand_JNT"

        result = toMObject(self.jointName)
        fullPathName = OpenMaya.MFnDagNode(result).fullPathName()

        self.assertEqual(fullPathName, expectedResult)


if __name__ == "__main__":
    unittest.main()