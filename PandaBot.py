import pyautogui
import time
import win32api, win32con
import sys, ctypes

# Game: https://vk.com/app8025526, Scale - 125%

# Press P to pause the bot
def pause():
    print(16 * '=','Paused', 16 * '=', sep ="")
    time.sleep(0.2)
    while not(is_key_pressed(0x50)):
        if is_key_pressed(0x51):
            sys.exit()
        pass
    print(16 * '=','Unaused', 15 * '=', sep = "")


# Check whether the key is pressed
def is_key_pressed(key):
    return ctypes.windll.user32.GetAsyncKeyState(key) & 0x8000 != 0

# New sleep func. that you could stop by pressing the stop key (q = 0x51)
def sleep_key(sec, key_code = 0x51, pause_key_code = 0x50):
    start_time = time.time()
    
    while True:
        # ExitKey pressed during the loop? - exit the entire program
        if is_key_pressed(key_code):
            sys.exit()

        if is_key_pressed(pause_key_code):
            pause()
            return
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # If the time has run out, exit the loop
        if elapsed_time >= sec:
            return

# Function to press LeftButton for a certain time
def press(sec):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(sec)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Function that works with a plank
def plank(x, coefficient, first_run):

    # For the first run the column is further on 35 px
    if first_run == True:
        x = x + 35

    # Simple calculation of the time for pressing a button
    seconds = 0.0694 + (x - 77) / 613
    
    print(f'Pressing button for {round(seconds, 3)} sec...')

    # Pressing LButton for (seconds)
    press(seconds)

    # Wait-time till the panda runs and gets back to the starting position
    wait = 0.6 + x / coefficient 

    print(f'Panda runs and waits for {round(wait, 3)} sec...')

    # Wait for (seconds)
    sleep_key(wait)

def main():
    # Width and height of the screen
    w_screen = win32api.GetSystemMetrics(0)
    h_screen = win32api.GetSystemMetrics(1)

    # Coefficient for formula in plank()
    coeff = w_screen * h_screen / 31000

    # You have to change 'left' and 'top' unless you have 3440x1440
    # You also need to check whether the whole range falls within the 'width'
    left, top, width = 720, 938, 650
    line_screenshot = (left, top, width, 1)
    
    # Set the position of the cursor on the game window
    win32api.SetCursorPos((600,600))

    # First run flag
    flag = True

    # Try to catch the problem with detection
    error_count = 0

    # Press Q to quit
    while not(is_key_pressed(0x51)):
        print('=' * 38)
        
        
        # Taking a screenshot of a line
        pic = pyautogui.screenshot(region = line_screenshot)
        
        # Iterating pixels in a line (700 px)
        for x in range(width):
            
            # Getting red and green values of a pixel
            # As we have a line so  ↓ y (height) = 0
            r,g,b = pic.getpixel((x,0))
            
            # Check if the pixel color and column center color match
            if r == 253 and g == 10 and b == 1:
    
                print(f'Distance: {x} pixels')
                
                # Press and wait till the next loop
                plank(x, coeff, flag)

                # First game played
                flag = False
                error_count = 0
                break
        else:
            error_count += 1
            # If you here probably you have problem in line 81 or in 109
            if error_count == 3:
                print('CANNOT DETECT THE RED LINE. CHECK COORDINATES.')
                sys.exit()

# Entry point
if __name__ == '__main__':

    # Press Q to start
    while not(is_key_pressed(0x50)):
        pass

    # Instantly release the button
    win32api.keybd_event(0x50, 0, win32con.KEYEVENTF_KEYUP, 0)

    main()
