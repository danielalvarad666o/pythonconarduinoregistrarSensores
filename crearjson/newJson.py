import json

class Jsonn:
    

               #guaradar en el archivo exitente
   def agregarproducto(self ,diccionario,elnombre):
     with open(elnombre+'.json','w') as file:
         json.dump(diccionario,file,indent=5)
   
  
         
   def datosdeljson1(self,nombredelarchivo):    
      with open(nombredelarchivo+'.json','r') as file:
       return json.load(file)
     
   def elmpatyjson(self,nombredelarchivo):  
    try:
      with open(nombredelarchivo+'.json','r') as file:
        json.load(file)
        return True
    except:
      return False
     