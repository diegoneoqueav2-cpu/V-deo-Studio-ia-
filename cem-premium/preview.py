import bpy, math
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
s=bpy.context.scene
s.render.engine='CYCLES'
s.cycles.samples=12
s.render.resolution_x=540
s.render.resolution_y=960
s.render.resolution_percentage=100
s.render.fps=30
s.frame_end=150
def mat(n,c,m=0):
 a=bpy.data.materials.new(n); a.diffuse_color=(*c,1); a.use_nodes=True
 p=a.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*c,1); p.inputs['Metallic'].default_value=m; p.inputs['Roughness'].default_value=.28
 return a
white=mat('White',(.95,.95,.95),.25)
gold=mat('Yellow',(1,.65,.015),.45)
green=mat('Emerald',(.008,.18,.055),.15)
def aim(o,p): o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(0,-12,0))
cam=bpy.context.object; aim(cam,(0,0,0)); s.camera=cam; cam.data.lens=43
cam.data.dof.use_dof=True; cam.data.dof.focus_distance=12; cam.data.dof.aperture_fstop=4
bpy.ops.mesh.primitive_plane_add(size=200,location=(0,4,0),rotation=(math.pi/2,0,0))
bpy.context.object.data.materials.append(green)
for loc,power,color,size in [((-4,-5,6),1800,(.8,1,.9),5),((4,-2,2),1200,(1,.8,.35),3),((0,2,5),2200,(.1,1,.4),4)]:
 bpy.ops.object.light_add(type='AREA',location=loc); o=bpy.context.object; o.data.energy=power; o.data.color=color; o.data.shape='DISK'; o.data.size=size; aim(o,(0,0,0))
def word(body,z,width,material,start,end):
 bpy.ops.object.text_add(location=(0,0,z),rotation=(math.pi/2,0,0))
 o=bpy.context.object; o.data.body=body; o.data.align_x='CENTER'; o.data.align_y='CENTER'; o.data.extrude=.08; o.data.bevel_depth=.025; o.data.materials.append(material)
 bpy.context.view_layer.update(); k=width/max(o.dimensions.x,.01)
 for f,scale,x,y in [(1,0,0,0),(max(1,start-1),0,0,0),(start+8,k,0,0),(end-8,k,0,0),(end,0,4,-2)]:
  o.scale=(scale,)*3; o.location=(x,y,z); o.keyframe_insert('scale',frame=f); o.keyframe_insert('location',frame=f)
 return o
word('BLACK',1,4,white,1,45)
word('FRIDAY',-.2,4.5,gold,5,45)
word('CHEGOU AQUI NO CEM',-1.5,4.5,white,9,45)
word('PRIMEIRO ANO',1,4.5,white,46,100)
word('DO ENSINO',0,4.5,gold,50,100)
word('FUNDAMENTAL',-1,4.5,gold,54,100)
word('MEGA',0,4.5,white,101,125)
word('DESCONTO',0,4.5,white,126,150)
for i in range(6):
 o=word('%',(-1)**i*2.5,1,gold,101,150)
 for f in (101,125,150):
  a=i*math.pi/3+(f-101)*.06; o.location=(2.6*math.cos(a),1+math.sin(a),3*math.sin(a)); o.rotation_euler=(math.pi/2,a,a); o.keyframe_insert('location',frame=f); o.keyframe_insert('rotation_euler',frame=f)
s.render.image_settings.file_format='PNG'
s.render.filepath='frames/'
bpy.ops.wm.save_as_mainfile(filepath='cem-preview.blend')
bpy.ops.render.render(animation=True)
