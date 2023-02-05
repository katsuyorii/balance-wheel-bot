import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from aiogram import types
import os

class Diagramm:
    def __init__(self, user_id,  data):
        self.data = data
        self.user_id = user_id

    async def create_diagram(self):
        colors = {"Карьера" : "darkorange", "Семья": "darkviolet",  "Друзья" : "yellowgreen",  "Здоровье": "dodgerblue",  "Хобби": "crimson", " Деньги": "deeppink", "Отдых": "green", "Саморазвитие": "silver"}

        fig, ax = plt.subplots(subplot_kw = dict(polar = True))
        fig.set_figwidth(15)
        fig.set_figheight(10)
        ax.set_title('Колесо баланса', color='Black', size = 15)

        norm = np.full(len(self.data), 1/len(self.data))*2*np.pi
        left = np.cumsum(np.append(0, norm[:-1]))

        ax.bar(x = left,
            width = norm,
            bottom = 0,
            height = [max(self.data.values())]*len(self.data),
            color = 'Gray',
            edgecolor ='w',
            linewidth = 2,
            align ="edge",
            alpha = .15)

        ax.bar(x = left,
            width = norm,
            bottom = 0,
            height = self.data.values(),
            color = colors.values(),
            edgecolor ='w',
            linewidth = 2,
            align ="edge",
            alpha = 1)

        ax.set_axis_off()

        cmap = dict(zip(self.data.keys(), colors.values()))
        patches = [Patch(color=v, label=k) for k, v in cmap.items()]

        ax.legend(title='Категории:', labels=colors.keys(), handles=patches, loc=(1.12, 0.4))
        plt.savefig(f'wheel_img/balance_wheel_{self.user_id}.png')

    async def send_diagramm_user(self, message : types.Message):
        with open(f'wheel_img/balance_wheel_{message.from_user.id}.png', 'rb') as ph:
            await message.answer_photo(photo=ph)

    async def delete_wheel_graph(self):
        path = f"wheel_img/balance_wheel_{self.user_id}.png"
        os.remove(path)
