import random

def simple_event_heal(state):
    amount = random.randint(5, 15)
    state['hp'] = min(state['max_hp'], state['hp'] + amount)
    return f"You find a small health herb and recover {amount} HP."

def simple_event_trap(state):
    dmg = random.randint(5, 20)
    state['hp'] -= dmg
    return f"A hidden trap injures you for {dmg} HP."

def simple_event_item(state):
    items = ['rusty key', 'glowing gem', 'map fragment', 'mysterious coin']
    item = random.choice(items)
    state['inventory'].append(item)
    return f"You acquire: {item}."

EVENTS = [simple_event_heal, simple_event_trap, simple_event_item, None, None]
