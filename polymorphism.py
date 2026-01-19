# class Animals:
#     def speak(self):
#         return "bow bow sound"
# class dog(Animals):
#     def speak(self):
#         return "woaf!!"
# class cat(Animals):
#     def speak(self):
#         return "meow" 
# def animal_sound(animal : Animals):
#         return animal.speak()
# dog=dog()
# cat=cat()
# print(animal_sound(dog))
# print(animal_sound(cat))  
# 
# 
class dog:
    def speak(self):
        print ("woaf!!")
class cat:
    def speak(self):
        print ("meow") 
class human:
    def speak(self):
        print ("Hello") 
def make_it_speak(obj):
    obj.speak()
d=dog()
c=cat()
h=human()
make_it_speak(d)
make_it_speak(c)
make_it_speak(h)    
        
            
        
        
        
        