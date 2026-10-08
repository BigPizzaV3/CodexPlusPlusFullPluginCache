import React from 'react'
import { Live } from './Live'
import type { BeatProps } from '../types'

/** The hook: footage, no text. */
export const Open: React.FC<BeatProps> = (props) => <Live {...props} beat={{ ...props.beat, subtitle: undefined }} />
