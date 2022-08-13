from mycroft import MycroftSkill, intent_file_handler


class RobotHelper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helper.robot.intent')
    def handle_helper_robot(self, message):
        self.speak_dialog('helper.robot')


def create_skill():
    return RobotHelper()

