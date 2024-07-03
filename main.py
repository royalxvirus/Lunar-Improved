import dearpygui.dearpygui as dpg
import json
import os
import sys
import threading
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
from termcolor import colored
import subprocess
import keyboard
from subprocess import call 
import psutil
from lib.events import Aimbot
import sys

import os
import uuid


dpg.create_context()
dpg.create_viewport(title='Lunar Improved [v1] created by royalxvirus', width=500, height=320, decorated=True, always_on_top=False, clear_color=(255, 255, 255, 255))
def on_insert():
    print('insert was pressed')
    dpg.set_viewport_always_top(True)
    keyboard.add_hotkey('insert', on_insert)


def on_del():
    print('delete was pressed')
    dpg.set_viewport_always_top(False)
    dpg.minimize_viewport
    keyboard.add_hotkey('delete', on_del)

dpg.show_imgui_demo
dpg.set_viewport_max_height(450)
dpg.set_viewport_max_width(525)
dpg.set_viewport_min_height(450)
dpg.set_viewport_min_width(525)
def print_me(sender):
    keyboard = Controller() 
    keyboard.press(Key.f2)#press f2 to close earlier instance of the nn windows
    keyboard.release(Key.f2)
def aimkey_alt():
    global aimkey
    aimkey = "alt"
    print(aimkey)
def aimkey_shift():
    global aimkey
    aimkey = "shift"
    print(aimkey)
def aimkey_leftMouse():
    global aimkey
    aimkey = "leftMouse"
    print(aimkey)
def aimkey_rightMouse():
    global aimkey
    aimkey = "rightMouse"
    print(aimkey)
def aimkey_ctrl():
    global aimkey
    aimkey = "ctrl"
    print(aimkey)
def aimkey_mouse5():
    global aimkey
    aimkey = "mouse5"
    print(aimkey)
def strenght(Sender):
    global aim_strenght
    print(dpg.get_value(Sender))
    aim_strenght = dpg.get_value(Sender)
def aim_height(Sender):
    global a_height
    print(dpg.get_value(Sender))
    a_height = dpg.get_value(Sender)
def detection_threshhold(Sender):
    global dt_value
    print(dpg.get_value(Sender))
    dt_value = (dpg.get_value(Sender))
def fovcolor(Sender):
    print(dpg.get_value(Sender))
def trigger_toggle(Sender):
    global trigger
    print(dpg.get_value(Sender))
    trigger = (dpg.get_value(Sender))
def aimbone(Sender):
    global bone
    print(dpg.get_value(Sender))
    bone = (dpg.get_value(Sender))
def fovslider(Sender):
    global fov
    print(dpg.get_value(Sender))
    fov = (dpg.get_value(Sender))
def triggermethod(Sender):
    global tmethod
    print(dpg.get_value(Sender))
    tmethod = (dpg.get_value(Sender))
def recoilstrength(Sender):
    global recoil
    print(dpg.get_value(Sender))
    recoil = (dpg.get_value(Sender))
def dataset(Sender):
    global data
    print(dpg.get_value(Sender))
    data = (dpg.get_value(Sender))
def xysens(Sender):
    global sens
    print(dpg.get_value(Sender))
    sens1 = (dpg.get_value(Sender))
    sens = int(sens1)
    
def scopescale(Sender):
    global ssens
    print(dpg.get_value(Sender))
    ssens1 = (dpg.get_value(Sender))
    ssens = int(ssens1)


