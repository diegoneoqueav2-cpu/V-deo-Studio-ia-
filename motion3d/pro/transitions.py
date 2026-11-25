import math
def clamp(t):return max(0,min(1,t))
def smooth(t):
 t=clamp(t);return t*t*(3-2*t)
def out_cubic(t):return 1-(1-clamp(t))**3
def pose(obj,t,mode='reveal',origin=(0,0,0),scale=1):
 t=clamp(t);e=out_cubic(t);x,y,z=origin
 obj.location=(x,y,z);obj.scale=(scale,)*3;obj.rotation_euler=(0,0,0)
 if mode=='reveal':obj.location.x=x+4*(1-e);obj.rotation_euler.z=.7*(1-e)
 elif mode=='rise':obj.location.z=z-3*(1-e)
 elif mode=='zoom':obj.scale=(scale*(.15+.85*e),)*3
 elif mode=='spin':obj.rotation_euler.z=2*math.pi*smooth(t)
 elif mode=='float':obj.location.z=z+.15*math.sin(t*2*math.pi)
 elif mode=='exit':obj.location.x=x-5*smooth(t)
 elif mode=='flip':obj.rotation_euler.z=math.pi*(1-e)
 elif mode=='slam':obj.scale=(scale*(1+.4*(1-e)),)*3
 else:raise ValueError(mode)
def visibility(root,visible):
 root.hide_render=not visible
 for child in root.children_recursive:child.hide_render=not visible
