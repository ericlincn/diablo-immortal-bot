import sys
import threading
from time import sleep
from typing import Any
import pyautogui
import pydirectinput
import timeit
import cv2 as cv
import numpy as np
from HookKeyboard import HookKeyboard
from LegendaryReminder import LegendaryReminder

from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.events.EventPhase import EventPhase
from cn.daftlib.core.ListenerManager import ListenerManager
from cn.daftlib.core.RemovableEventDispatcher import RemovableEventDispatcher
from cn.daftlib.observer.NotificationsCenter import NotificationsCenter
from commands.ClickCenterCommand import ClickCenterCommand
from commands.ClickCommand import ClickCommand
from cn.daftlib.command.Executer import Executer
from commands.ExitDungeonCommand import ExitDungeonCommand
from commands.MeleeAttackCommand import MeleeAttackCommand
from commands.NavigateOnMapCommand import NavigateOnMapCommand
from commands.RefuseInviteCommand import RefuseInviteCommand
from commands.SkillCommand import SkillCommand
from commands.SwitchMapCommand import SwitchMapCommand

from data.PosVars import Point, PosVars
from immortal.AutoAssembly import AutoAssembly
from immortal.AutoDefendCastle import AutoDefendCastle
# from immortal.AutoEcho import AutoEcho
from immortal.AutoEchoV2 import AutoEchoV2
# from immortal.AutoFarming import AutoFarming
# from immortal.AutoFarmingV2 import AutoFarmingV2
from immortal.AutoFarmingV4 import AutoFarmingV4
from immortal.AutoPickupLegendaryV2 import AutoPickupLegendaryV2
from immortal.AutoPurifyDecay import AutoPurifyDecay
from immortal.AutoRift import AutoRift
from immortal.AutoSalvaging import AutoSalvaging
from immortal.AutoSubmitEssence import AutoSubmitEssence
# from immortal.AutoSubmitEssenceV2 import AutoSubmitEssenceV2
from immortal.AutoSwitchHorse import AutoSwitchHorse
from immortal.AutoVault import AutoVault
from scripts.General import General
from scripts.Items import Items
from scripts.Map import Map
from scripts.Skills import Skills
from cn.daftlib.time.RepeatingTimer import RepeatingTimer

GAME_TITLE = "Diablo Immortal"
if pyautogui.getWindowsWithTitle(GAME_TITLE):  
    window = pyautogui.getWindowsWithTitle(GAME_TITLE)[0]
    # window.moveTo(-14, -(65-15))

# if window:
if True:
    # General.resizeWindow(window)

    watcher = ScreenWatcher()
    executer = Executer()
    reminder = LegendaryReminder()
    # hook = HookKeyboard()
    sleep(2)
    General.resizePositionWindow()
    sleep(2)
    
    # 自动不朽回音
    # auto = AutoEchoV2(watcher, executer)

    # 自动集会
    # auto = AutoAssembly(watcher, executer)

    # 自动宝库
    # auto = AutoVault(watcher, executer)

    # 自动切马
    # auto = AutoSwitchHorse(watcher, executer)

    # 自动防守西兰加
    # auto = AutoDefendCastle(watcher, executer)

    # 自动秘境
    # auto = AutoRift(watcher, executer)

    # 自动打野
    # 佐敦
    # route = [
    #     [240,265,5], [260,139,7], [412,126,8], [500,238,5], [336,380,10], [245,471,5], [88,290,10]
    # ]
    # 扎万
    # route = [
    #     [499,66,8], [350,107,8], [208,86,8], [125,264,8], [366,375,10], [578, 384, 8], [570, 153, 12]
    # ]
    # 黑暗森林
    # route = [
    #     [352,177,11], [189,303,8], [328,386,8], [461,410,8], [673,337,10]
    # ]
    route = [
        [352,177,11], [228,138,6], [189,303,7], [239,412,5], [328,386,6], [461,410,8], [750,299,16]
    ]
    # route = [
    #     [352,177,11], [228,138,6], [189,303,7], [239,412,5], [328,386,6], [461,410,8], [727,299,16]
    # ]

    # auto = AutoFarming(watcher, executer, "zoltun1.png", route)
    # [665,215,15]
    # auto = AutoFarmingV3(wamtcher, executer, "zoltun1.png", route)

    # auto = AutoFarmingV4(watcher, executer, "wood1.png", route)
    # NotificationsCenter.register("legendary", auto)
    
    # auto = AutoFarmingV3(watcher, executer, "zavan1.png", route)
    # auto = AutoSubmitEssence(watcher, executer)
    # auto = AutoSalvaging(watcher, executer)
    # auto = AutoPickupLegendaryV2(watcher, executer)
    # auto = AutoPurifyDecay(watcher, executer)