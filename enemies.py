"""
The enemies module is responsible for defining enemy classes with various
behaviours.  It also contains logic to make enemies show up in the game at
certain points in time.
"""

from gamelib import GameElement
import turtle_adventure


class Enemy(GameElement):
    """
    Define an enemy for the Turtle's adventure game with specific behaviors
    """
    # TODO
    # * Implement __init__()
    # * Implement all methods required by the GameElement abstract class
    # * Define enemy's update logic in the update() method
    # * Check whether the player hits this enemy, then call the method
    #   game_over_lose() in TurtleAdventureGame

    def __init__(self,
                 game: "turtle_adventure.TurtleAdventureGame",
                 size: int,
                 color: str):
        pass

    def create(self) -> None:
        pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

    def delete(self) -> None:
        pass


class EnemyGenerator:
    """
    An EnemyGenerator instance is responsible for creating enemies of various
    kinds and scheduling them to appear at certain points in time.
    """

    # TODO
    # insert code to generate enemies based on the given game level; call
    # TurtleAdventureGame's add_enemy() method to add one enemy into the game
    # at a time.
    #
    # Hint: the 'game' parameter is a tkinter's frame, so it's after()
    # method can be used to schedule some future events.

    def __init__(self, game: "turtle_adventure.TurtleAdventureGame", level: int):
        self.__game: "turtle_adventure.TurtleAdventureGame" = game
        self.__level: int = level

        # example
        self.__game.after(100, self.create_enemy)

    def create_enemy(self):
        new_enemy = Enemy(self.__game, 20, "red")
        new_enemy.x = 100
        new_enemy.y = 100
        self.__game.add_enemy(new_enemy)

