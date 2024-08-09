####*Args e **kwargs permitem que você passe um número não especificado de argumentos para uma função.​

def soma_args(*args):
  return sum(args)



x = soma_args(18,19,20)