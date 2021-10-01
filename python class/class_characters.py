

#clase para crear characteres

class Characters ():
	
    def __init__ (self, name, strength):
        
        global character_list
        character_list= {}
        self.name = name
        self.strength = strength
    

    def show_player (self):

         print (f"your player is {self.name} and your strength is {self.strength}") 

    def show_strength  (self):
        player_strength = self.strength
        return  player_strength 

    
    def show_name (self):
        player_name = self.name
        return  player_name
    

            
name_player1= input("ingresa el nombre de tu jugador 1")
strength_player1= input("ingresa la fuerza de tu jugador 1")
            
name_player2= input("ingresa el nombre de tu jugador 2")
strength_player2= input("ingresa la fuerza de tu jugador 2")

#new instancia de clase character for player1
character_1= Characters(name_player1, strength_player1)
#call method show_player
character_1.show_player()
#call method show_strength1
player1_strength = character_1.show_strength ()
#call method save_data
player1_name = character_1.show_name () 

#new instancia de clase character for player2
character_2= Characters(name_player2, strength_player2)
#call method show_strength2 
character_2.show_player()
#call method show_strength
player2_strength = character_2.show_strength ()
#call method save_data
player2_name = character_2.show_name ()



#funcion para analizar instancia de clases con personajes y comparar fuerzas

def analyse_players_class_strength ():

    global player1_strength
    global player2_strength
    global player1_name
    global player2_name
 
    if player1_strength > player2_strength:
        print (f"{player1_name} wins")
    else:
        print (f"{player2_name} wins")


analyse_players_class_strength ()




