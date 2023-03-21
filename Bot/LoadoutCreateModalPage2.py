import discord


class LoadoutCreateModalPage2(discord.ui.Modal, title="Create Loadout Page (2/3)"):
    barrel_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Barrel",
        required=False,
        placeholder="Enter Barrel Type"
    )

    laser_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Laser",
        required=False,
        placeholder="Enter Laser Type"
    )

    magazine_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Magazine",
        required=False,
        placeholder="Enter Magazine Type"
    )

    optic_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Optic",
        required=False,
        placeholder="Enter Optic Type"
    )

    rear_grip = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Rear Grip",
        required=False,
        placeholder="Enter Rear Grip"
    )

    async def on_submit(self, interaction):
        await interaction.response.defer(thinking=False)
