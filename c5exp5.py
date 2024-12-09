from graphics.rectangle import area as rect_area, perimeter as rect_perim
from graphics.circle import area as circ_area, perimeter as circ_perim
from graphics.the3d_figs.cuboid import area as cube_area, volume as cube_v
from graphics.the3d_figs.sphere import area as sphere_area,volume as sphere_v


print("Rectangle Area:",rect_area(5,3))
print("Rectangle Perimeter:",rect_perim(5,3))

print("Circle:",circ_area(4))
print("Circle Perimeter:",circ_perim(4))

print("Cuboid Area:", cube_area(2,3,4))
print("Cuboid Perimeter:", cube_v(2,3,4))

print("Sphere Area:", sphere_area(6))
print("Sphere perimeter:",sphere_v(6))



