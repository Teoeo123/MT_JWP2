import numpy as np

class Vector3D:
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self) -> str:
        return "Vector3D({},{},{})".format(self.x, self.y, self.z)
    def norm(self):
        return np.sqrt(self.x**2+self.y**2+self.z**2)
    def __add__(self, sVector):
        return Vector3D(self.x+sVector.x, self.y+sVector.y, self.z+sVector.z)
    def __sub__(self, sVector):
        return Vector3D(self.x-sVector.x, self.y-sVector.y, self.z-sVector.z)
    def __mul__(self,a):
        return Vector3D(self.x*a, self.y*a, self.z*a)
    def dot(self,sV):
        return self.x* sV.x + self.y* sV.y + self.z* sV.z
    def cross(self, sV):
        return Vector3D(self.y * sV.z - self.z*sV.y, self.z * sV.x - self.x* sV.z, self.x * sV.y - self.y* sV.x)
    def are_orthogonal(self, sV):
        return (self.dot(sV) == 0)
a = Vector3D(1,2,3)
b= Vector3D(3,2,1)
print(a)
a.x = 3
print(a.x)
print(a.norm())
print(a,'+',b,'=',a + b)
print(a,'-',b,'=',a - b)
print(a,'*',4,'=',a*4)
print('iloczyn skalarny ab:', a.dot(b))
print('iloczyn wektorowy ab:', a.cross(b))
print('Ortogonalne ab:', a.are_orthogonal(b))
