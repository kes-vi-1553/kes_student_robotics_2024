ROTATE_LEFT = 1
LEFT_PIN = 0
STRAIGHT_LEFT = -1

RIGHT_PIN = 1
ROTATE_RIGHT = 1
STRAIGHT_RIGHT = -1

ROTATE_SPEED = 0.5

class Movement:
    def __init__(self, robot):
        self.robot = robot

    def set_rotate_servos(self):
        self.robot.servo_board.servos[LEFT_PIN].position = ROTATE_LEFT
        self.robot.servo_board.servos[RIGHT_PIN].position = ROTATE_RIGHT

    def set_straight_servos(self):
        self.robot.servo_board.servos[LEFT_PIN].position = STRAIGHT_LEFT
        self.robot.servo_board.servos[RIGHT_PIN].position = STRAIGHT_RIGHT

    def forward(self, time, speed):
        self.set_straight_servos()
        self.robot.motor_board.motors[0].power = speed
        self.robot.motor_board.motors[1].power = speed
        self.robot.sleep(time)
        self.robot.motor_board.motors[0].power = 0
        self.robot.motor_board.motors[1].power = 0

    def rotate_right(self, time):
        self.set_rotate_servos()
        self.robot.motor_board.motors[0].power = -ROTATE_SPEED
        self.robot.motor_board.motors[1].power = ROTATE_SPEED
        self.robot.sleep(time)
        self.robot.motor_board.motors[0].power = 0
        self.robot.motor_board.motors[1].power = 0
        
    def rotate_left(self, time):
        self.set_rotate_servos()
        self.robot.motor_board.motors[0].power = ROTATE_SPEED
        self.robot.motor_board.motors[1].power = -ROTATE_SPEED
        self.robot.sleep(time)
        self.robot.motor_board.motors[0].power = 0
        self.robot.motor_board.motors[1].power = 0