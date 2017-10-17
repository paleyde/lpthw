class fail()
    
	def enter(self)
	    print "go back to the previous stage"
		
		

class stage1():
    
    def enter(self):
        print "welcome to the stage 1"
        
        action = raw_input("Distance Travelled:")
        if action >= 10
            return 'stage2'
		else:
            return 'stage1'

class stage2():
    
    def enter(self):
        print "Congo! Welcome to the stage 2"
        
        action = raw_input("Distance Travelled:")
		if action >=100
		    return 'stage3'
		else:
            return 'stage2'
			
class stage3():
    
    def enter(self):
        print "Congo! Welcome to the stage 2"
        
        action = raw_input("Number of hurdles")  

        if action >=50
            return 'stage4'
        else:
            return 'stage3'

class stage4():
    
    def enter(self):
        print "Congo! Welcome to the stage 2"
        
        action1 = raw_input("Distance Travelled")
		action2 = raw_input("Number of hurdles")  

        if action1 >=1000 and action2>=100
            return 'Finished'
        else:
            return 'stage3'			
        			
class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'		