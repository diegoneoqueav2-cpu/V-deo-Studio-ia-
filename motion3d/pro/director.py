"""Deterministic scene planner; not a generative AI."""
import json,sys
def plan(script,fps=30):
 scenes=[];frame=0
 for i,line in enumerate(script.splitlines()):
  line=line.strip()
  if not line:continue
  duration=max(2.5,len(line.split())/2.5+.5)
  length=round(duration*fps)
  scenes.append({'id':len(scenes)+1,'text':line,'start':frame,'frames':length,'camera':['hero','push','orbit_left','slide_right'][len(scenes)%4],'transition':['reveal','rise','zoom'][len(scenes)%3],'asset':None})
  frame+=length
 if not scenes:raise ValueError('Empty script')
 return {'fps':fps,'width':1080,'height':1920,'duration_frames':frame,'scenes':scenes}
if __name__=='__main__':
 with open(sys.argv[1],encoding='utf8') as f:result=plan(f.read())
 with open(sys.argv[2],'w',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
