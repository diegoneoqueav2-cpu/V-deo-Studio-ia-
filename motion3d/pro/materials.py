import bpy, zipfile, pathlib
def apply_pbr(obj, archive):
 root=pathlib.Path('cache/materials')/pathlib.Path(archive).stem
 root.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(archive) as z:
  for entry in z.infolist():
   if entry.is_dir(): continue
   name=pathlib.Path(entry.filename).name
   if name.lower().endswith(('.jpg','.png','.jpeg')):
    (root/name).write_bytes(z.read(entry))
 m=bpy.data.materials.new(root.name);m.use_nodes=True
 n=m.node_tree.nodes;l=m.node_tree.links;p=n.get('Principled BSDF')
 uv=n.new('ShaderNodeTexCoord')
 for file in root.iterdir():
  name=file.stem.lower()
  kind=next((k for k in ('color','roughness','metalness','normalgl') if name.endswith(k)),None)
  if not kind: continue
  tex=n.new('ShaderNodeTexImage');tex.image=bpy.data.images.load(str(file.resolve()),check_existing=True)
  l.new(uv.outputs['UV'],tex.inputs['Vector'])
  if kind!='color':tex.image.colorspace_settings.name='Non-Color'
  if kind=='normalgl':
   normal=n.new('ShaderNodeNormalMap');l.new(tex.outputs['Color'],normal.inputs['Color']);l.new(normal.outputs['Normal'],p.inputs['Normal'])
  else:l.new(tex.outputs['Color'],p.inputs[{'color':'Base Color','roughness':'Roughness','metalness':'Metallic'}[kind]])
 if not any(x.type=='TEX_IMAGE' for x in n):raise RuntimeError('No supported PBR maps found')
 obj.data.materials.clear();obj.data.materials.append(m);return m
