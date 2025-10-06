# 🐍 Python Snake Game

Welcome to the **Classic Snake Game** built entirely in **Python** using the `turtle` graphics module.  
This project recreates the nostalgic retro game experience — simple, fast, and addictive.  
The goal? Eat as many red apples as possible 🍎 without crashing into the walls or your own tail!

---

## 🚀 Features

✅ Smooth and responsive movement (W, A, S, D controls)  
✅ Real-time score tracking and high-score memory  
✅ Dynamic speed increase with every food eaten  
✅ Clean and minimal retro design  
✅ Fully built using Python’s built-in libraries (no extra dependencies)

---

## 🎮 How to Play

1. **Run the game** using your Python interpreter.
2. Use the following keys to move your snake:
   - **W** → Move Up  
   - **S** → Move Down  
   - **A** → Move Left  
   - **D** → Move Right
3. Eat the red food to grow your snake and increase your score.
4. Don’t crash into the walls or your own tail — or the game will reset!
5. Try to beat your **High Score** each time. 🏆

---

## 🧠 Game Logic Overview

- The game continuously runs inside a **main loop** that updates the screen using `win.update()`.
- Every time the snake eats food, a new body segment is added.
- The `delay` variable decreases slightly to increase game speed gradually.
- Collision with the border or the snake’s own body resets the game.

---

## 🖥️ Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.x |
| **Graphics** | Turtle Graphics |
| **Modules Used** | `turtle`, `time`, `random` |

---

🧩 Code Highlights

turtle.Screen() is used to create the main game window.

head.direction keeps track of snake movement direction.

win.onkeypress() links keyboard controls to movement functions.

segments[] list dynamically stores all body parts of the snake.

delay dynamically controls the snake’s speed for smooth gameplay.

💡 Future Enhancements

🔹 Add a Main Menu with difficulty selection
🔹 Include Sound Effects for eating and collisions
🔹 Display a Game Over Screen
🔹 Implement Save/Load High Score feature

📜 License

This project is licensed under the MIT License — feel free to modify and share!

🐍 Enjoy the Game!

Eat, grow, and survive. How long can you last before you crash? 💥
Try to beat your own record and make your snake the longest in town!