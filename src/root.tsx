import React from 'react';
import {Composition} from 'remotion';
import {Video} from './Video';

export const Root: React.FC = () => (
  <Composition id="VideoDirector" component={Video} durationInFrames={180} fps={30} width={1080} height={1920} />
);
