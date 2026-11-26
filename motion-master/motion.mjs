export const clamp=(x)=>Math.max(0,Math.min(1,x));
export const mix=(a,b,t)=>a+(b-a)*t;
export const smooth=t=>{t=clamp(t);return t*t*(3-2*t)};
export const smoother=t=>{t=clamp(t);return t*t*t*(t*(6*t-15)+10)};
export function bezier(t,x1=.22,y1=1,x2=.36,y2=1){t=clamp(t);const c=(u,a,b)=>3*(1-u)**2*u*a+3*(1-u)*u*u*b+u**3;let lo=0,hi=1;for(let i=0;i<24;i++){let m=(lo+hi)/2;if(c(m,x1,x2)<t)lo=m;else hi=m;}return c((lo+hi)/2,y1,y2)}
export function spring(t,damping=7,frequency=12){if(t<=0)return 0;return 1-Math.exp(-damping*t)*(Math.cos(frequency*t)+damping/frequency*Math.sin(frequency*t))}
export function trajectory(t,a,b,c,d){t=clamp(t);return a.map((v,i)=>(1-t)**3*v+3*(1-t)**2*t*b[i]+3*(1-t)*t*t*c[i]+t**3*d[i])}
export function project([x,y,z],focal=900){const k=focal/Math.max(1,focal+z);return {x:x*k,y:y*k,scale:k}}
export function morph(a,b,t){if(a.length!==b.length)throw Error('Morph requires matching topology');return a.map((p,i)=>p.map((v,j)=>mix(v,b[i][j],smooth(t))))}
export function shutterSamples(frame,count=8,shutter=.5){return Array.from({length:count},(_,i)=>frame+((i+.5)/count-.5)*shutter)}
export function stagger(frame,start,duration,index,delay=4){return clamp((frame-start-index*delay)/duration)}
