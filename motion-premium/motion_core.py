"""Reusable motion primitives; independent of rendering backend."""
import math
def clamp(t): return max(0.,min(1.,t))
def bezier(t,x1=.22,y1=1.,x2=.36,y2=1.):
    t=clamp(t)
    def b(u,a,c): return 3*(1-u)**2*u*a+3*(1-u)*u*u*c+u**3
    lo,hi=0.,1.
    for _ in range(24):
        u=(lo+hi)/2
        if b(u,x1,x2)<t: lo=u
        else: hi=u
    return b((lo+hi)/2,y1,y2)
def spring(t,damping=7.,frequency=11.):
    t=clamp(t)
    if t==1: return 1.
    return 1-math.exp(-damping*t)*math.cos(frequency*t)
def progress(time,start,duration):
    return clamp((time-start)/max(duration,1e-6))
def tween(a,b,time,start,duration,curve=bezier):
    p=curve(progress(time,start,duration))
    return a+(b-a)*p
def velocity(sample,t,dt=1/120):
    return (sample(t+dt)-sample(t-dt))/(2*dt)
def blur_length(sample,t,fps=30,shutter=.5):
    return abs(velocity(sample,t))*shutter/fps
def click_reaction(t,click):
    age=t-click
    if age<0: return dict(scale=1.,glow=0.,ripple=0.,opacity=0.)
    p=progress(age,0,.55)
    return dict(scale=1-.09*math.exp(-10*age)*math.sin(min(age/.12,1)*math.pi/2),glow=math.exp(-7*age),ripple=bezier(p),opacity=1-p)
def stagger(index,start,interval=.035):
    return start+index*interval
def perspective_scale(depth,focal=8.):
    return focal/max(.1,focal+depth)
def morph_points(a,b,t):
    if len(a)!=len(b): raise ValueError("Morph requires matching topology")
    p=bezier(t)
    return [tuple(x+(y-x)*p for x,y in zip(u,v)) for u,v in zip(a,b)]
