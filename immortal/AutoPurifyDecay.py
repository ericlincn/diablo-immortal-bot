from time import sleep
from cn.daftlib.command.ICommand import ICommand
from commands.ClickCommand import ClickCommand
from cn.daftlib.events.EventDispatcher import EventDispatcher
from commands.PlayerWalkCommand import PlayerWalkCommand
from commands.SwitchPackageCommand import SwitchPackageCommand
from data.PosVars import Point, PosVars
from immortal.AutoBase import AutoBase
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.command.Executer import Executer
from scripts.General import General
from commands.MoveToCenterCommand import MoveToCenterCommand
from commands.SkillCommand import SkillCommand
from commands.MeleeAttackCommand import MeleeAttackCommand
from scripts.Items import Items
from scripts.Skills import Skill
from scripts.Skills import Skills

class AutoPurifyDecay(AutoBase, EventDispatcher):

    def __init__(self, watcher: ScreenWatcher, executer: Executer) -> None:
        
        AutoBase.__init__(self, watcher, executer)
        EventDispatcher.__init__(self)

        # self.executer.start(.2)

        self.startNavi()

    def startNavi(self):

        print("开始导航")
        box = PosVars.getDecayPercentText()
        dest = Point(int(box.x+box.width*.5), int(box.y+box.height*.5))
        self.executer.addCommmand(ClickCommand(None, dest), 18)

        self.addSkill()
        self.executer.addCommmand(ICommand(), 3)

        print("点树")
        dest = PosVars.getDecayTree()
        self.executer.addCommmand(ClickCommand(None, dest), 11)

        self.skillLoopCount = 0
        self.onSkillEnd(None)
        # self.addSkill()
        # self.executer.addCommmand(ICommand(), 7)
        # self.addSkill()
        # self.executer.addCommmand(ICommand(), 10)
        # self.addSkill()
        # self.executer.addCommmand(ICommand(), 7)
        # self.addSkill()
        # self.executer.addCommmand(ICommand(), 10)

        # self.executer.addEventListener(Event.COMPLETE, self.fightComplete)

    def onSkillEnd(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.onSkillEnd)

        if self.skillLoopCount < 5:
            self.addSkill()
            self.executer.addCommmand(ICommand(), 8)
        else:
            self.fightComplete(None)

        self.skillLoopCount += 1 

    def addSkill(self):

        self.executer.addCommmand(MoveToCenterCommand())

        arr = [1, 3, 2, 4]
        count = 0
        for i in range(0, len(arr)):
            skill = Skill(arr[i], False, 0)
            if Skills.getSkillColddown(skill) == Skills.SKILL_IS_COLD_DOWN:
                self.executer.addCommmand(SkillCommand(arr[i]))
                count += 1

        if count < 2:
            self.executer.addCommmand(MoveToCenterCommand())
            self.executer.addCommmand(MeleeAttackCommand())
            self.executer.addCommmand(MeleeAttackCommand())
            self.executer.addCommmand(MeleeAttackCommand())

        self.executer.addEventListener(Event.COMPLETE, self.onSkillEnd)

    def fightComplete(self, e):

        print("战斗结束")
        self.executer.removeEventListener(Event.COMPLETE, self.fightComplete)

        chip = Items.hasLegendrayChipOnScreen()
        print(chip)

        if chip:
            dest = Point(int(chip.left+chip.width*.5), int(chip.top+chip.height*.5))
            self.executer.addCommmand(PlayerWalkCommand(dest), 2)
            self.executer.addEventListener(Event.COMPLETE, self.pickComplete)
        else:
            self.pickComplete(None)

    def pickComplete(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.pickComplete)

        print("捡装备结束")
        self.executer.addCommmand(SwitchPackageCommand(), 2)
        dest = PosVars.getTownPortalButton(0)
        self.executer.addCommmand(ClickCommand(None, dest), 1)
        dest = PosVars.getTownPortalButton(1)
        self.executer.addCommmand(ClickCommand(None, dest), 11)

        self.executer.addEventListener(Event.COMPLETE, self.backtoTown)

    def backtoTown(self, e):

        print("回城结束")
        self.executer.removeEventListener(Event.COMPLETE, self.backtoTown)
        self.dispatchEvent(Event(Event.COMPLETE))