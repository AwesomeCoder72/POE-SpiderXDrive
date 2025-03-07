#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
motor_1 = Motor(Ports.PORT1, False)
motor_2 = Motor(Ports.PORT2, False)
motor_3 = Motor(Ports.PORT3, False)
motor_4 = Motor(Ports.PORT4, False)
distance_5 = Distance(Ports.PORT5)


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode EXP Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
import random

# Begin project code

class XDrive():
    def __init__(self, FR_drive, FL_drive, BR_drive, BL_drive, dist_sensor):
        self.fr = FR_drive
        self.fl = FL_drive
        self.br = BR_drive
        self.bl = BL_drive
        self.dst = dist_sensor

        self.x_motors = [self.fr, self.fl, self.br, self.bl]

        self.sees_object = False

        self.is_stopped = False

        self.movement_directions = ["forward", "backward", "left", "right", "spin_cw", "spin_ccw"]

        # self.movement_options = [self.spin_forward, 
        #                          self.spin_backward, 
        #                          self.spin_left, 
        #                          self.spin_right,
        #                          self.spin_turn]
    
    def set_vel(self, vel):
        for motor in self.x_motors:
            motor.set_velocity(vel, PERCENT)
    
    def spin_straight_or_turn(self, direction):
        self.is_stopped = False
        if (self.movement_directions[direction] == "forward"):
            self.fr.spin(REVERSE)  
            self.br.spin(REVERSE)
            self.fl.spin(FORWARD)
            self.bl.spin(FORWARD)
        elif (self.movement_directions[direction] == "backward"):
            self.fr.spin(FORWARD)
            self.br.spin(FORWARD)
            self.fl.spin(REVERSE)
            self.bl.spin(REVERSE)
        elif (self.movement_directions[direction] == "left"):
            self.fr.spin(REVERSE)
            self.br.spin(FORWARD)
            self.fl.spin(REVERSE)
            self.bl.spin(FORWARD)
        elif (self.movement_directions[direction] == "right"):
            self.fr.spin(FORWARD)
            self.br.spin(REVERSE)
            self.fl.spin(FORWARD)
            self.bl.spin(REVERSE)        
        elif (self.movement_directions[direction] == "spin_cw"):
            self.spin_turn(True)
        elif (self.movement_directions[direction] == "spin_ccw"):
            self.spin_turn(False)



    def spin_forward(self):
        self.fr.spin(REVERSE)  
        self.br.spin(REVERSE)
        self.fl.spin(FORWARD)
        self.bl.spin(FORWARD)

    def spin_backward(self):
        self.fr.spin(FORWARD)
        self.br.spin(FORWARD)
        self.fl.spin(REVERSE)
        self.bl.spin(REVERSE)

    def spin_left(self):
        self.fr.spin(REVERSE)
        self.br.spin(FORWARD)
        self.fl.spin(REVERSE)
        self.bl.spin(FORWARD)

    def spin_right(self):
        self.fr.spin(FORWARD)
        self.br.spin(REVERSE)
        self.fl.spin(FORWARD)
        self.bl.spin(REVERSE)

    def spin_turn(self, direction):
        self.set_vel(40)
        if direction:
            for motor in self.x_motors:
                motor.spin(FORWARD)
        else:
            for motor in self.x_motors:
                motor.spin(REVERSE)

    def select_random_movement(self, option_count):
        selection = random.randint(0, option_count)

        return selection
    
    def check_for_object(self, inches_away):
        brain.screen.set_cursor(2, 1)
        brain.screen.print( distance_5.object_distance(INCHES))
        if distance_5.object_distance(INCHES) < inches_away:
            sees_object = True
        else:
            sees_object = False
        
        return sees_object

    def main_movement_loop(self):
        time_zero = brain.timer.time(MSEC)
        new_chase_movement = True
        new_rand_movement = True

        brain.screen.set_cursor(1,1)

        x = 750

        movement_index = self.select_random_movement(5)
        time_new_movement_start = brain.timer.time(MSEC)

        while True:
            brain.screen.set_cursor(1,1)
            current_time = brain.timer.time(MSEC)


            if (self.check_for_object(12) and not self.check_for_object(3)):
                brain.screen.print(True)
                # if not self.is_stopped:
                #     self.stopall()
                self.set_vel(100)
                
                self.spin_straight_or_turn(0)

            elif (current_time - time_new_movement_start) > x:
                time_new_movement_start = brain.timer.time(MSEC)
                movement_index = self.select_random_movement(5)
                brain.screen.set_cursor(3, 1)
                # x+=x
                self.stopall()
            
            

            else:
                self.set_vel(20)
                brain.screen.print(False)

                self.spin_straight_or_turn(movement_index)

            brain.screen.set_cursor(3, 1)
            brain.screen.print(movement_index)

            wait(0.05, SECONDS)
            brain.screen.clear_screen()

            # self.stopall()        

    def move_to_theta(self, theta):
        self.fr.spin(FORWARD)
        self.br.spin(REVERSE)
        self.fl.spin(FORWARD)
        self.bl.spin(REVERSE)
        
        # my_number = atan        


    def stopall(self):
        for motor in self.x_motors:
            motor.stop()
        # self.is_stopped = True

spiderDrive = XDrive(motor_2, motor_1, motor_3, motor_4, distance_5)
spiderDrive.set_vel(20)

spiderDrive.main_movement_loop()

# spiderDrive.spin_forward()
# wait(1,SECONDS)
# spiderDrive.spin_backward()
# wait(1,SECONDS)

# spiderDrive.spin_right()
# wait(1,SECONDS)
# spiderDrive.spin_left()
# wait(1,SECONDS)

spiderDrive.stopall()
