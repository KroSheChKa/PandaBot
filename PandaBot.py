import pyautogui
import time
import keyboard
import win32api, win32con

# Site: https://vk.com/app8025526, Scale - 125%

# Function to press LeftButton for a certain time
def press(sec):

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(sec)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Function that works with a plank
def plank(x):

    # Simple calculation of the time for pressing a button
    seconds = (x - 33) / 618

    print(f'Pressing button for {round(seconds, 3)} sec...')

    # Pressing LButton for (seconds)
    press(seconds)

    # Wait-time till the panda runs and gets back to the starting position
    wait = 0.6 + x / 160

    print(f'Panda runs and waits for {round(wait, 3)} sec...', end ='\n\n')

    # Wait for (seconds)
    time.sleep(wait)

def main():
    
    # Set the position of the cursor on the game window
    win32api.SetCursorPos((960,960))
    
    # Press Q to quit
    while keyboard.is_pressed('q') == False:

        # Taking a screenshot of a line
        pic = pyautogui.screenshot(region = (720,935,700,1))

        # Iterating pixels in a line (700 px)
        for x in range(700):
    
            # Getting red and green values of a pixel
            # As we have a line so  ↓ y (height) = 0
            r,g,_ = pic.getpixel((x,0))
    
            # Check if the pixel color and column center color match
            if r == 253 and g == 10:
    
                print(f'Distance: {x} pixels')
                # Press and wait till the next loop
                plank(x)

    else:
        # Width and height of the screen
        w_screen = win32api.GetSystemMetrics(0)
        h_screen = win32api.GetSystemMetrics(1)

        # As we set a limit area for cursor, we have to remove it
        win32api.ClipCursor((0,0,w_screen,h_screen))

# Entry point
if __name__ == '__main__':

    # Time to prepare
    time.sleep(2)
    
    main()
