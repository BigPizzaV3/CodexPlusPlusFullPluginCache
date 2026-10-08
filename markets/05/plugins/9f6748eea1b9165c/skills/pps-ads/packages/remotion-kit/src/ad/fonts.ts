import { loadFont as loadInter } from '@remotion/google-fonts/Inter'
import { loadFont as loadBricolage } from '@remotion/google-fonts/BricolageGrotesque'

export const inter = loadInter('normal', { weights: ['400', '600', '700'], subsets: ['latin'] })
export const bricolage = loadBricolage('normal', { weights: ['800'], subsets: ['latin'] })
