import random 

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo| ______ |oooo| ------> |Defense: {weapon_defense}
    |oooo|' .  . '|oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \ '----´           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|   \'          |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/   \          |Attack: {left_arm_attack}
  / \_/ ||| |/\| ||| \_/  \         |Defense: {left_arm_defense}
 |\/     O\=----=/O      \/|        |Energy consumption: {left_arm_energy_consump}
 <>        |=\/=|        <> ------> |
 <>       |------|       <>         |3: {right_arm_name}
|  |   _ _|======|_ _   |  |        |Is available: {right_arm_status}
//\\  / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  ||||        ||||  \__/        
      ||||        ||||          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      ><            ><           |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
    _|\_/|_      _|\_/|_        |Is available: {right_leg_status}
   /__n_n__\    /__n_n__\       |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""

class Part():
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def is_available(self):
        return not self.defense_level <= 0

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return{
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }
    
    def reduce_defense (self, attack_level):
        self.defense_level -= attack_level
        if self.defense_level <= 0:
            self.defense_level = 0
        return self.defense_level


class Robot:
    def __init__(self, name):
        self.name = name
        self.energy = 10
        self.parts=[
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=1, energy_consumption=10),
            Part("Left arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        if self.parts[part_to_use].defense_level <= 0:
            print("la parte {} no esta disponible para atacar".format(self.parts[part_to_use].name))
            return
        enemy_robot.parts[part_to_attack].reduce_defense(self.parts[part_to_use].attack_level)
        self.energy -= self.parts[part_to_use].energy_consumption

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def is_on(self):
        return self.energy > 0

    def print_energy(self):
        print("su robot tiene", self.energy, "puntos de energia restantes")

    def print_status(self):
        str_robot = robot_art.format(**self.get_part_status())
        self.print_energy()
        print(str_robot)


def build_robot():
    robot_name = input("Nombre de su robot: ")
    robot = Robot(robot_name)
    robot.print_status()
    return robot

def play():
    playing = True
    print("BIENVENIDO A EL JUEGO!")
    print("DATOS DEL JUGADOR 1")
    robot_one = build_robot()
    print("DATOS DEL JUGADOR 2")
    robot_two = build_robot()

    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()
        part_to_use = input("seleccione la parte con la que atacará [0, 1, 2, 3, 4, 5]: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        part_to_attack = input("seleccione la parte a la que atacará [0, 1, 2, 3, 4, 5]: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print("felicidades, usted ganó!!!")

play()

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
}