def getAimkeyString(Sender):
    global aimkey
    dpg.get_value(Sender)
    print(dpg.get_value(Sender))
    confAimkey = dpg.get_value(Sender)
    print("Your Aimkey is",confAimkey)
    if confAimkey == "LEFT ALT":
        print("Your Aimkey is LEFT  ALT")
        aimkey = "leftAlt"
    elif confAimkey == "LEFT SHIFT":
        print("Your Aimkey is really LEFT SHIFT")
        aimkey = "leftShift"
    elif confAimkey == "RIGHT CLICK":
        print("Your Aimkey is really RIGHT MOUSE")
        aimkey = "rightMouse"
    elif confAimkey == "LEFT CLICK":
        print("Your Aimkey is really LEFT MOUSE")
        aimkey = "leftMouse"
    elif confAimkey == "MOUSE 4":
        print("Your Aimkey is really MOUSE4")
        aimkey = "mouse4"
    elif confAimkey == "MOUSE 5":
        print("Your Aimkey is really MOUSE5")
        aimkey = "mouse5"
    elif confAimkey == "CNTRL":
        print("Your Aimkey is really CNTRL")
        aimkey = "cntrl"
    elif confAimkey == "`":
        print("Your Aimkey is really `")
        aimkey = "`"
    elif confAimkey == "1":
        print("Your Aimkey is really 1")
        aimkey = "1"
    elif confAimkey == "2":
        print("Your Aimkey is really 2")
        aimkey = "2"
    elif confAimkey == "3":
        print("Your Aimkey is really 3")
        aimkey = "3"
    elif confAimkey == "4":
        print("Your Aimkey is really 4")
        aimkey = "4"
    elif confAimkey == "5":
        print("Your Aimkey is really 5")
        aimkey = "5"
    elif confAimkey == "6":
        print("Your Aimkey is really 6")
        aimkey = "6"
    elif confAimkey == "7":
        print("Your Aimkey is really 7")
        aimkey = "7"
    elif confAimkey == "8":
        print("Your Aimkey is really 8")
        aimkey = "8"
    elif confAimkey == "9":
        print("Your Aimkey is really 9")
        aimkey = "9"
    elif confAimkey == "0":
        print("Your Aimkey is really 0")
        aimkey = "0"
    elif confAimkey == "-":
        print("Your Aimkey is really -")
        aimkey = "-"
    elif confAimkey == "=":
        print("Your Aimkey is really =")
        aimkey = "="
    elif confAimkey == "Q":
        print("Your Aimkey is really Q")
        aimkey = "Q"
    elif confAimkey == "W":
        print("Your Aimkey is really W")
        aimkey = "W"
    elif confAimkey == "E":
        print("Your Aimkey is really E")
        aimkey = "E"
    elif confAimkey == "R":
        print("Your Aimkey is really R")
        aimkey = "R"
    elif confAimkey == "T":
        print("Your Aimkey is really T")
        aimkey = "T"
    elif confAimkey == "Y":
        print("Your Aimkey is really Y")
        aimkey = "Y"
    elif confAimkey == "U":
        print("Your Aimkey is really U")
        aimkey = "U"
    elif confAimkey == "I":
        print("Your Aimkey is really I")
        aimkey = "I"
    elif confAimkey == "O":
        print("Your Aimkey is really O")
        aimkey = "O"
    elif confAimkey == "P":
        print("Your Aimkey is really P")
        aimkey = "P"
    elif confAimkey == "[":
        print("Your Aimkey is really [")
        aimkey = "["
    elif confAimkey == "]":
        print("Your Aimkey is really ]")
        aimkey = "]"
    elif confAimkey == "A":
        print("Your Aimkey is really A")
        aimkey = "A"
    elif confAimkey == "S":
        print("Your Aimkey is really S")
        aimkey = "S"
    elif confAimkey == "D":
        print("Your Aimkey is really D")
        aimkey = "D"
    elif confAimkey == "F":
        print("Your Aimkey is really F")
        aimkey = "F"
    elif confAimkey == "G":
        print("Your Aimkey is really G")
        aimkey = "G"
    elif confAimkey == "H":
        print("Your Aimkey is really H")
        aimkey = "H"
    elif confAimkey == "J":
        print("Your Aimkey is really J")
        aimkey = "J"
    elif confAimkey == "K":
        print("Your Aimkey is really K")
        aimkey = "K"
    elif confAimkey == "L":
        print("Your Aimkey is really L")
        aimkey = "L"
    elif confAimkey == ";":
        print("Your Aimkey is really ;")
        aimkey = ";"
    elif confAimkey == "@":
        print("Your Aimkey is really @")
        aimkey = "@"
    elif confAimkey == "#":
        print("Your Aimkey is really #")
        aimkey = "#"
    elif confAimkey == "Z":
        print("Your Aimkey is really Z")
        aimkey = "Z"
    elif confAimkey == "'":
        print("Your Aimkey is really '")
        aimkey = "'"
    elif confAimkey == "X":
        print("Your Aimkey is really X")
        aimkey = "X"
    elif confAimkey == "C":
        print("Your Aimkey is really C")
        aimkey = "C"
    elif confAimkey == "V":
        print("Your Aimkey is really V")
        aimkey = "V"
    elif confAimkey == "B":
        print("Your Aimkey is really B")
        aimkey = "B"
    elif confAimkey == "N":
        print("Your Aimkey is really N")
        aimkey = "N"
    elif confAimkey == "M":
        print("Your Aimkey is really M")
        aimkey = "M"
    elif confAimkey == ",":
        print("Your Aimkey is really ,")
        aimkey = ","
    elif confAimkey == ".":
        print("Your Aimkey is really .")
        aimkey = "."
    elif confAimkey == "/":
        print("Your Aimkey is really /")
        aimkey = "/"
    elif confAimkey == "CAPS LOCK":
        print("Your Aimkey is really CAPS LOCK")
        aimkey = "capsLock"
    elif confAimkey == "\ ":
        print("Your Aimkey is really \ ")
        aimkey = "\ "

