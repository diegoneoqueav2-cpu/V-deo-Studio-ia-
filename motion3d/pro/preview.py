import sys, os, bpy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from studio import lighting, quality, camera_motion, import_product
from assets import poly_hdri, ambient_material
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
hdri=poly_hdri()
texture_zip=ambient_material()
print('Downloaded material archive:',texture_zip)
# Neutral test object, not a representation of a commercial phone.
bpy.ops.mesh.primitive_uv_sphere_add(segments=64,ring_count=32)
o=bpy.context.object
for p in o.data.polygons:p.use_smooth=True
m=bpy.data.materials.new('Studio test metal');m.use_nodes=True
p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.6,.18,.04,1);p.inputs['Metallic'].default_value=.8;p.inputs['Roughness'].default_value=.22;o.data.materials.append(m)
bpy.ops.object.camera_add();cam=bpy.context.object;cam.data.lens=48;bpy.context.scene.camera=cam
camera_motion(cam,'hero',.6)
lighting('premium',hdri);quality(False)
s=bpy.context.scene;s.render.image_settings.file_format='PNG';s.render.filepath=os.path.abspath('studio-preview.png');bpy.ops.render.render(write_still=True)
