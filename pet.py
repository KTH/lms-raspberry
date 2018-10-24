from sense_hat import SenseHat
import time

sense = SenseHat()

red = (100, 0, 27)
whi = (100, 95, 91)
bla = (0, 0, 0)
ora = (100, 62, 0)
gra = (76, 76, 78)
bro = (72, 30, 17)
blu = (10, 17, 128)
pur = (54, 10, 33)

#pet_stance1 = [
#  bla, red, red, whi, whi, whi, gra, bla,
#  red, red, whi, whi, bla, whi, bla, gra,
#  bla, pur, whi, whi, bla, whi, bla, gra,
#  bla, red, whi, whi, whi, whi, whi, gra,
#  bla, red, red, whi, whi, whi, whi, bla,
#  red, red, pur, bro, ora, ora, bro, bla,
#  red, pur, red, red, red, red, red, pur,
#  bla, blu, blu, blu, bla, blu, blu, blu
#  ]

#pet_stance2 = [
#  bla, red, red, red, whi, gra, bla, bla,
#  red, red, red, whi, whi, bla, gra, bla,
#  bla, pur, pur, whi, whi, bla, gra, bla,
#  bla, red, red, whi, whi, whi, gra, bla,
#  bla, red, red, red, whi, whi, gra, bla,
#  red, red, pur, bro, ora, ora, bro, bla,
#  red, pur, red, red, red, red, red, pur,
#  bla, bla, blu, blu, blu, blu, bla, bla
#  ]

pet_walk1 = [
  bla, bla, ora, ora, ora, bla, bla, bla,
  bla, bla, ora, blu, ora, blu, bla, bla,
  bla, bla, ora, ora, ora, bla, bla, bla,
  bla, bla, red, red, red, bla, bla, bla,
  bla, bla, ora, red, red, ora, bla, bla,
  bla, bla, red, red, red, bla, bla, bla,
  bla, ora, ora, bla, ora, bla, bla, bla,
  bla, bla, bla, bla, ora, bla, bla, bla
  ]

pet_walk2 = [
  bla, bla, ora, ora, ora, bla, bla, bla,
  bla, bla, ora, blu, ora, blu, bla, bla,
  bla, bla, ora, ora, ora, bla, bla, bla,
  bla, bla, red, red, red, bla, bla, bla,
  bla, bla, ora, red, red, ora, bla, bla,
  bla, bla, red, red, red, bla, bla, bla,
  bla, bla, ora, ora, ora, bla, bla, bla,
  bla, bla, ora, bla, bla, bla, bla, bla
  ]

sense.clear()
x, y, z = sense.get_accelerometer_raw().values()

def walking():
	for i in range(20):
		sense.set_pixels(pet_walk1)
		time.sleep(0.25)
		sense.set_pixels(pet_walk2)
		time.sleep(0.25)

while x<2 and y<2 and z<2:
	x, y, z = sense.get_accelerometer_raw().values()

walking()