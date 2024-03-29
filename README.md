# PandaBot

## A game bot that paves the way for the panda

**The bot works using the `pyautogui` and `win32con/api` libraries**
>I don't really like pyautogui for its slow speed, but in this case it's not required.
>...and this is one of my first projects, so I used that simple library

Video how PandaBot performs:

https://user-images.githubusercontent.com/104899233/232223120-c5344b1e-ae10-4995-ab47-65c4b7ee39b0.mp4

> **Full [video](https://www.youtube.com/watch?v=MLeEA3e4K_A&ab_channel=KroSheChKa) in my [YouTube](https://www.youtube.com/@kroshechka)**
----

The game is built on the principle that you have to lengthen a stick so that it falls on the next column.

- For each successful fall `+1 point`, as well as for hitting exactly in the center `+1 bonus point`
- Did you understick or overstick? - **game over**.

---

## The idea
**The bot works as follows:**
- Screenshot of the game area
> There is no need to make a screenshot of the entire game screen, just a line, `1 pixel height` at the level of the red dash (center of the column)
- Determine the distance to the center of a column. (Iterate each pixel in the line, checking if its color values are the color of the center)

- Calculate how much time it would take to press the left button to hit exactly in the center of the column
> As the stick grows at a `constant velocity`, we can assume that the **distance to the column is exactly proportional to the time spent on the "growing" of the stick**.

```python
seconds = 0.0694 + (x - 77)/613
```
- Press a button, release and wait for the panda to pass the way and return to the starting position

...repeat

**In fact, the bot can work for as long as you want!**

---

## How to launch

### [Game](https://vk.com/app8025526)

*As I have written in my previous works, the bot is written for a particular environment on the computer, the `specific location` of the window, the screen resolution, etc.*

To run this bot, you need:

- Install [python 3.X](https://www.python.org/downloads/) (3.10 recommended) together with `IDLE` on your computer **(you should run the code via IDLE!)**
- Clone this project by this command somewhere on your computer:
> **Make sure you have downloaded [git](https://git-scm.com/downloads)!**
```
git clone https://github.com/KroSheChKa/PandaBot.git
```
- Open cmd in the created folder or press RButton in the folder and click "`Git Bash Here`" and paste that:
```
pip install -r requirements.txt
```

**Particular case:** *If you have a monitor 3440x1440, then simply place the window with the game exactly half the screen on the left, set the **window scale 125%** and run it via `Python IDLE`*

In other cases it is possible to run this code on your computer, **but** you will have to `change some values` depending on the resolution of your monitor, such as:

```python
# You have to change 'left' and 'top' unless you have 3440x1440
pic = pyautogui.screenshot(region = (left, top, width, 1))
```
> [Help](https://pyautogui.readthedocs.io/en/latest/screenshot.html) to deal with `screenshot region`

**Сonvince that the width of the screenshot covers the whole game area!**

```python
# Also check whether the color of the center of the column matches this data
if r == 253 and g == 10 and b == 1:
```

**REMEMBER** that the cursor must always be on the game area for the bot to work.
```python
# X and Y should be in the game area
win32api.SetCursorPos((x,y))
```

### To start the bot press P. The same as to cause a pause. Press Q to end the bot completely.

----

*Any suggestions? You found a flaw?*

-> Leave a comment in [Discussions](https://github.com/KroSheChKa/BasketBot/discussions)
