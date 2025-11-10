### Ejercicio: Agrupación y Manipulación de Sets

#1. **Une los siguientes sets** en uno solo llamado `mi_set_3`:

'''
```python
   set1 = {1, 2, "tres", "cuatro"}
   set2 = {"tres", 4, 5}
```
'''
  
# 2. **Agrega** el nombre "`Damián`" al set `mi_set_3` utilizando métodos de sets.

# 3. Elimina un elemento al **azar** del set `mi_set_3`.


# Solución:
set1 = {1, 2, "tres", "cuatro"}
set2 = {"tres", 4, 5}

mi_set_3 = set1.union(set2) # Une los sets
print(mi_set_3) # Imprime el set unido
mi_set_3.add("Damián") # Agrega "Damián" al set
print(mi_set_3) # Imprime el set
mi_set_3.pop() # Elimina un elemento al azar del set
print(mi_set_3) # Imprime el set después de eliminar un elemento