import random

random.seed(0)


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.turn_total = 0

    def add_points(self, turn_points):
        self.turn_total += turn_points
        print(f"Player {self.name} | Turn total: {self.turn_total} | Potential game total: "
              f"{self.total + self.turn_total}")

    def accumulated_points(self):
        self.total += self.turn_total
        self.turn_total = 0
        print(f"Player {self.name} | Current total: {self.total}")

    def decision(self):
        choice = input('Enter "r" to roll or "h" to hold. ').lower()
        return choice


class Game:
    def __init__(self, players, die):
        self.players = players
        self.die = die
        self.current_player = None

    def next_player(self):
        if self.current_player is None:
            self.current_player = 0
        else:
            self.current_player += 1
            if self.current_player == len(players):
                self.current_player = 0

        print(f"Player {self.players[self.current_player].name}\'s turn")
        return self.players[self.current_player]

    def check_winner(self):
        for player in self.players:
            if player.total >= 100:
                return True
        else:
            return False

    def turn(self):
        current_player = self.next_player()
        while not self.check_winner():
            choice = current_player.decision()
            if choice == 'r':
                roll = self.die.roll()
                if roll != 1:
                    print(f"Player {current_player.name} rolled a {roll}.")
                    current_player.add_points(roll)
                else:
                    print(f"Player {current_player.name} rolled a 1 and scratched.")
                    current_player.turn_total = 0
                    current_player.accumulated_points()
                    print("-------------------------------------------------------")
                    current_player = self.next_player()
            elif choice == 'h':
                current_player.accumulated_points()
                if not self.check_winner():
                    print("-------------------------------------------------------")
                    current_player = self.next_player()
                else:
                    print(f"Player {current_player.name} has won the game with {current_player.total} points!!!")

            else:
                print('Invalid entry. Enter "r" to roll or "h" to hold.')
                continue


if __name__ == '__main__':
    print("Welcome to Pig")

    die = Die()
    players = [Player("One"), Player("Two")]
    game = Game(players, die)
    game.turn()
