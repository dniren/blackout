Code for randomizing challenges from a master list - pairs well with Twitch

1. Run install.py.

2. .txt files with challenges go in the "Blackout Lists" folder. One set of challenges should be in its own .txt file, one per line. These files will be copied from but never edited, so they're reusable.

3. Go to configure.py. Define the "challenges_master_list" variable with the name of the .txt file in the "Blackout Lists" folder you want to use. Again, this list will not be edited when you run the code.

4. The "tasks_message" variable will appear immediately before the "challenge completed" tally and be stored in "Appendix/Counter.txt," so I recommend putting a space inside the parentheses after the text.

5. Define the "start_new_challenge_key" variable with the key you want to use to reset or start the challenge. If the code crashes or you stop it and want to continue your current challenge, do NOT hit this key.

6. Define the "complete_challenge_keys" with the preferred keys, then include the number afterward: "y: 1". The active challenges will be stored in "Appendix/active_challenges.txt". If you define three challenge hotkeys, you'll be shown three challenges at a time. One hotkey, one challenge, et cetera.

7. When you run the code and hit the "start_new_challenge_key" hotkey, the first challenges will go to "Appendix/active_challenges.txt" and the rest will be copied to "Appendix/all_session_challenges.txt." Each time you hit a challenge hotkey, that challenge will be replaced with a new one until they run out, when they'll be replaced with your "out_of_challenges_message."

8. Each time you hit the "start_new_challenge_key," "active_challenges.txt" and "all_session_challenges.txt" will completely refresh. Again, don't hit the key if you're midway through a set of challenges and are just continuing.

9. On OBS, go to Sources, +, Text, "text input mode from file," and select "Appendix/active_challenges.txt." Do the same with "Appendix/all_session_challenges.txt." These will update on your stream in real time as you start the session and complete challenges.

10. Have fun!
