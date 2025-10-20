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
