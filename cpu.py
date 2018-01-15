import numpy as np

class CpuTemp:
    """Generate CPU temperature"""
    spike = False
    spike_value = 0
    value = 37.0
    temp_range = range(30, 120)

    def get_spike_value(self):
        if self.spike and np.random.ranf() < 0.5:
            self.spike = False
            return -1 * self.spike_value
        elif np.random.ranf() < 0.001:
            self.spike_value = np.random.ranf() * 50
            self.spike = True
            return self.spike_value
        else:
            return 0.0

    def update(self):
        gain = (np.random.ranf() - 0.5) * 1
        err = 0

        # add random increase
        if np.random.ranf() < 0.03:
            err = (np.random.ranf() - 0.5) * 10

        new_value = self.value + gain + err + self.get_spike_value()
        if int(new_value) in self.temp_range:
            self.value = new_value

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    cpu_temp = []
    hd_err_sda_x = []
    hd_err_sda_y = []

    cpu = CpuTemp()
    for i in range(10000):
        cpu_temp.append(cpu.value)
        if (np.random.ranf() < sigmoid(((cpu.value - 120) / 120))/10):
            hd_err_sda_x.append(i)
            hd_err_sda_y.append(cpu.value)
        cpu.update()

    plt.interactive(True)
    plt.plot(cpu_temp)
    plt.scatter(hd_err_sda_x, hd_err_sda_y, marker='+', c='r', s=502)


