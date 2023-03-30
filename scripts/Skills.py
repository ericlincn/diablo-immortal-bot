from time import sleep
import pyautogui
import pydirectinput
import collections
from data.PosVars import PosVars
from scripts.Map import Map
from utils.ColorUtil import ColorUtil
from cn.daftlib.time.RepeatingTimer import RepeatingTimer

Skill = collections.namedtuple("Skill", "keynum isChannle duration")

class Skills:

    SKILL_IS_COLD_DOWN = 1
    SKILL_IS_COOLING = -1
    SKILL_EXHAUSTED = 0

    @staticmethod
    def getSkillColddown(skill):

        targetSkillPos = None

        match skill.keynum:
            case 1:
                targetSkillPos = PosVars.getSkill1()
            case 2:
                targetSkillPos = PosVars.getSkill2()
            case 3:
                targetSkillPos = PosVars.getSkill3()
            case 4:
                targetSkillPos = PosVars.getSkill4()

        if targetSkillPos:
            
            offsetX = PosVars.getSkillColddownOffse().x
            offsetY = PosVars.getSkillColddownOffse().y

            if skill.isChannle:
                offsetX = PosVars.getChannleSkillOffseA().x
                offsetY = PosVars.getChannleSkillOffseA().y

                offsetX2 = PosVars.getChannleSkillOffseB().x
                offsetY2 = PosVars.getChannleSkillOffseB().y

                shot = pyautogui.screenshot(None, (targetSkillPos.x+offsetX, targetSkillPos.y+offsetY, 1, 1))
                p = shot.getpixel((0, 0))
                shot2 = pyautogui.screenshot(None, (targetSkillPos.x+offsetX2, targetSkillPos.y+offsetY2, 1, 1))
                p2 = shot2.getpixel((0, 0))

                if ColorUtil.getDifference(p, (119, 119, 119)) < 0.005:
                    return Skills.SKILL_EXHAUSTED
                elif ColorUtil.getDifference(p2, (255, 184, 82)) < 0.005:
                    return Skills.SKILL_IS_COLD_DOWN
                elif ColorUtil.getDifference(p, (63, 46, 0)) < 0.005:
                    return Skills.SKILL_IS_COLD_DOWN
            
            else:
                shot = pyautogui.screenshot(None, (targetSkillPos.x+offsetX, targetSkillPos.y+offsetY, 1, 1))
                p = shot.getpixel((0, 0))

                if ColorUtil.getDifference(p, (0, 0, 0)) > 0.005:
                    return Skills.SKILL_IS_COLD_DOWN
        
        return Skills.SKILL_IS_COOLING