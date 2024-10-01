import meteor_data_class
def read_meteor_data(file_path):
    with open(file_path,'r') as file:
        headers = file.readline().strip()
        print(f"Headers: {headers}")

        for line in file:
            fields  = line.strip().split('\t')

            if len(fields) >= 12:
                entry = meteor_data_class.MeteorDataEntry(
                    name=fields[0],
                    id_=fields[1],
                    nameType=fields[2],
                    recclass=fields[3],
                    mass=fields[4],
                    fall=fields[5],
                    year=fields[6],
                    reclat=fields[7],
                    reclong=fields[8],
                    geoLocation=fields[9],
                    states=fields[10],
                    country=fields[11]
                )
                meteor_entries.append(entry)
                return meteor_entries

def print_heavy_meteories(meteor_entries):
      print(f'{'Line':<5} {'Name':<30} {'Mass':< 12}')
      print("-"* 50)

      for idx, entry in enumerate(meteor_entries, start =1):
          if entry.mass > 2900000:
              print(f"{id<5} {entry.name:<30} {entry.mass:<12}")


def print_recent_meteories(meteor_entries):
    print(f'\n {'Line': < 5} {'Name': < 30} {entry.mass: < 12}')
    print("-" * 40)

    for idx, entry in enumerate(meteor_entries, start=1):
        if entry.year > 2013:
            print(f"{idx: < 5} {entry.name:<30} {entry.mass:<4}")

meteor_entries = read_meteor_data('meteorite_landings_data.txt')
print_heavy_meteories(meteor_entries)
print_recent_meteories(meteor_entries)




