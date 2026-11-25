import json,sys
from faster_whisper import WhisperModel
def transcribe(path,output):
 model=WhisperModel('small',device='cpu',compute_type='int8')
 segments,info=model.transcribe(path,word_timestamps=True)
 words=[{'text':w.word.strip(),'start':w.start,'end':w.end} for s in segments for w in (s.words or [])]
 with open(output,'w',encoding='utf8') as f:json.dump({'language':info.language,'words':words},f,ensure_ascii=False,indent=2)
if __name__=='__main__':transcribe(sys.argv[1],sys.argv[2])
