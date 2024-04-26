import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

# Функция переводящая напряжение в массив 1 и 0 для вывода да плату
def to_bin(number):
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        number = number // 2
    while len(binary_list) < 8:
        binary_list.insert(0, 0)
    return binary_list

# Функция получающая значение с компаратора и переводящая в число от 0 до 255
def adc():
    res = 0
    i = 128
    while i >= 1:
        GPIO.output(dac, to_bin(int(i + res)))
        time.sleep(0.01)
        tmp = GPIO.input(comp)
        if tmp == 0:
            res += i
        i /= 2
    
    return int(res)

# Выводит значение массива 1 и 0 на плату
def num2_dac_leds(value):
    signal = to_bin(value)
    GPIO.output(dac, signal)
    return signal

# Инициализация констант
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
bits = len(dac)
levels = 2 ** bits
maxV = 3.3

# Инициализация пинов
GPIO.setmode(GPIO.BCM)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)

# Массивы значений
data_volts = []
data_times = []

try:
    # Начало измерений
    val = 0
    GPIO.output(troyka, 1)
    start_time = time.time()

    # Конденсатор заряжается только до 207
    while(val < 207):
        val = adc()
        print(f"Up: {val}")
        num2_dac_leds(val)
        data_times.append(time.time() - start_time)
        data_volts.append(val)

    discharge_start = len(data_volts)
    # Процесс разрядки
    GPIO.output(troyka, 0)

    # Конденсатор разряжается до 168
    while(val > 168):
        val = adc()
        print(f"Down: {val}")
        num2_dac_leds(val)
        data_times.append(time.time() - start_time)
        data_volts.append(val)

    # Финальное измерение времени
    end_time = time.time()

    # Записываем частоту дискретизации и шаг квантования в файл
    with open("./settings.txt", "w") as file:
        file.write("Frec:" + str((end_time - start_time) / len(data_volts)))
        file.write(("\n"))
        file.write("Voltage step:" + str(maxV / 256))

    # Печать финального сообщения
    print(end_time - start_time, " secs\n", (end_time - start_time) / len(data_volts), "\n", maxV / 256)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()

# Запись данных в файл
with open("data.txt", "w") as file:
    for i in range(discharge_start):
        print(f"{data_volts[i]}", file=file)
    for i in range(discharge_start, len(data_volts)):
        print(f"{data_volts[i]}", file=file)

# Вывод графика U(t)
plt.plot(data_times, data_volts)
plt.show()