def thread_second():
    call(["python", "extension.py"])
    processThread = threading.Thread(target=thread_second)
    processThread.start()
def close():
    exit()
        
def setsens():
    os.system('python setSens.py')

def fov_state(Sender): #returns 1 or 0 under fov_dis depending on the state of the checkbox
    global fov_dis
    print(dpg.get_value(Sender))
    if dpg.get_value(Sender) == True:
        print("FOV circle is activated")
        fov_dis = 1
    elif dpg.get_value(Sender) == False:
        print("FOV circle is deactivated")
        fov_dis = 0

def save():
    path = os.getcwd()
    configuration = {"aimkey": aimkey, "strenght": aim_strenght,"confidence": dt_value, "trigger_enabled": trigger, "aim_bone": bone, "fov": fov, "triggermethod": tmethod, "dataset": data, "recoilstrength": recoil}
    with open('lib/config/guiconf.json', 'w') as outfile:
     json.dump(configuration, outfile)
     os.startfile(path + "//dirmanager.exe")

def savesens():
    path = os.getcwd()
    sensitivity_settings = {"xy_sens": sens, "targeting_sens": ssens, "xy_scale": 8/sens, "targeting_scale": 800/(ssens * sens)}
    with open('lib/config/config.json', 'w') as outfile:
     json.dump(sensitivity_settings, outfile)
    


def start():
    keyboard = Controller() 
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    import json
    import os
    import sys
    import threading
    import time
    from pynput import keyboard
    from termcolor import colored
    import webbrowser 
    
    def on_release(key):
        try:
            if key == keyboard.Key.f1:
                Aimbot.update_status_aimbot()
            if key == keyboard.Key.f2:
                Aimbot.clean_up()
        except NameError:
            pass   
    
    def lunar():
        global lunar
        lunar = Aimbot(collect_data = "collect_data" in sys.argv)
        lunar.start()

        os.system('cls' if os.name == 'nt' else 'clear')
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
        path_exists = os.path.exists("lib/config/config.json")
        if not path_exists or ("setup" in sys.argv):
            if not path_exists:
                print("Ingame sensitivity hasnt been configurated yet...")
            setup()
    
    def setup():
        path = "lib/config"
        if not os.path.exists(path):
            os.makedirs(path)
    
        print("In-game X and Y sensitivity have to be the same!")
        def prompt(str):
            valid_input = False
            while not valid_input:
                try:
                    number = float(input(str))
                    valid_input = True
                except ValueError:
                    print("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)")
            return number
    
        xy_sens = prompt("X-Axis and Y Sensitivity (from in-game settings): ")
        targeting_sens = prompt("Targeting Sensitivity (from in-game settings): ")
    
        print("Your in-game targeting sensitivity must be the same as your scoping sensitivity")
        sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 8/xy_sens, "targeting_scale": 800/(targeting_sens * xy_sens)}
    
        with open('lib/config/config.json', 'w') as outfile:
            json.dump(sensitivity_settings, outfile)
        print("Sensitivity configuration complete")
    
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
        path_exists = os.path.exists("lib/config/config.json")
        if not path_exists or ("setup" in sys.argv):
            if not path_exists:
                print("Ingame sensitivity hasnt been configurated yet...")
            setup()
        path_exists = os.path.exists("lib/data")
        if "collect_data" in sys.argv and not path_exists:
            os.makedirs("lib/data")
        from lib.events import Aimbot
        listener = keyboard.Listener(on_release=on_release)
        listener.start()
        lunar()

        

