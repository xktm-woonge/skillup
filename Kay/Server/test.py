import pyautogui
import schedule

def click_at_coordinates(x, y):
    pyautogui.click(x, y)

def schedule_click(target_time, x, y):
    schedule.every().day.at(target_time).do(click_at_coordinates, x, y)

# "14:00:00"에 x: 100, y: 100 좌표를 클릭하도록 스케줄링합니다.
schedule_click("14:00:01", 257, 818)

while True:
    schedule.run_pending()
