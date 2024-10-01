import self

class MeteorDataEntry:
 def __init__(name, id_, nameType, recclass, mass, fall, year, reclat, reclong, geoLocation, states, country):
  self.name = name
  self.id = id_
  self.nameType = nameType
  self.recclass = recclass
  self.mass = mass
  self.fall = fall
  self.year = year
  self.reclat = reclat
  self.reclong = reclong
  self.geoLocation = geoLocation
  self.states = states
  self.country = country

 def __repr__(self):
  return f"MeteorDataEntry({self.name},{self.id_},{self.nameType},{self.recclass},{self.mass},{self.fall},{self.year},{self.reclat},{self.relong},{self.geoLocation},{self.states}, {self.country})"


    #def print_hi(name):
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #if __name__ == '__main__': print_hi('PyCharm')


