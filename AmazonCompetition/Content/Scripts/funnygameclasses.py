import unreal_engine as ue
import os
ue.log('Hello i am a Python module')

class Hero:

    # this is called on game start
    def begin_play(self):
        ue.print_string('Begin Play on Hero class')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        ue.print_string(dir_path)
        os.system(r'START python C:\Users\Jake\Documents\\"Unreal Projects"\AmazonCompetition\Content\Scripts\test.py')
    # this is called at every 'tick'    
    def tick(self, delta_time):
        # get current location
        location = self.uobject.get_actor_location()
        # increase Z honouring delta_time
        location.z += 100 * delta_time
        # set new location
        self.uobject.set_actor_location(location)