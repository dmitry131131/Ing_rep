import numpy as np 
import matplotlib.pyplot as plt 
from textwrap import wrap

# Раздел с параметрами графика
width_graph   = 16
hight_graph   = 9
dpi_graph     = 400
max_len_title = 50

title = "Процесс заряда и разряда конденсатора в RC-цепочке"

marker_frequency = 5
marker_size      = 6

# Раздел с параметрами АЦП
maxV = 3.3
maxB = 256

with open("settings.txt", 'r') as file:
    settings_list = []
    for line in file:
        line = line.strip()
        try:
            num = float(line)
            settings_list.append(num)
        except ValueError:
            pass

with open("data.txt", 'r') as file:
    data_list = []
    for line in file:
        line = line.strip()
        try:
            num = int(line)
            data_list.append(float((num / maxB) * maxV))
        except ValueError:
            pass

# Создание массива с данными АЦП
data_array = np.array(data_list)

# Создание массива с временем
time_list  = [float(i * settings_list[0]) for i in range(1, len(data_list)+1)]
time_array = np.array(time_list)

# Вычисление времени зарядки и разрядки
all_time       = len(data_list) * settings_list[0]
charge_time    = data_list.index(max(data_list)) * settings_list[0]
discharge_time = all_time - charge_time

fig, plt_1 = plt.subplots(figsize=(width_graph, hight_graph), dpi=dpi_graph)

plt_1.plot(time_array, data_array,
        linestyle="-",
        linewidth=2,
        color="#ac3b61",
        label="V(t)",
        marker="o",
        markerfacecolor="#123c69",
        markeredgecolor="#123c69",
        markersize=marker_size,
        markevery=marker_frequency
)

# Добавление названия графика
title_lines = wrap(title, max_len_title)
title_text  = '\n'.join(title_lines)
plt_1.set_title(title_text, loc="center")

plt_1.set_ylim(0, 3.5)
plt_1.set_xlim(0, 15)
plt_1.set_xlabel("Время, с")
plt_1.set_ylabel("Напряжение, В")

plt_1.minorticks_on()
plt_1.grid(which="major", color="#444", ls="-", lw=1)
plt_1.grid(which="minor", color="#aaa", ls=":", lw=1)

plt_1.text(12.1, 0.25, f"Общее время {round(all_time, 2)}c")
plt_1.text(12.1, 0.15, f"Время заряда {round(charge_time, 2)}c")
plt_1.text(12.1, 0.05, f"Время разряда {round(discharge_time, 2)}c")
plt_1.legend()

fig.savefig("graph.png")