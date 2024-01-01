import pandas as pd

def main():
    csv_data_frame = pd.read_csv('./src/Nakuru_sensor_data.csv', sep=';')
    exelFile = pd.ExcelWriter('./src/NakuruCensorData.xlsx')
    csv_data_frame.to_excel(exelFile, index=False)

    # save the resulsts
    exelFile._save()
main()
def extract_values():
  values = {}
  count = 0
  humidity = []
  temperature = []
  P1 = []
  P2 = []
  
  for value_type, value in dataframe3:
  
    if value_type['humidity']:
      humidity.append(value[count])
      ++count
    elif value_type['temperature']:
       temperature.append(value[count])
       ++count
    elif value_type['P1']:
       P1.append(value[count])
       ++count
    elif value_type['P2']:
      P2.append(value[count])
      ++count
  return {humidity, temperature, P1, P2}

