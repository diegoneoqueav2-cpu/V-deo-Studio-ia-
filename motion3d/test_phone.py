import bpy, math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
def mat(n,c,m=0,r=.3):
 a=bpy.data.materials.new(n); a.diffuse_color=(*c,1); a.use_nodes=True
 p=a.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*c,1); p.inputs['Metallic'].default_value=m; p.inputs['Roughness'].default_value=r
 return a
metal=mat('Orange metal',(.8,.18,.035),.75); glass=mat('Lens',(.012,.018,.035),.55,.13)
root=bpy.data.objects.new('Phone',None); bpy.context.collection.objects.link(root)
def cube(n,loc,dim,ma,bevel,parent=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=n; o.dimensions=dim; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma)
 b=o.modifiers.new('Rounded edges','BEVEL'); b.width=bevel; b.segments=6; o.modifiers.new('Normals','WEIGHTED_NORMAL'); o.parent=parent; return o
cube('Body',(0,0,0),(1.5,.18,3),metal,.08,root)
cube('Screen',(0,-.1,0),(1.4,.035,2.9),glass,.017,root)
cube('Camera island',(0,.12,1),(1.38,.13,.8),metal,.06,root)
for x,z in [(-.43,1.2),(.03,1),(-.43,.78)]:
 for rad,y,ma in [(.21,.21,metal),(.17,.25,glass)]:
  bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=rad,depth=.07,location=(x,y,z),rotation=(math.pi/2,0,0)); o=bpy.context.object; o.data.materials.append(ma); o.parent=root
for f,a in [(1,0),(120,360)]:
 root.rotation_euler=(.12,0,math.radians(a)); root.keyframe_insert(data_path='rotation_euler',frame=f)
for fc in root.animation_data.action.fcurves:
 for k in fc.keyframe_points:k.interpolation='LINEAR'
def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(4,-7,2)); cam=bpy.context.object; aim(cam,(0,0,0)); cam.data.type='ORTHO'; cam.data.ortho_scale=5.5
s=bpy.context.scene;s.camera=cam
for loc,power,size in [((4,-4,5),900,5),((-4,2,3),1100,4),((0,4,-1),700,3)]:
 bpy.ops.object.light_add(type='AREA',location=loc); o=bpy.context.object;o.data.energy=power;o.data.shape='DISK';o.data.size=size;aim(o,(0,0,0))
s.world.color=(.15,.035,.28)
s.render.engine='CYCLES';s.cycles.samples=12
s.render.resolution_x=540;s.render.resolution_y=960;s.render.resolution_percentage=100;s.render.fps=24;s.frame_end=120
s.render.image_settings.file_format='PNG';s.render.filepath='//frames/'
bpy.ops.render.render(animation=True)
