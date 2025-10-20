import json
import os
import random
from events import EVENTS
from page import wrap

def save_state(state, save_file):
    try:
        with open(save_file, 'w') as f:
            json.dump(state, f, indent=2)
        print(f"[saved] game saved to {save_file}")
    except Exception as e:
        print("Save failed:", e)

def load_state(save_file):
    if not os.path.exists(save_file):
        print("No save file found.")
        return None
    try:
        with open(save_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("Failed to load save:", e)
        return None

def play(pages, save_file):
    state = {'page': 0, 'hp': 100, 'max_hp': 100, 'inventory': [], 'moves': 0}
    n = len(pages)
    print("Welcome to MaxPages Adventure! Reach page", n - 1, "to win.")
    while True:
        if state['hp'] <= 0:
            print("\nYou have 0 HP — you collapse. Game over.")
            if input("Load last save? (y/n): ").strip().lower() == 'y':
                loaded = load_state(save_file)
                if loaded:
                    state.update(loaded)
                    print("Loaded. Continuing...")
                    continue
            print("Thanks for playing.")
            break

        cur = pages[state['page']]
        print("\n" + "=" * 70)
        print(f"{cur.title}  (HP: {state['hp']}, Inventory: {state['inventory']})")
        print("-" * 70)
        print(wrap(cur.desc))
        print()

        if cur.idx == n - 1:
            print("You have reached the final page. Congratulations — you win!")
            print(f"Total moves: {state['moves']}")
            if input("Save your final state? (y/n): ").strip().lower() == 'y':
                save_state(state, save_file)
            break

        for i, (label, target, event) in enumerate(cur.choices):
            print(f"{i + 1}. {label} -> Page {target}")
        print("S. Save game    L. Load game    Q. Quit")

        choice = input("Choose an option: ").strip().lower()
        if choice == 'q':
            if input("Quit without saving? (y/n): ").strip().lower() == 'y':
                print("Goodbye.")
                break
            else:
                continue
        if choice == 's':
            save_state(state, save_file)
            continue
        if choice == 'l':
            loaded = load_state(save_file)
            if loaded:
                state.update(loaded)
            continue

        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(cur.choices):
                print("Invalid choice number.")
                continue
        except ValueError:
            print("Enter a number, S, L, or Q.")
            continue

        label, target, event_fn_name = cur.choices[idx]
        event_fn = None
        for fn in EVENTS:
            if fn and fn.__name__ == event_fn_name:
                event_fn = fn
                break
        if event_fn:
            print("\n>> Event:", event_fn(state))

        state['page'] = target
        state['moves'] += 1
        if random.random() < 0.12:
            dmg = random.randint(1, 12)
            state['hp'] -= dmg
            print(f"\nA lurking foe scratches you for {dmg} HP.")
        if state['moves'] % 7 == 0:
            save_state(state, save_file)
