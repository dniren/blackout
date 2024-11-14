from random import choice
import config


def on_press(key):
    try: key_char = key.char
    except AttributeError: return
    if key_char == config.start_new_challenge_key:
        create_starting_challenges(len(config.complete_challenge_keys.keys()), config.challenges_master_list,
                                   config.tasks_message)
    if key_char in config.complete_challenge_keys.keys():
        challenge_completed(config.complete_challenge_keys[key_char])


def create_starting_challenges(challenge_number: int, master_list: str,
                               tasks_message: str):
    with open(f'Blackout Lists/{master_list}') as f:
        challenges: list = f.readlines()
    selections = ''
    for lead_number in range(1, challenge_number + 1):
        selection = choice(challenges)
        selections += f'{lead_number}. {selection}'
        challenges.remove(selection)

    # copy first challenges to new file
    with open('Appendix/active_challenges.txt', 'w') as f:
        f.writelines(selections)

    # copy unassigned challenges to separate file
    with open('Appendix/all_session_challenges.txt', 'w') as f:
        f.writelines(challenges)
    with open('Appendix/counter.txt', 'w') as f:
        f.write(f'{tasks_message}0')


def challenge_completed(challenge_number: int):
    # get list of remaining challenges, get new one and remove from list
    with open('Appendix/all_session_challenges.txt') as f:
        challenges: list = f.readlines()
    try:
        new_challenge = choice(challenges)
        challenges.remove(new_challenge)
        with open('Appendix/all_session_challenges.txt', 'w') as f:
            f.writelines(challenges)
        out_of_challenges = False
    except (IndexError, ValueError):
        new_challenge = 'Out of challenges!\n'
        out_of_challenges = True

    # sub out completed challenge for new one
    with open('Appendix/active_challenges.txt') as f:
        old_challenges: list = f.readlines()
    old_challenges[challenge_number - 1] = f'{challenge_number}. {new_challenge}'
    with open('Appendix/active_challenges.txt', 'w') as f:
        f.writelines(old_challenges)
    if not out_of_challenges:
        counter_increase()


def counter_increase():
    with open('Appendix/counter.txt') as f:
        info: list[str] = f.read().split(' ')
    text: str = ' '.join(info[:-1])
    count: int = int(info[-1])
    count += 1
    with open('Appendix/counter.txt', 'w') as f:
        f.write(f'{text} {count}')
