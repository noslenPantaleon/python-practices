import rack_class                # import CreatedRack class
import json
from datetime import datetime
import time

datetime_now= datetime.now ()
print (datetime_now.strftime ('%d/%m/%Y %H:%M:%S'))
hour= (datetime_now.strftime ('%H'))

rack1= rack_class.CreatedRack ("rack1")  
rack1.add_lights ([1,2,3,4])                                               # call add_lights method                                    
lights_preset = rack1.lights_preset("rack1", [1,2,3,4], 8, 20)         # call add_lights method 
lights_on = lights_preset['lights_on']                                     # get light_on data from returned dictionary 
lights_off = lights_preset['lights_off']                                   # get light_off data from returned dictionary
coolers = rack1.add_coolers(["c1","c2","c3","c4"]) 


def add_light_config ():

    light_input_id =  input ("ingrese el numero de id")
    light_input_state= input ("ingrese 1 para encender luz, o 0 para apagar luz")
    light = rack1.swicht_lights (str (light_input_id),  int (light_input_state)) 
    rack1.show_lights_preset
  

add_light_config ()
