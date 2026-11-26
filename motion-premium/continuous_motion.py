import math
def clamp(t): return max(0,min(1,t))
def smooth(t):
 t=clamp(t);return t*t*(3-2*t)
def impulse(t):
 t=clamp(t);return 1-(1-t)**3
def spring(t):
 t=clamp(t);return 1 if t==1 else max(0,1-math.exp(-7*t)*math.cos(11*t))
