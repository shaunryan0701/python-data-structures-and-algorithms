class Cookie:
  def __init__(self, colour):
    self.colour = colour

  def get_colour(self):
    return self.colour

  def set_colour(self, colour):
    self.colour = colour 

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

cookie_one.set_colour('yellow')

print(f'Cookie one is {cookie_one.get_colour()}')
print(f'Cookie one is {cookie_two.get_colour()}')