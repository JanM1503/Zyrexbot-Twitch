from twitchio.ext import commands
import requests
import datetime
import os
import re
import time


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token='', prefix='!', initial_channels=['zyrex1503'])
        self.ns_count = self.load_ns_count()
        self.wp_count = self.load_wp_count()
        self.nt_count = self.load_nt_count()
        self.last_ns_time = 0
        self.last_wp_time = 0     
        self.last_nt_time = 0    
        self.prefix = '!'
        
    async def event_ready(self):
        print(f'Eingelogt als | {self.nick}')


    async def event_message(self, message):
        if message and message.author:
            with open('C:\\Users\\muell\\OneDrive\\Desktop\\Zyrexbot Twitch\\messages.txt', 'a', encoding='utf-8') as f:
                f.write(f'{message.author.name}: {message.content} ({datetime.datetime.now()})\n')
            line_count = sum(1 for line in open('C:\\Users\\muell\\OneDrive\\Desktop\\Zyrexbot Twitch\\messages.txt', 'r', encoding='utf-8'))
            if line_count % 20 == 0:
                print("This is an automated message")
            

            ctx = await self.get_context(message)
            await self.invoke(ctx)

            if re.match(r"^ns$", message.content, re.IGNORECASE):
                current_time = time.time()
                if current_time - self.last_ns_time > 5:
                    self.ns_count += 1
                    self.last_ns_time = current_time
                    self.save_ns_count()
                    await message.channel.send(f"Zyrex hat {self.ns_count} mal nice getroffen! peepoClap PETTHESTREAMER")

            if re.match(r"^wp$", message.content, re.IGNORECASE):
                current_time = time.time()
                if current_time - self.last_wp_time > 5:
                    self.wp_count += 1
                    self.last_wp_time = current_time
                    self.save_wp_count()
                    await message.channel.send(f"Zyrex hat {self.wp_count} mal super gut gespielt! peepoClap PETTHESTREAMER")

            if re.match(r"^nt$", message.content, re.IGNORECASE):
                current_time = time.time()
                if current_time - self.last_nt_time > 5:
                    self.nt_count += 1
                    self.last_nt_time = current_time
                    self.save_nt_count()
                    await message.channel.send(f"Zyrex hat zum {self.nt_count} mal sein Bestes gegeben! FeelsStrongMan")
        


    def save_ns_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\ns_count.txt')
        with open(file_path, 'w') as f:
            f.write(str(self.ns_count))
        print(f"Saved ns_count to {file_path}")

    def load_ns_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\ns_count.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                if content:
                    print(f"Loaded ns_count: {content}")
                    return int(content)
        return 0

    def save_wp_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\wp_count.txt')
        with open(file_path, 'w') as f:
            f.write(str(self.wp_count))
        print(f"Saved wp_count to {file_path}")

    def load_wp_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\wp_count.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                if content:
                    print(f"Loaded wp_count: {content}")
                    return int(content)
        return 0

    def save_nt_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\nt_count.txt')
        with open(file_path, 'w') as f:
            f.write(str(self.nt_count))
        print(f"Saved nt_count to {file_path}")

    def load_nt_count(self):
        file_path = os.path.join(os.getcwd(), r'C:\Users\muell\OneDrive\Desktop\Zyrexbot Twitch\nt_count.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                if content:
                    print(f"Loaded nt_count: {content}")
                    return int(content)
        return 0

    @commands.command()
    async def lurk(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} | Danke ❤️!')

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'pong')

    @commands.command()
    async def valorant(self, ctx: commands.Context):
      response = requests.get('https://api.henrikdev.xyz/valorant/v1/account/Zyrex/1503')
      data = response.json()
      name = data['data']['name']
      tag = data['data']['tag']
      

      await ctx.send(f'@{ctx.author.name} | {name}#{tag}')


    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} | https://zyrex.live/help ')

    @commands.command()
    async def pc(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} | Nvidia 1660 Super, AMD Ryzen 5 3600, 16 GB Ram')

    @commands.command()
    async def leaderboard(self, ctx: commands.Context):

        (f' @{ctx.author.name} | die Bestenliste findest du hier https://StreamElements.com/zyrex1503/leaderboard')
    
    @commands.command()
    async def zyrex1503(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} | @zyrex1503 ist gut in Valorant')

    @commands.command()
    async def nanoleafscontrol(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} | !ocean, !pink, !blau, !rot, !grün, !gelb, !orange, !lila, !weiß, !cyan, !tomate, !blutorange')

    @commands.command()
    async def rank(self, ctx: commands.Context):
        response = requests.get('https://api.henrikdev.xyz/valorant/v2/mmr/eu/Zyrex/1503')
        data = response.json()
        currenttierpatched = data['data']['current_data']['currenttierpatched']
        ranking_in_tier = data['data']['current_data']['ranking_in_tier']
        mmr_change_to_last_game = data['data']['current_data']['mmr_change_to_last_game']

        if mmr_change_to_last_game > 0:
            mmr_change_to_last_game_text = f"{mmr_change_to_last_game}RR gewonnen"
        else:
            mmr_change_to_last_game_text = f"{mmr_change_to_last_game}RR verloren"

        emote1 = ""

        if currenttierpatched == "Ascendant 1":
            emote1 = "Ascendant1"
        elif currenttierpatched == "Ascendant 2":
            emote1 = "Ascendant1"
        elif currenttierpatched == "Ascendant 3":
            emote1 = "Ascendant1"
        elif currenttierpatched == "Immortal 1":
            emote1 = "Immortal1"
        elif currenttierpatched == "Immortal 2":
            emote1 = "Immortal1"
        elif currenttierpatched == "Immortal 3":
            emote1 = "Immortal3"
        elif currenttierpatched == "Radiant":
            emote1 = "Radiant1"

        await ctx.send(f'@{ctx.author.name} | Zyrex ist {currenttierpatched} {emote1} mit {ranking_in_tier}RR. '
                    f'Letzte Runde hat er {mmr_change_to_last_game_text}')


    @commands.command()
    async def updown(self, ctx: commands.Context):
        now = datetime.datetime.now()

        if now.hour < 6:
            last_day = now - datetime.timedelta(days=1)
            start_time = datetime.datetime(year=last_day.year, month=last_day.month, day=last_day.day, hour=6)
        else:
            start_time = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=7)

        url = 'https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/mmr-history/eu/f19f6004-4011-5075-91eb-5d9f341e713b'
        response = requests.get(url)
        data = response.json()

        net_rr_gain = 0
        total_wins = 0
        total_losses = 0
        total_draws = 0
        rr_changes = []

        if 'data' in data:
            for game in data['data']:
                game_date = datetime.datetime.fromisoformat(game['date'][:-1])
                if game_date >= start_time:
                    rr_change = game.get('last_mmr_change', 0)
                    net_rr_gain += rr_change
                    if rr_change > 0:
                        total_wins += 1
                    elif rr_change < 0:
                        total_losses += 1
                    else:
                        total_draws += 1
                    rr_changes.append(rr_change)

        rr_changes_formatted = ', '.join([f"+{rr}" if rr > 0 else f"{rr}" for rr in rr_changes])
        rr_expression = " + ".join(map(str, rr_changes))
        result_message = f'Zyrex hat heute {abs(net_rr_gain)} RR gewonnen ({total_wins}W-{total_losses}L) ({rr_changes_formatted} = {abs(net_rr_gain)})'

        if net_rr_gain > 0:
            result_message += '↑.'
        else:
            result_message += '↓.'

        await ctx.send(result_message)


    @commands.command()
    async def radiant(self, ctx: commands.Context):
        response = requests.get('https://api.henrikdev.xyz/valorant/v1/leaderboard/eu')
        data = response.json()
        mmr_response = requests.get('https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/eu/f19f6004-4011-5075-91eb-5d9f341e713b')
        mmr_data = mmr_response.json()
        elo_leaderboard = None
        elo_mmr = None

        if data and isinstance(data, list):
            radiant_players = [player for player in data if player.get('rankedRating', 0) >= 550]

            if len(radiant_players) >= 500:
                sorted_data = sorted(radiant_players, key=lambda x: x['rankedRating'], reverse=True)
                elo_leaderboard = sorted_data[499]['rankedRating'] + 2100
            else:
                await ctx.send(f'@{ctx.author.name} | Du brauchst mindestenst 550 RR to reach the Radiant.')
                return
        else:
            await ctx.send(f'@{ctx.author.name} | Keine data gefunden vom Radiant Leaderboard.')
            return

        if mmr_data and 'data' in mmr_data and 'elo' in mmr_data['data']:
            elo_mmr = mmr_data['data']['elo']
        else:
            await ctx.send(f'@{ctx.author.name} | Keine MMR data gefunden.')
            return

        if elo_leaderboard is not None and elo_mmr is not None:
            if elo_mmr > elo_leaderboard:
                await ctx.send(f'@{ctx.author.name} | Zyrex ist Radiant.')
            else:
                difference = elo_leaderboard - elo_mmr
                await ctx.send(f'@{ctx.author.name} | Zyrex is {difference}RR von Radiant Radiant1 entfernt.')
        else:
            await ctx.send(f'@{ctx.author.name} | Elo values not found.')


    async def fetch_song_info(self):
        url = 'https://api.lanyard.rest/v1/users/587711153770070032'
        response = requests.get(url)
        data = response.json()

        if data['success'] and data['data']['listening_to_spotify']:
            song_info = data['data']['spotify']
            album_art_url = song_info['album_art_url']
            album_name = song_info['album']
            artist_name = song_info['artist']
            song_name = song_info['song']

            return f"Listening to: {song_name} by {artist_name} from album {album_name}\n"
        else:
            return "Nothing is currently playing."


    @commands.command()
    async def song(self, ctx: commands.Context):
        song_info = await self.fetch_song_info()
        await ctx.send(f'@{ctx.author.name} | {song_info}')

bot = Bot()
bot.run()
