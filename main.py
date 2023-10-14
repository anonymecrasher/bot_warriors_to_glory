import pynput
import time

mouse = pynput.mouse.Controller()
agi_location = (722, 362)
defence_location = (722, 511)
vit_location = (722, 642)
force_location = (584, 362)
att_location = (584, 511)
stam_location = (584, 642)

build_agi = (76, 24, 7, 0, 7, 55)


def left_clik(n=1):
    for i in range(n):
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)
        time.sleep(0.1)


def right_clik(n=1):
    for i in range(n):
        mouse.press(pynput.mouse.Button.right)
        mouse.release(pynput.mouse.Button.right)
        time.sleep(0.1)


def lunch_fight():
    mouse.position = (218, 250)
    left_clik()
    mouse.position = (920, 805)
    left_clik()

def set_attribut_and_stuff_agi():
    mouse.position = (196, 325)
    left_clik()
    time.sleep(0.2)
    mouse.position = (1018, 113)
    left_clik()
    time.sleep(1.5)
    left_clik()

    # set attribut

    mouse.position = agi_location
    left_clik(build_agi[0])
    mouse.position = defence_location
    left_clik(build_agi[1])
    mouse.position = vit_location
    left_clik(build_agi[2])
    mouse.position = force_location
    left_clik(build_agi[3])
    mouse.position = att_location
    left_clik(build_agi[4])
    mouse.position = stam_location
    left_clik(build_agi[5])

    # set skill

    time.sleep(0.1)
    mouse.position = (1219, 113)
    left_clik()
    time.sleep(0.1)
    mouse.position = (960, 357)
    left_clik(3)
    mouse.position = (960, 410)
    left_clik(3)
    mouse.position = (960, 530)
    left_clik(3)
    mouse.position = (960, 584)
    left_clik(4)
    mouse.position = (960, 638)
    left_clik()

    # buy items

    mouse.position = (982, 785)
    left_clik()
    time.sleep(0.5)

    mouse.position = (208, 373)
    left_clik()
    time.sleep(2.5)

    mouse.position = (983, 317)
    left_clik()
    mouse.position = (1181, 426)
    left_clik()
    mouse.position = (976, 99)
    left_clik()
    mouse.position = (1181, 426)
    left_clik()
    mouse.position = (1446, 426)
    left_clik()
    mouse.position = (1707, 426)
    left_clik()
    mouse.position = (1181, 789)
    left_clik()
    mouse.position = (1446, 789)
    left_clik()

    # equip items

    mouse.position = (463, 913)
    left_clik()
    time.sleep(0.5)

    mouse.position = (189, 630)
    right_clik()
    mouse.position = (239, 633)
    left_clik()

    mouse.position = (299, 630)
    right_clik()
    mouse.position = (350, 633)
    left_clik()

    mouse.position = (410, 630)
    right_clik()
    mouse.position = (460, 633)
    left_clik()

    mouse.position = (520, 630)
    right_clik()
    mouse.position = (570, 633)
    left_clik()

    mouse.position = (189, 761)
    right_clik()
    mouse.position = (239, 764)
    left_clik()

    mouse.position = (299, 761)
    right_clik()
    mouse.position = (350, 764)
    left_clik()

    mouse.position = (410, 761)
    right_clik()
    mouse.position = (460, 764)
    left_clik()


time.sleep(3)
set_attribut_and_stuff_agi()
