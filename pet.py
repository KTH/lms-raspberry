from sense_hat import SenseHat
import time

sense = SenseHat()

red = (100, 0, 27)
whi = (100, 95, 91)
bla = (0, 0, 0)
ora = (100, 62, 0)
gra = (76, 76, 78)
bro = (72, 30, 17)
blu = (10, 17, 34)
pur = (54, 10, 33)

pet_stance1 = [
  bla, red, red, whi, whi, whi, gra, bla,
  red, red, whi, whi, bla, whi, bla, gra,
  bla, pur, whi, whi, bla, whi, bla, gra,
  bla, red, whi, whi, whi, whi, whi, gra,
  bla, red, red, whi, whi, whi, whi, bla,
  red, red, pur, bro, ora, ora, bro, bla,
  red, pur, red, red, red, red, red, pur,
  bla, blu, blu, blu, bla, blu, blu, blu
  ]
  
pet_stance2 = [
  bla, red, red, whi, whi, whi, gra, bla,
  red, red, whi, whi, bla, whi, bla, gra,
  bla, pur, whi, whi, bla, whi, bla, gra,
  bla, red, whi, whi, whi, whi, whi, gra,
  bla, red, red, whi, whi, whi, whi, bla,
  red, red, pur, bro, ora, ora, bro, bla,
  red, pur, red, red, red, red, red, pur,
  bla, bla, bla, blu, blu, blu, bla, bla
  ]

sense.set_pixels(pet_stance1)