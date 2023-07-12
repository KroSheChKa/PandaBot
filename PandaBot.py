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
def plank(x, coefficient, first_run):

    # For the first run the column is further on 35 px
    if first_run == True:
        x = x + 35

    # Simple calculation of the time for pressing a button
    seconds = 0.0694 + (x - 77)/613
    
    print(f'Pressing button for {round(seconds, 3)} sec...')

    # Pressing LButton for (seconds)
    press(seconds)

    # Wait-time till the panda runs and gets back to the starting position
    wait = 0.6 + x / coefficient 

    print(f'Panda runs and waits for {round(wait, 3)} sec...')

    # Wait for (seconds)
    time.sleep(wait)

def main():
    # Width and height of the screen
    w_screen = win32api.GetSystemMetrics(0)
    h_screen = win32api.GetSystemMetrics(1)

    # Coefficient for formula in plank()
    coeff = w_screen * h_screen / 31000

    # You have to change 'left' and 'top' unless you have 3440x1440
    left, top, width = 720, 945, 650
    line_screenshot = (left, top, width, 1)
    
    # Set the position of the cursor on the game window
    win32api.SetCursorPos((600,600))

    # First run flag
    flag = True

    # Press Q to quit
    while keyboard.is_pressed('q') == False:
        
        print('=' * 38)
        
        # Taking a screenshot of a line (you should manage 3 )
        pic = pyautogui.screenshot(region = line_screenshot)
        
        # Iterating pixels in a line (700 px)
        for x in range(width):
            
            # Getting red and green values of a pixel
            # As we have a line so  ↓ y (height) = 0
            r,g,b = pic.getpixel((x,0))
            
            # Check if the pixel color and column center color match
            if r == 238 and g == 50 and b == 34:
    
                print(f'Distance: {x} pixels')
                
                # Press and wait till the next loop
                plank(x, coeff, flag)

                # First game played
                flag = False
                
                break

# Entry point
if __name__ == '__main__':

    # Time to prepare
    time.sleep(2)
    
    main()
