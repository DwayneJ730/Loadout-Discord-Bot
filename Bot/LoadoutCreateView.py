import discord
from discord.ui import View
from LoadoutCreateModalPage1 import LoadoutCreateModalPage1
from LoadoutCreateModalPage2 import LoadoutCreateModalPage2
from LoadoutCreateModalPage3 import LoadoutCreateModalPage3


class LoadoutCreateView(View):
    @discord.ui.button(label="Create Loadout (1/3)", row=0, style=discord.ButtonStyle.primary)
    async def loadout1_button_callback(self, interaction, button):
        modal = LoadoutCreateModalPage1()
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Create Loadout (2/3)", row=1, style=discord.ButtonStyle.primary)
    async def loadout2_button_callback(self, interaction, button):
        modal2 = LoadoutCreateModalPage2()
        await interaction.response.send_modal(modal2)

    @discord.ui.button(label="Create Loadout (3/3)", row=2, style=discord.ButtonStyle.primary)
    async def loadout3_button_callback(self, interaction, button):
        modal3= LoadoutCreateModalPage3()
        await interaction.response.send_modal(modal3)

    @discord.ui.button(label="Submit", row=3, style=discord.ButtonStyle.primary)
    async def submit_button_callback(self, interaction, button):
        await interaction.response.send_message("Loadout Successfully Created")
