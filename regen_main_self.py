from pathlib import Path

src_path = Path('main.py')
dst_path = Path('main_self.py')
text = src_path.read_text(encoding='utf-8')

# Remove bot command framework import
text = text.replace('from discord.ext import commands\n', '')

# Replace bot runtime with client runtime
text = text.replace("bot     = commands.Bot(command_prefix='!', intents=intents)\n", 'client = discord.Client(intents=intents)\n')
text = text.replace('await bot.fetch_user(uid)', 'await client.fetch_user(uid)')
text = text.replace('acts = _actions(server_id, bot.user.id)', 'acts = _actions(server_id, client.user.id)')
text = text.replace('try:\n        pt = getattr(ActivityType, BOT_PRESENCE["type"].lower(), ActivityType.playing)\n        await bot.change_presence(activity=Activity(type=pt, name=BOT_PRESENCE["text"]))\n    except: pass\n',
                    'try:\n        pt = getattr(ActivityType, BOT_PRESENCE["type"].lower(), ActivityType.playing)\n        await client.change_presence(activity=Activity(type=pt, name=BOT_PRESENCE["text"]))\n    except: pass\n')
text = text.replace('@bot.event', '@client.event')
text = text.replace('await bot.process_commands(message)\n', '')
text = text.replace('bot.run(bot_token, log_handler=None)', 'client.run(user_token)')

# Replace direct bot references
text = text.replace('bot.get_guild(int(sid))', 'client.get_guild(int(sid))')
text = text.replace('bot.', 'client.')

# Use user_token variable
text = text.replace("bot_token = input(f\"  {R1}{B}>>{RS} {wht('token  ')} {D2}:{RS} \" ).strip()\n",
                    "user_token = input(f\"  {R1}{B}>>{RS} {wht('token  ')} {D2}:{RS} \" ).strip()\n")
text = text.replace('if not bot_token or not server_id:', 'if not user_token or not server_id:')

# Fix banner labels and any remaining bot wording
text = text.replace('def _print_banner(bot_n="", srv_n="", members=0, animated=False):', 'def _print_banner(user_n="", srv_n="", members=0, animated=False):')
text = text.replace('  {DIM}bot{RS} ', '  {DIM}user{RS} ')
text = text.replace('if not guild: log_err("bot not in this server"); return', 'if not guild: log_err("user not in this server"); return')

# Add safe client initialization
text = text.replace('intents = discord.Intents.all()\nclient = discord.Client(intents=intents)\n',
                    'intents = None\nif hasattr(discord, "Intents"):\n    intents = discord.Intents.all()\n\nclient = discord.Client(intents=intents) if intents is not None else discord.Client()\n')

# Ensure correct UTF-8 writing
dst_path.write_text(text, encoding='utf-8')
print('main_self.py regenerated successfully')
