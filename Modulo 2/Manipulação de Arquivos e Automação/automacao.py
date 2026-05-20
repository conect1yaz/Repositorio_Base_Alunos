import pyautogui as pg

#pg.mouseInfo()

pg.press("win")
pg.sleep(1)

pg.write("chrome", interval= 0.5)
pg.press("enter")
pg.write("www.youtube.com", interval = 0.3)
pg.press("enter")

pg.moveTo(688,109, duration= 0.5 )
pg.sleep(1)
pg.click(688,109)
pg.sleep(0.5)

pg.write("Milky just the way you are", interval= 0.3)
pg.press("enter")
pg.moveTo(707,542, duration= 1)
pg.click(707,542, duration= 1)

pg.moveTo(1402,909, duration= 1.5)
pg.click(1402,909, duration= 0.3)