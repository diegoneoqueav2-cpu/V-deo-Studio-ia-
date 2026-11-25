import bpy, math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
def mat(n,c,m=0,r=.3):
 a=bpy.data.materials.new(n); a.diffuse_color=(*c,1); a.use_nodes=True
 p=a.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*c,1); p.inputs['Metallic'].default_value=m; p.inputs['Roughness'].default_value=r
 return a
import os
def aim(o,p): o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
def cube(n,loc,dim,ma,bevel,parent=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=n; o.dimensions=dim; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma); b=o.modifiers.new('Rounded','BEVEL'); b.width=bevel;b.segments=6;o.modifiers.new('Normals','WEIGHTED_NORMAL');o.parent=parent;return o
def phone(name,color):
 root=bpy.data.objects.new(name,None);bpy.context.collection.objects.link(root)
 metal=mat(name,color,.7);glass=mat(name+' glass',(.012,.018,.035),.5,.12)
 cube('Body',(0,0,0),(1.5,.18,3),metal,.08,root)
 cube('Screen',(0,-.1,0),(1.4,.035,2.9),glass,.017,root)
 cube('Island',(0,.12,1),(1.38,.13,.8),metal,.06,root)
 for x,z in [(-.43,1.2),(.03,1),(-.43,.78)]:
  for rad,y,ma in [(.21,.21,metal),(.17,.25,glass)]:
   bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=rad,depth=.07,location=(x,y,z),rotation=(math.pi/2,0,0));o=bpy.context.object;o.data.materials.append(ma);o.parent=root
 return root
old=phone('Graphite',(.09,.1,.12));new=phone('Orange',(.85,.18,.025))
s=bpy.context.scene
bpy.ops.object.camera_add(location=(0,-10,0));cam=bpy.context.object;aim(cam,(0,0,0));cam.data.type='ORTHO';cam.data.ortho_scale=9;s.camera=cam
for loc,power,size in [((4,-4,5),1100,5),((-4,2,3),1300,4),((0,4,-1),900,3)]:
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.size=size;aim(o,(0,0,0))
def flat(name,c):
 m=bpy.data.materials.new(name);m.use_nodes=True;n=m.node_tree.nodes;n.clear();e=n.new('ShaderNodeEmission');e.inputs[0].default_value=(*c,1);out=n.new('ShaderNodeOutputMaterial');m.node_tree.links.new(e.outputs[0],out.inputs[0]);return m
white=flat('White',(1,1,1));purple=flat('Purple',(.19,.025,.7));black=flat('Black',(.012,.008,.025))
bg=cube('Backdrop',(0,4,0),(12,.1,15),purple,.01)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font=bpy.data.fonts.load(fontpath) if os.path.exists(fontpath) else None
def title(body,z,size,material):
 bpy.ops.object.text_add(location=(0,-2,z),rotation=(math.pi/2,0,0));o=bpy.context.object;o.data.body=body;o.data.align_x='CENTER';o.data.align_y='CENTER';o.data.size=size;o.data.space_line=1.05
 if font:o.data.font=font
 o.data.materials.append(material);return o
texts=[title('Quer trocar\nde celular?',2.6,.57,white),title('Use seu iPhone\nde entrada',2.7,.52,black),title('E pegue um\niPhone 17',2.7,.58,white),title('Melhores preços\naqui na',1.1,.52,white),title('mixphone.rio',-.1,.55,white)]
num=title('17',-.3,2.5,white);num.location.y=1
def smooth(x):x=max(0,min(1,x));return x*x*(3-2*x)
s.render.engine='CYCLES';s.cycles.samples=8;s.render.resolution_x=540;s.render.resolution_y=960;s.render.resolution_percentage=100;s.render.fps=24;s.frame_end=336;s.render.image_settings.file_format='PNG';s.render.filepath=os.path.abspath('frames')+'/'
for f in range(1,337):
 t=(f-1)/24;scene=0 if t<3 else 1 if t<6 else 2 if t<10 else 3
 start=[0,3,6,10][scene];u=t-start;e=smooth(u/.6)
 bg.data.materials[0]=[purple,white,purple,black][scene]
 for i,o in enumerate(texts):
  visible=(i==scene or (scene==3 and i==4))
  o.hide_render=not visible;o.location.x=(1-e)*(-3 if i%2==0 else 3);o.scale=(.85+.15*e,)*3
 num.hide_render=scene!=2
 for j,o in enumerate([old,new]):
  show=(j==0 and scene in (0,1)) or (j==1 and scene==2)
  o.hide_render=not show;o.location=(3*(1-e),0,-.65+.13*math.sin(t*3));o.rotation_euler=(.15*math.sin(t*2),.12*math.cos(t*2),math.pi+u*.8);o.scale=(1.1,)*3
 s.frame_set(f);bpy.ops.render.render(write_still=True) if False else None
 s.render.filepath=os.path.abspath('frames/%04d.png'%f);bpy.ops.render.render(write_still=True)
