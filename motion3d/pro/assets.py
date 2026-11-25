"""Download only explicitly selected CC0 assets; retain provenance."""
import json, pathlib, urllib.request
def fetch(url, path):
 path=pathlib.Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 if not path.exists():
  req=urllib.request.Request(url,headers={'User-Agent':'MotionStudio/1.0'})
  with urllib.request.urlopen(req,timeout=90) as response, path.open('wb') as out:
   import shutil
   shutil.copyfileobj(response,out)
 return path
def poly_hdri(asset='studio_small_03',resolution='1k'):
 req=urllib.request.Request('https://api.polyhaven.com/files/'+asset,headers={'User-Agent':'MotionStudio/1.0'})
 with urllib.request.urlopen(req,timeout=60) as response: data=json.load(response)
 item=data['hdri'][resolution]['hdr']
 p=fetch(item['url'],'cache/'+asset+'.hdr')
 return p
def ambient_material(asset='Metal032',resolution='1K'):
 return fetch('https://ambientcg.com/get?file='+asset+'_'+resolution+'-JPG.zip','cache/'+asset+'.zip')
