import json,sys
import librosa
import numpy as np
def analyze(path):
 y,sr=librosa.load(path,mono=True)
 onset=librosa.onset.onset_detect(y=y,sr=sr,units='time')
 tempo,beats=librosa.beat.beat_track(y=y,sr=sr)
 return {'duration':len(y)/sr,'tempo':float(np.asarray(tempo).reshape(-1)[0]),'beats':librosa.frames_to_time(beats,sr=sr).tolist(),'onsets':onset.tolist()}
if __name__=='__main__':
 with open(sys.argv[2],'w') as f:json.dump(analyze(sys.argv[1]),f,indent=2)
