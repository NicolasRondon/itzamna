# Accounts
Es la aplicación encargada de gestionar los usuarios dentro de
Itzamná, donde se extiende la classe UserManager debido a los nuevos
campos que son agregados en el modelo User 
 
 
##Metodos 
```python
def get_full_name():
    pass # Retorna el first_name + last_name

def get_short_name():
    pass # Retorna el username
``` 

##Campos
   - first_name (Requerido)
   - last_name (Requerido)
   - username  (Requerido)
   - email  (Requerido)
   - course 
   - gender 
   - active 
   - staff 
   - is_superuser 
   - joined_date 
