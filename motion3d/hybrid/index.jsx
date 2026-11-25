import React from 'react';
import {registerRoot,Composition,AbsoluteFill,Img,staticFile,useCurrentFrame,interpolate,Easing} from 'remotion';
import {gsap} from 'gsap';
const ease=gsap.parseEase('power3.out');
function Hybrid(){
 const f=useCurrentFrame();const t=Math.min(1,Math.max(0,(f-12)/24));const p=ease(t);
 const fade=interpolate(f,[0,12,135,149],[0,1,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 return <AbsoluteFill style={{backgroundColor:'#130d20',color:'white',fontFamily:'Arial,sans-serif',opacity:fade}}>
 <AbsoluteFill style={{overflow:'hidden'}}><Img src={staticFile('studio-preview.png')} style={{width:'100%',height:'100%',objectFit:'cover',transform:'scale('+ (1+f/1800)+')'}}/></AbsoluteFill>
 <AbsoluteFill style={{background:'linear-gradient(180deg,rgba(15,5,30,.8),transparent 40%,transparent 60%,rgba(15,5,30,.9))'}}/>
 <div style={{position:'absolute',top:180,left:80,right:80,fontSize:88,fontWeight:900,letterSpacing:-3,opacity:p,transform:'translateY('+((1-p)*90)+'px)'}}>MOTION<br/><span style={{color:'#c7a0ff'}}>PRO STUDIO</span></div>
 <div style={{position:'absolute',bottom:180,left:80,right:80,fontSize:40,opacity:interpolate(f,[45,70],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp',easing:Easing.out(Easing.cubic)})}}>BLENDER × REMOTION</div>
 </AbsoluteFill>
}
registerRoot(()=> <Composition id="Hybrid" component={Hybrid} durationInFrames={150} fps={30} width={1080} height={1920}/>);