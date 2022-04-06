# Introduction
This is a simple, powerful Telegram Bot getting the present server status from all Lost Ark Servers.
The project was heavily inspired by [axsddlr/lost_ark_api](https://github.com/axsddlr/lost_ark_api) repository.

# Installation
Run `pip3 -r requirements.txt` to install all dependencies.

Configuring LostArk Server status Bot is easy. You just need create a config.py your present directory.

Example config.py

```python
TOKEN = "YOUR BOT TOKEN"
ALL_ADMINS = [12345678] 
TARGET_GROUP = -123456789
```
# Usage
* Enter `/start` to verify your admin permission. 
* Enter `/all_stats` to view all Lost Ark server stats.

# TODO
* Translate messages
* Help command
* Integrate specific server status