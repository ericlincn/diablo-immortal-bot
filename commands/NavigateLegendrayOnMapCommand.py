from commands.NavigateOnMapCommand import NavigateOnMapCommand
from scripts.Map import Map

class NavigateLegendrayOnMapCommand(NavigateOnMapCommand):

    def getBox(self):

        box = Map.getLegendaryBoxInMap()
        print("NavigateLegendrayOnMapCommand", box)
        return box