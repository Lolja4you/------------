import serial
# Открываем Serial порт ('COMX' замените на имя вашего порта)
ser = serial.Serial('COM7', 9600)
# Читаем ответ от Arduino через Serial порт
while True:
    response = ser.readline()
    decoded_response = response.decode('utf-8')
    print(decoded_response)