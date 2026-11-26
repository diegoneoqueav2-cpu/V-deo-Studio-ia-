import bpy, math
from mathutils import Vector
b=bpy
b.ops.object.select_all(action='SELECT'); b.ops.object.delete(use_global=False)
s=b.context.scene
s.render.engine='BLENDER_EEVEE_NEXT' if b.app.version >= (4,2,0) else 'BLENDER_EEVEE'
s.render.resolution_x=1080;s.render.resolution_y=1920;s.render.resolution_percentage=100;s.render.fps=60;s.frame_end=1200
def mat(n,c):
 m=b.data.materials.new(n);m.diffuse_color=(*c,1);return m
green=mat('Emerald',(.025,.48,.19));white=mat('White',(.95,1,.96));dark=mat('Deep green',(.012,.22,.07))
def assign(o,m):o.data.materials.append(m);return o
def ball(loc,r,m):
 b.ops.mesh.primitive_uv_sphere_add(segments=48,ring_count=24,radius=r,location=loc);o=assign(b.context.object,m)
 for p in o.data.polygons:p.use_smooth=True
 return o
def cube(loc,scale,m):
 b.ops.mesh.primitive_cube_add(size=1,location=loc);o=assign(b.context.object,m);o.scale=scale;b.ops.object.transform_apply(location=False,rotation=False,scale=True);v=o.modifiers.new('Rounded','BEVEL');v.width=.12;v.segments=5;o.modifiers.new('Normals','WEIGHTED_NORMAL');return o
def txt(t,y,size,m):
 b.ops.object.text_add(location=(0,y,0));o=b.context.object;o.data.body=t;o.data.align_x='CENTER';o.data.align_y='CENTER';o.data.size=size;o.data.extrude=.065;o.data.bevel_depth=.018;return assign(o,m)
def key(o,f,loc,scale=(1,1,1),rot=(0,0,0)):
 o.location=loc;o.scale=scale;o.rotation_euler=rot
 for p in ['location','scale','rotation_euler']:o.keyframe_insert(data_path=p,frame=f)
def appear(o,a,z):
 p=tuple(o.location);q=tuple(o.scale)
 key(o,1,(p[0],p[1],-20),(.001,)*3);key(o,a,(p[0]-2,p[1]-.4,-4),(.05,)*3,(0,.8,-.3));key(o,a+19,p,tuple(v*1.08 for v in q));key(o,a+31,p,q);key(o,z-12,p,q);key(o,z,(p[0]+3,p[1],-5),(.001,)*3)
b.ops.object.camera_add(location=(0,0,12));cam=b.context.object;s.camera=cam;cam.data.lens=38
for loc,power,size in [((-4,5,7),1400,5),((4,1,5),900,4),((0,-5,4),500,3)]:
 b.ops.object.light_add(type='AREA',location=loc);o=b.context.object;o.data.energy=power;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(-o.location).to_track_quat('-Z','Y').to_euler()
s.world.color=(.25,.25,.25)
bg=cube((0,0,-1.5),(40,40,.2),green)
for a,z,lines,m in [(25,240,[('BLACK FRIDAY',1.2,.65),('CHEGOU NO CEM',.15,.48)],white),(245,480,[('MEGA',1.7,1.25),('DESCONTO',.45,.75),('PARA NOVOS ALUNOS',-.5,.34)],white),(485,840,[('PRIMEIRO ANO',1.5,.58),('DO ENSINO FUNDAMENTAL',.65,.29),('1',-1.25,2.2)],white),(845,1080,[('ATÉ O FINAL',1.6,.65),('DE NOVEMBRO',.65,.55),('30',-1.3,1.7)],white),(1085,1200,[('CEM BILÍNGUE',.6,.6),('GARANTA SUA VAGA!',-.5,.43)],white)]:
 for i,(t,y,size) in enumerate(lines):appear(txt(t,y,size,m),a+i*9,z)
orb=ball((0,0,0),.65,white)
for a in [1,225,465,825,1065]:
 key(orb,a,(-4,-2,-4),(.35,)*3);key(orb,a+13,(0,0,2),(1.2,)*3);key(orb,a+22,(1.8,-2,0),(.8,)*3);key(orb,a+35,(5,-3,-4),(.01,)*3)
appear(txt('%',-1.8,1.5,white),265,480)
appear(cube((-1.8,-1.7,0),(1.1,1.5,.65),dark),500,840)
for i in range(3):appear(cube((1.7,-1.6+i*.25,0),(1.2,.22,.8),white),520+i*12,840)
appear(cube((0,-1.3,-.35),(2.5,2.3,.3),dark),855,1080)
s.render.image_settings.file_format='FFMPEG';s.render.ffmpeg.format='MPEG4';s.render.ffmpeg.codec='H264';s.render.filepath='//CEM_V5.mp4'
b.ops.wm.save_as_mainfile(filepath='/tmp/CEM_V5.blend')
b.ops.render.render(animation=True)
