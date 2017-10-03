
class Calculadora():
 def __init__(self):
    self.resultado = 0

  def obtener_resultado(self):
    return self.resultado

  def suma(self, num1, num2):
    try:
     if(num1 == 0 or num2 == 0):
      return 'No se aceptan ceros'
     elif(int(num1) > 10000 or int(num2) > 10000):
      return 'No se aceptan numeros mayores a 10,000'
     else:
      self.resultado = num1 + num2
      return self.resultado
    except:
     return 'Datos incorrectos'

  def resta(self, num1, num2):
    try:
      if(num1 == 0 or num2 == 0):
       return 'No se aceptan ceros'				
      elif(int(num1) > 10000 or int(num2) > 10000):
       return 'No se aceptan numeros mayores a 10,000'
      else:
       self.resultado = num1 - num2
       return self.resultado
     except:
      return 'Datos incorrectos'

  def multiplicacion(self, num1, num2):
    self.resultado = num1 * num2
    return self.resultado

  def division(self, num1, num2):
    self.resultado = num1 / num2
    return self.resultado

  def potencia(self, num1, num2):
    self.resultado = num1 ** num2
    return self.resultado

  def raiz(self, num):
    self.resultado = int(num ** 0.5)
    return self.resultado
