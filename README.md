## 🧭 Advanced MaxPages Adventure

Welcome to **Advanced MaxPages Adventure** — a modular, text-based exploration and combat game written in Python.  
You explore mysterious “pages,” fight enemies, find treasures, and level up to reach the final page.

---

## 🚀 Features

- 🗺️ **Procedurally Generated Pages**
  - Each playthrough is unique with different paths and room types (treasure, trap, merchant, boss).

- ⚔️ **Turn-Based Combat**
  - Fight enemies like goblins, wolves, and bandits.
  - Attack, flee, or use items like potions or bombs.

- 🎒 **Inventory System**
  - Collect and use healing potions, bombs, and torches.
  - Manage items directly in battle or while exploring.

- 🧙 **Leveling & Stats**
  - Gain XP from combat and level up to increase HP, Attack, and Defense.

- 💾 **Save/Load + Autosave**
  - Progress is automatically saved every few moves.
  - Manual saving and loading supported.

- 🌈 **Colored Text (Optional)**
  - Install `colorama` for colored terminal output.

---

## 🧩 Folder Structure
advanced_maxpages_modular/

│

├── main.py # Entry point

├── game_engine.py # Core gameplay loop + save/load + UI

├── page.py # Page generation and types

├── events.py # Random events and enemy creation

├── combat.py # Turn-based battle system

├── player.py # Player stats and leveling logic

├── items.py # Item definitions and item effects

├── config.py # Constants and global settings

└── README.md # This file

---

## 🎮 How to Play

1. Run the game

python3 main.py --pages 40


2. Game Commands

- Type numbers (1, 2, 3…) to choose paths.

- I → Open inventory

- S → Save game

- L → Load saved game

- M → View visited pages

- Q → Quit game

3. Goal

Survive traps, defeat enemies, and reach the final page!

---

## 🧠 Tips

Use healing items wisely — HP doesn’t regenerate automatically.

Leveling up fully restores your HP.

Merchant pages sometimes give free items.

Save frequently to protect progress.

---


---

## ⚙️ Requirements

- **Python 3.8+**
- Optional:
  ```bash
  pip install colorama
