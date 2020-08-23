import os
import configparser
from gi.repository import GLib


__all__ = ['load', 'get']


CONFIG_DIR = os.path.join(GLib.get_user_config_dir(), 'notifymuch')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'notifymuch.cfg')

DEFAULT_CONFIG = {
    'query': 'is:unread and is:inbox',
    'sort': 'oldest', 
    'mail_client': 'gnome-terminal -x mutt -y',
    'recency_interval_hours': '48',
    'hidden_tags': 'inbox unread attachment replied sent encrypted signed',
    'notification_format': "%%T %%t (%%s %%d)",
    'message_length': 120
}

CONFIG = configparser.ConfigParser()


def load():
    global CONFIG
    CONFIG['notifymuch'] = DEFAULT_CONFIG
    if not CONFIG.read(CONFIG_FILE):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            CONFIG.write(f)


def get(option):
    return CONFIG['notifymuch'][option]
