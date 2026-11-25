import bpy, math, random
def cinematic(camera,target=None):
 s=bpy.context.scene
 s.render.use_motion_blur=True
 s.render.motion_blur_shutter=.35
 camera.data.dof.use_dof=True
 camera.data.dof.aperture_fstop=5.6
 if target: camera.data.dof.focus_object=target
 else: camera.data.dof.focus_distance=8
 s.cycles.use_denoising=True
 s.view_settings.view_transform='AgX'
def particles(count=40,seed=42):
 rng=random.Random(seed)
 for i in range(count):
  bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=rng.uniform(.015,.045),location=(rng.uniform(-3,3),rng.uniform(-1,3),rng.uniform(-4,4)))
  o=bpy.context.object
  o.keyframe_insert(data_path='location',frame=1)
  o.location.z+=rng.uniform(.3,1.5)
  o.keyframe_insert(data_path='location',frame=90)
def animate_product(obj,frames=90):
 base=obj.rotation_euler.copy()
 for f in range(1,frames+1):
  t=(f-1)/(frames-1);e=t*t*(3-2*t)
  obj.rotation_euler=base;obj.rotation_euler.z+=math.tau*e
  obj.keyframe_insert(data_path='rotation_euler',frame=f)
