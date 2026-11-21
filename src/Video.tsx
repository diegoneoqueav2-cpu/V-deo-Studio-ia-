import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

export const Video: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const reveal = (start: number) => spring({frame: frame - start, fps, config: {damping: 18, stiffness: 100}});
  const enter = (start: number) => ({
    opacity: interpolate(frame, [start, start + 12], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
    transform: `translateY(${(1 - reveal(start)) * 90}px) scale(${0.92 + reveal(start) * 0.08})`,
  });
  const glow = 0.5 + Math.sin(frame / 14) * 0.12;
  return (
    <AbsoluteFill style={{background: '#071b16', color: '#fff', fontFamily: 'Arial, sans-serif', overflow: 'hidden'}}>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 38%, #155b45 0%, #071b16 58%)'}} />
      <div style={{position: 'absolute', top: 360, left: 130, width: 820, height: 820, borderRadius: '50%', border: '3px solid #35d79c', opacity: glow, transform: `scale(${1 + frame / 2500})`}} />
      <div style={{position: 'absolute', top: 435, left: 205, width: 670, height: 670, borderRadius: '50%', border: '1px solid #a8f5d2', opacity: 0.35}} />
      <div style={{position: 'absolute', top: 680, width: '100%', textAlign: 'center', fontSize: 46, fontWeight: 700, letterSpacing: 12, color: '#9cf0c6', ...enter(8)}}>VIDEO DIRECTOR</div>
      <div style={{position: 'absolute', top: 795, width: '100%', textAlign: 'center', fontSize: 106, fontWeight: 900, letterSpacing: -3, ...enter(28)}}>SUA IDEIA</div>
      <div style={{position: 'absolute', top: 915, width: '100%', textAlign: 'center', fontSize: 104, fontWeight: 900, color: '#45e7a5', ...enter(45)}}>EM MOVIMENTO</div>
      <div style={{position: 'absolute', top: 1150, width: '100%', textAlign: 'center', fontSize: 42, letterSpacing: 3, ...enter(80)}}>MOTION GRAPHICS • REMOTION</div>
      <div style={{position: 'absolute', top: 1650, width: '100%', textAlign: 'center', fontSize: 40, color: '#9cf0c6', ...enter(120)}}>CRIADO NA NUVEM</div>
    </AbsoluteFill>
  );
};
