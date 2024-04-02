import maya.cmds as m
from modules.nodel import Dep_Node

# create a sphere

sphereName = "our_sphere"
sphereNode = m.polySphere(n=sphereName)[0]

# create a dep_node object for the sphere
sphere = Dep_Node(sphereNode)

# access the properties of the sphere
print("Sphere Name:", sphere.name)
print("Sphere Path:", sphere.fullPath)
print("Sphere type:", sphere.type)

# rename
newName = "newly_named_sphere"
sphere.rename(newName)

# lock
sphere.lock(True)
if sphere.isLocked:
    print("Sphere is locked")
else:
    print("Sphere is not locked")

# unlock then delete
sphere.lock(False)
sphere.delete()
if sphere.exists():
    print("Sphere still exists")
else:
    print("Sphere has been deleted")
