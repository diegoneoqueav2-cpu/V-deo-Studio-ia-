import bpy
from mathutils import Vector
from studio import import_product
def load_product(path,height=3):
 before=set(bpy.data.objects)
 import_product(path)
 objects=[o for o in bpy.data.objects if o not in before]
 meshes=[o for o in objects if o.type=='MESH']
 if not meshes:raise ValueError('No mesh in product')
 bpy.context.view_layer.update()
 corners=[o.matrix_world@Vector(c) for o in meshes for c in o.bound_box]
 lo=Vector(tuple(min(v[i] for v in corners) for i in range(3)))
 hi=Vector(tuple(max(v[i] for v in corners) for i in range(3)))
 root=bpy.data.objects.new('Product controller',None);bpy.context.collection.objects.link(root)
 for o in objects:
  if o.parent not in objects:
   world=o.matrix_world.copy();o.parent=root;o.matrix_world=world
 extent=max(hi-lo)
 if extent<=0:raise ValueError('Invalid product dimensions')
 scale=height/extent
 root.scale=(scale,)*3;root.location=-(lo+hi)*.5*scale
 return root
