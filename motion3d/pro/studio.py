import bpy, math
from mathutils import Vector
LIGHTS={
'premium':[((4,-4,5),1100,5,(1,.9,.8)),((-4,1,3),900,4,(.7,.8,1)),((0,4,2),1300,3,(1,1,1))],
'soft':[((3,-4,4),700,6,(1,1,1)),((-3,-2,2),500,5,(1,1,1))],
'neon':[((4,-2,3),1000,3,(.5,.2,1)),((-4,2,3),1100,3,(.2,.5,1))],
'warm':[((3,-4,5),1100,4,(1,.65,.35)),((-3,2,3),700,5,(1,.9,.7))],
'contrast':[((3,-4,5),1400,2,(1,1,1)),((-3,3,2),900,2,(1,1,1))]
}
def aim(o,p=(0,0,0)): o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
def lighting(name='premium',hdri=None):
 for loc,power,size,color in LIGHTS[name]:
  bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.size=size;o.data.color=color;aim(o)
 if hdri:
  w=bpy.context.scene.world;w.use_nodes=True;n=w.node_tree.nodes;env=n.new('ShaderNodeTexEnvironment');env.image=bpy.data.images.load(str(hdri));w.node_tree.links.new(env.outputs['Color'],n.get('Background').inputs['Color']);n.get('Background').inputs['Strength'].default_value=.45
def ease(t):
 t=max(0,min(1,t));return t*t*(3-2*t)
def camera_motion(camera,name,t,target=(0,0,0)):
 e=ease(t);a=(e-.5)*1.2
 presets={'orbit_left':(7*math.sin(a),-7*math.cos(a),2),'orbit_right':(-7*math.sin(a),-7*math.cos(a),2),'push':(0,-9+3*e,1),'pull':(0,-6-3*e,1),'rise':(0,-8,1+3*e),'fall':(0,-8,4-3*e),'slide_left':(2-4*e,-8,1),'slide_right':(-2+4*e,-8,1),'crane':(2*e,-8,1+3*e),'reveal':(4*(1-e),-8,2),'macro':(0,-5+e,1),'wide':(0,-7-3*e,2),'arc_high':(6*math.sin(a),-6*math.cos(a),4),'arc_low':(6*math.sin(a),-6*math.cos(a),.3),'diagonal':(3-6*e,-8,3-2*e),'float':(.4*math.sin(t*6.28),-8,1+.3*math.sin(t*6.28)),'top':(0,-.1-7*(1-e),7*e+1),'hero':(2*(1-e),-8,2-e),'sweep':(4-8*e,-9,2),'static':(0,-8,1)}
 camera.location=Vector(target)+Vector(presets[name]);aim(camera,target)
def quality(preview=True):
 s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=24 if preview else 64;s.cycles.use_denoising=True;s.render.resolution_x=540 if preview else 1080;s.render.resolution_y=960 if preview else 1920;s.render.resolution_percentage=100;s.render.fps=24 if preview else 30
def import_product(path):
 if str(path).lower().endswith(('.glb','.gltf')): bpy.ops.import_scene.gltf(filepath=str(path))
 elif str(path).lower().endswith('.obj'): bpy.ops.wm.obj_import(filepath=str(path))
 else: raise ValueError('Use licensed GLB or OBJ')
 return list(bpy.context.selected_objects)
def text_motion(obj,t,mode='slide'):
 e=ease(t)
 if mode=='slide': obj.location.x=-3*(1-e)
 elif mode=='pop': obj.scale=(.5+.5*e,)*3
 elif mode=='rise': obj.location.z-=.8*(1-e)
