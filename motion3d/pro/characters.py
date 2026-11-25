import bpy
from studio import import_product
def load_character(path):
 before=set(bpy.data.objects)
 import_product(path)
 objects=[o for o in bpy.data.objects if o not in before]
 rigs=[o for o in objects if o.type=='ARMATURE']
 if not rigs:raise ValueError('Character requires a rigged GLB/GLTF')
 return rigs[0],objects
def facial_key(mesh,name,value,frame):
 keys=mesh.data.shape_keys
 if not keys or name not in keys.key_blocks:raise ValueError('Missing facial shape: '+name)
 k=keys.key_blocks[name];k.value=max(0,min(1,value));k.keyframe_insert(data_path='value',frame=frame)
def apply_action(rig,action_name):
 action=bpy.data.actions.get(action_name)
 if not action:raise ValueError('Missing action')
 rig.animation_data_create();rig.animation_data.action=action
