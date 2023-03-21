import discord


class LoadoutCreateModalPage3(discord.ui.Modal, title="Create Loadout Page (3/3)"):
    underbarrel_type = discord.ui.TextInput(
        label="Underbarrel",
        required=False,
        placeholder="Enter UnderBarrel Type"
    )

    muzzle_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Muzzle",
        required=False,
        placeholder="Enter Muzzle Type"
    )

    comb_type = discord.ui.TextInput(
        label="Comb",
        required=False,
        placeholder="Enter Comb Type"
    )
    async def on_submit(self, interaction):
        await interaction.response.defer(thinking=False)
