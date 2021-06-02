import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from hashlib import sha256
from random import sample
from string import *
import os


def plot():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.bar(['힘', '민첩', '지능', '운'], [10, 20, 50, 30])
    file_name = sha256(str(sample(ascii_letters + digits, k=10)).replace("[", "").replace("]", "").replace("\'", "").replace(",", "").replace(" ", "").encode()).hexdigest()[:10]
    plt.savefig('E:/fantasy_job_test/templates/' + file_name + '.png')
    return file_name + '.png'
    

if __name__ == '__main__':
    plot()
