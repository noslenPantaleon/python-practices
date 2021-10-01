automation_config = {}
swicht_lights = {}

class CreatedRack:


    def __init__ (self, rack_id):
  
        self.rack_id =  rack_id

    
        
      
    def add_lights(self, add_lights):

        global lights_id
        lights_id=  [] 
        self.add_lights = add_lights 
        lights_id.append (self.add_lights)
        return lights_id

    
    def add_coolers(self, add_coolers ):

        global coolers
        coolers=  [] 
        self.add_coolers = add_coolers
        coolers.append (self.add_coolers)
        return coolers

    def add_waterpumps(self, add_waterpumps ):

        global waterpumps
        waterpumps=  [] 
        self.add_waterpumps = add_waterpumps
        waterpumps.append (self.add_waterpumps)
        return waterpumps

    def add_sensors(self, add_sensors ):

        global sensors
        sensors=  [] 
        self.add_sensors = add_sensors
        sensors.append (self.add_sensors)
        return sensors


    def swicht_lights (self, light_id, action):

        global swicht_lights
        self.light_id= light_id
        self.action = action

        swicht_lights ["light_id"] = self.light_id
        swicht_lights ["action"] = self.action
        return (swicht_lights)

               

    def swicht_coolers (self, cooler_id, action):

        self.cooler_id= cooler_id
        self.action = False

        if action== 1:
            print ("on")
            self.action == 1
        else:
            print ("off")
            self.action == 0


    def lights_preset (self, rack_id, light_id, lights_on, lights_off):

        global automation_config
        automation_config = {}

        self.rack_id =  str (rack_id)
        self.light_id = light_id
        self.lights_on = lights_on 
        self.lights_off = lights_off

        automation_config["rack_id"] = self.rack_id
        automation_config ["light_id"] = self.light_id
        automation_config ["lights_on"] = self.lights_on
        automation_config ["lights_off"] = self.lights_off
        return automation_config
        


    def show_lights_preset (self):
          
        global lights_preset

        lights_config = lights_preset
        return lights_config
       
























   
           
       
    

        



    
        
    
















           
           
"""