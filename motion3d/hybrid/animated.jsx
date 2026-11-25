import React from 'react';
import {registerRoot,Composition,AbsoluteFill,Img,Audio,staticFile,useCurrentFrame,interpolate} from 'remotion';
import {gsap} from 'gsap';
import timing from './timing.json';
const ease=gsap.parseEase('power3.out');
function Film(){const f=useCurrentFrame(),t=f/30,p=ease(Math.min(1,f/22)),beat=Math.max(0,...timing.onsets.filter(x=>x<=t)),pulse=Math.exp(-12*(t-beat));
return <AbsoluteFill style={{background:'#100a20',color:'white',fontFamily:'Arial'}}>
<Img src={staticFile('frames/'+String(f+1).padStart(4,'0')+'.png')} style={{width:'100%',height:'100%',objectFit:'cover'}}/>
<Audio src={staticFile('sound.wav')}/>
<AbsoluteFill style={{background:'linear-gradient(180deg,#100a20cc,transparent 40%,transparent 65%,#100a20cc)'}}/>
<div style={{position:'absolute',top:160,left:80,right:80,fontSize:94,fontWeight:900,opacity:p,transform:'translateY('+((1-p)*70)+'px) scale('+(1+.025*pulse)+')'}}>MOTION<br/><span style={{color:'#c8a4ff'}}>PRO STUDIO</span></div>
<div style={{position:'absolute',bottom:160,left:80,fontSize:42,opacity:interpolate(f,[25,45],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}>3D • MOTION • SOUND</div></AbsoluteFill>}
registerRoot(()=> <Composition id="Animated" component={Film} durationInFrames={90} fps={30} width={1080} height={1920}/>);