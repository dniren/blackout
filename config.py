from pynput import keyboard
import main

# .txt file where you want to pull challenges from. Must be in the Blackout Lists folder
challenges_master_list = 'skyrim.txt'

# if True, resets the counter and active challenges list
# if False, counter and active challenges do not change
new_challenge = False
tasks_message = 'Tasks completed: '

start_new_challenge_key = '0'

complete_challenge_keys = {
    'y': 1,
    'u': 2,
    'i': 3
}


if __name__ == '__main__':
    with keyboard.Listener(on_press=main.on_press) as listener:
        listener.join()
