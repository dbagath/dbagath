import traceback

lst = [1,2,3,4,5]
dicta={11:"one",22:"two"}

try:
  print(lst[4], int("5"), dicta[22], 5+5, st)

except Exception:
  print("Exception")
  traceback.print_exc()  
except ValueError:
  print("ValueError")
  traceback.print_exc()  
except IndexError:
  print("IndexError")
  traceback.print_exc()  
except KeyError:
  print("KeyError")
  traceback.print_exc()  
except TypeError:
  print("TypeError")
  traceback.print_exc() 
except NameError:
  print("NameError") 
  traceback.print_exc()

else:
  print("Else block")

print("Normal execution")
