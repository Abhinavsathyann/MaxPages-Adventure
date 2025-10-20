import random
from textwrap import fill
from events import EVENTS

def wrap(s):
    return fill(s, width=70)

class Page:
    def __init__(self, idx, title, desc):
        self.idx = idx
        self.title = title
        self.desc = desc
        self.choices = []

    def add_choice(self, label, target, event=None):
        self.choices.append((label, target, event))

def generate_pages(n):
    pages = []
    for i in range(n):
        title = f"Page {i}"
        desc = f"This is page {i}. You see strange markings and pathways leading onward."
        page = Page(i, title, desc)

        choices = set()
        if i < n - 1:
            choices.add(i + 1)
        jump = min(n - 1, i + random.randint(2, max(2, n // 10)))
        choices.add(jump)
        if i > 0 and random.random() < 0.25:
            choices.add(random.randint(0, i - 1))
        if random.random() < 0.15:
            choices.add(random.randint(0, n - 1))

        labels = [
            "Take the left path",
            "Go through the archway",
            "Climb the stairs",
            "Squeeze through the gap",
            "Follow the light"
        ]
        choices = list(choices)[:3]
        for idx_choice, target in enumerate(choices):
            label = labels[idx_choice % len(labels)]
            event = random.choice(EVENTS)
            page.add_choice(label, target, event)
        pages.append(page)
    return pages
