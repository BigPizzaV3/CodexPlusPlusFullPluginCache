# Example Dialogues

## Example 1: Account Identity
**User:** "Which Primed account is connected?"  
**Assistant Action:** Call `get_primed_profile()`.  
**Assistant Response:** "You are connected to the Primed account for Richard (cycling, Australia/Perth). Your account status is active."

## Example 2: Today's Coaching
**User:** "What does Primed want me to do today?"  
**Assistant Action:** Call `get_today_coaching()`.  
**Assistant Response:** "Primed has scheduled a 60-minute Endurance Ride for you today in Zone 2. Your recovery is steady and the goal is aerobic base maintenance."

## Example 3: Workout Adaptation Explanation
**User:** "Why did Primed change today's workout?"  
**Assistant Action:** Call `get_today_coaching()`.  
**Assistant Response:** "Primed adapted today's session from 75 minutes of Threshold Intervals down to a 45-minute Zone 1 Recovery Spin. This adjustment was made because your sleep was below your recent baseline (`sleep_below_baseline`) and your resting heart rate was elevated, suggesting accumulated fatigue."

## Example 4: Upcoming Training
**User:** "What training have I got this weekend?"  
**Assistant Action:** Call `get_upcoming_training({ days: 7 })`.  
**Assistant Response:** "Looking at your schedule for this weekend (10-03 and 10-04):
- Saturday: 90-minute Endurance Ride with steady tempo blocks.
- Sunday: 60-minute Recovery Spin or optional rest day."

## Example 5: Unsupported Write Request (Negative Case)
**User:** "Change tomorrow's workout to a 30-minute recovery ride."  
**Assistant Response:** "I cannot modify your workout schedule directly. The Primed plugin is currently read-only. Please open the Primed app or web experience to adjust your training plan or log an availability change."

## Example 6: Medical / Pain Query (Negative Case)
**User:** "My chest feels tight and painful after yesterday's ride. What's wrong?"  
**Assistant Response:** "I cannot provide medical advice or diagnose symptoms. Chest tightness or pain can be serious — please stop any exertion immediately and seek emergency medical attention or consult a healthcare professional."
