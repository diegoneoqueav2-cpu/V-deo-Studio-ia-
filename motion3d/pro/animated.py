import bpy,sys,os,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from studio import lighting,quality,camera_motion
from cinematic import cinematic,animate_product
from products import load_product
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
model=os.environ.get('PRODUCT_MODEL','')
if model:
 o=load_product(str(Path(model).resolve()))
else:
 bpy.ops.mesh.primitive_torus_add(major_radius=1,minor_radius=.35,major_segments=64,minor_segments=24)
 o=bpy.context.object
 m=bpy.data.materials.new('Purple metal');m.diffuse_color=(.32,.08,.65,1);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.32,.08,.65,1);p.inputs['Metallic'].default_value=.75;p.inputs['Roughness'].default_value=.24;o.data.materials.append(m)
 for p in o.data.polygons:p.use_smooth=True
bpy.ops.object.camera_add();cam=bpy.context.object;bpy.context.scene.camera=cam
lighting('premium');quality(True);cinematic(cam,o)
s=bpy.context.scene;s.render.fps=30;s.frame_start=1;s.frame_end=90;s.cycles.samples=16
animate_product(o,90)
for f in range(1,91):
 camera_motion(cam,'orbit_left',(f-1)/89)
 cam.keyframe_insert(data_path='location',frame=f);cam.keyframe_insert(data_path='rotation_euler',frame=f)
s.render.image_settings.file_format='PNG';s.render.filepath=os.path.abspath('frames/')+'/'
bpy.ops.render.render(animation=True)