with dpg.theme() as global_theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (112, 112, 112, 255))
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 0))
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (20, 20, 20, 240))
                dpg.add_theme_color(dpg.mvThemeCol_Border, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (28, 28, 28, 255))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (20, 20, 20, 255))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (0, 0, 0, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (0, 0, 0, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (0, 0, 0, 255))
                dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (28, 28, 28, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (15, 15, 15, 135))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (20, 20, 20, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (120, 120, 120, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (207, 212, 207, 255))
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (90, 90, 90, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button, (50, 50, 50, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Header, (81, 81, 81, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (81, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (81, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Separator, (54, 54, 54, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (167, 46, 179, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (54, 54, 54, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (167, 46, 179, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (167, 46, 179, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (18, 26, 38, 247))
                dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (36, 66, 107, 255))
                dpg.add_theme_color(dpg.mvThemeCol_DockingPreview, (20, 20, 20, 80))
                dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg, (51, 51, 51, 255))
                dpg.add_theme_color(dpg.mvThemeCol_PlotLines, (156, 156, 156, 255))
                dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, (255, 110, 89, 255))
                dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, (230, 179, 0, 255))
                dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, (255, 153, 0, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (107, 38, 130, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (217, 168, 75, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (28, 28, 28, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (35, 35, 35, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (66, 150, 250, 89))
                dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget, (255, 255, 0, 230))
                dpg.add_theme_color(dpg.mvThemeCol_NavHighlight, (66, 150, 250, 255))
                dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight, (255, 255, 255, 179))
                dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg, (204, 204, 204, 51))
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (204, 204, 204, 89))
                dpg.add_theme_color(dpg.mvPlotCol_FrameBg, (28, 28, 28, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_PlotBg, (0, 0, 0, 128), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, (81, 81, 81, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_LegendBg, (28, 28, 28, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_LegendBorder, (20, 20, 20, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_LegendText, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_TitleText, (0, 0, 0, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_InlayText, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_XAxis, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxis, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxis2, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid2, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxis3, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid3, (255, 255, 255, 50), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_Selection, (66, 150, 250, 89), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_Query, (20, 20, 20, 255), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvPlotCol_Crosshairs, (255, 255, 255, 128), category=dpg.mvThemeCat_Plots)
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (28, 28, 28, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (107, 38, 130, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (180, 140, 54, 220), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (107, 38, 130, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100, 100))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (50, 50, 50, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (30, 30, 30, 255))
                dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (0, 0, 0, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, (0, 0, 0, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, (0, 0, 0, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_Link, (61, 133, 224, 200), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_Pin, (53, 150, 250, 180), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_PinHovered, (53, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (61, 133, 224, 30), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (61, 133, 224, 150), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_GridBackground, (40, 40, 50, 200), category=dpg.mvThemeCat_Nodes)
                dpg.add_theme_color(dpg.mvNodeCol_GridLine, (200, 200, 200, 40), category=dpg.mvThemeCat_Nodes)
dpg.bind_theme(global_theme)

dpg.window(no_background=True)

path = os.getcwd()

import webbrowser

def discord():
    webbrowser.open_new_tab("")

    
def Youtube():
    webbrowser.open_new_tab("")
    
def TikTok():
    webbrowser.open_new_tab("")

    

def exit():
    os._exit(1)

def small():
    os.startfile(path + "\square\small.exe")
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)
    #fovclass='small'

def medium():
    os.startfile(path + "\square\medium.exe")
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)
    #fovclass='medium'

def big():
    os.startfile(path + "\square\large.exe")
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)
    #fovclass='big'

def closeFov():
    subprocess.call("TASKKILL /F /IM medium.exe", shell=True)
    subprocess.call("TASKKILL /F /IM small.exe", shell=True)
    subprocess.call("TASKKILL /F /IM large.exe", shell=True)
    #fovclass='small'

def showfov():
    os.startfile(path + "\square\medium.exe")

class guiConf:
        with open("lib/config/guiconf.json") as f:
         gui_Conf = json.load(f)

smoothdef = guiConf.gui_Conf["strenght"] #gets the strenght value from the guiconf 
dtthresholddef = guiConf.gui_Conf["confidence"]
use_trigger_botdef = guiConf.gui_Conf["trigger_enabled"]
aim_bonedef = guiConf.gui_Conf["aim_bone"]
box_sizedef = guiConf.gui_Conf["fov"]
tmethoddef = guiConf.gui_Conf["triggermethod"]
aimkeydef = guiConf.gui_Conf["aimkey"]
    

with dpg.window(label="              Lunar Improved by royalxvirus",width=625,height=450,no_move=True,no_resize=True,no_close=True,no_collapse=True):
    
    with dpg.tab_bar():
     with dpg.tab(label="Aimbot"):
        bone_list = ["Head", "Body", "Legs/Feet"]
        trig_list = ["Normal", "Burst", "Tap"]
        dpg.add_input_text(label="Aimkey",uppercase=True,callback=getAimkeyString, default_value=aimkeydef)
        with dpg.group(horizontal=True):
            dpg.add_slider_float(label="Strength",min_value=1, default_value=smoothdef, max_value=10,callback = strenght)
            dpg.add_text("? ", tag="strtooltip")

            with dpg.tooltip("strtooltip"):
               dpg.add_text("How fast the aimbot will move in pixels")
        with dpg.group(horizontal=True):
            dpg.add_slider_float(label="Confidence", min_value=0.2, default_value=dtthresholddef, max_value=0.8,callback = detection_threshhold)
            dpg.add_text("?", tag="conftooltip")

            with dpg.tooltip("conftooltip"):
               dpg.add_text("How much confidence the ai needs to lock-on")
        with dpg.group(horizontal=True):
            dpg.add_slider_float(label="FOV", min_value=300, default_value=box_sizedef, max_value=1000,callback = fovslider)
            dpg.add_text("? ", tag="fovtooltip")

            with dpg.tooltip("fovtooltip"):
               dpg.add_text("The range that the ai will detect in, higher range decreases performance")
        with dpg.group(horizontal=True):
            dpg.add_checkbox(label="Show FOV", callback=showfov)
            dpg.add_button(label="Remove All FOV",callback=closeFov)
        #dpg.add_slider_float(label="Aim Height", min_value=1, default_value=30, max_value=100,callback = aim_height)
        dpg.add_separator()
        dpg.add_text("Aim Bone")
        with dpg.group(horizontal=True):
            dpg.add_combo(items=bone_list, callback=aimbone, default_value=aim_bonedef)
            dpg.add_text("? ", tag="aimbonetooltip")

            with dpg.tooltip("aimbonetooltip"):
               dpg.add_text("Where will the aimbot lock to")
            #dpg.add_button(label="Small",callback=small)
            #dpg.add_button(label="Medium",callback=medium)
            #dpg.add_button(label="Large",callback=big)
        dpg.add_separator()
        
        with dpg.group(horizontal=True):
            dpg.add_checkbox(label="Enable Triggerbot", callback=trigger_toggle, default_value=use_trigger_botdef)
            dpg.add_text("? ", tag="trigbonetooltip")

            with dpg.tooltip("trigbonetooltip"):
               dpg.add_text("Enables logic to shoot when the aimbot is 90'%' locked")
        dpg.add_text("Triggerbot Fire Method")
        dpg.add_combo(items=trig_list, callback=triggermethod, default_value=tmethoddef)
        dpg.add_separator()

        #dpg.add_slider_float(label="X and Y Sens", min_value=1.0, default_value=15.0, max_value=100.0,callback = sens)
        dpg.add_text(" ")
        dpg.add_button(label="Close",callback=exit)
        dpg.add_button(label="Start",callback=start)
        dpg.add_button(label="Save Config",callback=save)

     with dpg.tab(label=" Antirecoil "):
         dpg.add_text("Recoil Reducer")
         rstrength = guiConf.gui_Conf["recoilstrength"]
         dpg.add_slider_float(label="Strength",min_value=1, default_value=rstrength, max_value=100,callback = recoilstrength)
         with dpg.group(horizontal=True):
            dpg.add_checkbox(label="Enable only when aimed in")
            dpg.add_text("? ", tag="aimtooltip")

            with dpg.tooltip("aimtooltip"):
               dpg.add_text("Will only reduce recoil when right click is held, recommended")


         dpg.add_separator()


         dpg.add_button(label="Close",callback=exit)
         dpg.add_button(label="Start",callback=start)
         dpg.add_button(label="Save Config",callback=save)
         
     with dpg.tab(label=" Settings "):
         datasets = ['fortnite specific', 'universal']
         dpg.add_text("Chose Dataset")
         with dpg.group(horizontal=True):
            data = guiConf.gui_Conf["dataset"]
            dpg.add_combo(items=datasets, callback=dataset, default_value=data)
            dpg.add_text("? ", tag="datatooltip")

            with dpg.tooltip("datatooltip"):
               dpg.add_text("What data training will the ai detect with")
         dpg.add_text(" ")
         dpg.add_separator()
         dpg.add_input_text(label='xy sens', uppercase=True, callback=xysens)
         dpg.add_input_text(label='scope+aim sens', uppercase=True, callback=scopescale)
         dpg.add_button(label="Save Sensitivity",callback=savesens)
         
         dpg.add_button(label="Close",callback=exit)
         dpg.add_button(label="Start",callback=start)
         dpg.add_button(label="Save Config",callback=save)
     
     with dpg.tab(label="Socials Plug"):
         dpg.add_text("")
         #dpg.add_button(label="Discord",callback=discord)
         #dpg.add_button(label="Youtube",callback=Youtube)
         #dpg.add_button(label="TikTok",callback=TikTok)
         
         #ADD THESE IF YOU'RE SELLING THIS YOU SKID


        
     
    
  


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()