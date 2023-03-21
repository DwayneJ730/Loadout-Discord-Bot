import discord


class LoadoutCreateModalPage1(discord.ui.Modal, title="Create Loadout Page (1/3)"):
    creator_name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Creator's Name",
        required=True,
        placeholder="Enter Creator's Name"
    )

    gun_name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Gun Name",
        required=True,
        placeholder="Enter Gun Name"
    )

    game_mode = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Game Mode",
        required=True,
        placeholder="WZ or MP"
    )

    ammo_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Ammo",
        required=False,
        placeholder="Enter Ammo Type"
    )

    stock_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Stock",
        required=False,
        placeholder="Enter Stock Type"
    )

    async def on_submit(self, interaction):
        await interaction.response.defer(thinking=False)
