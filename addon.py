# -*- coding: utf-8 -*-

import os
import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
from urlparse import parse_qsl
from urllib import urlencode
import json


_url = sys.argv[0]
_handle = int(sys.argv[1])


def main(paramstring):
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'play':
            play_video(params['video'])
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        #
        # This action caused one time after Kodi boot
        # Other openings the addon just show result of previous call
        list_channels(get_channels())


def play_video(path):
    play_item = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def get_channels():
    with open(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'tv.json'), 'r') as jsonfo:
        return json.load(jsonfo)


def list_channels(channels):
    xbmcplugin.setPluginCategory(_handle, 'Yandex TV')
    xbmcplugin.setContent(_handle, 'videos')

    for channel in channels:
        list_item = xbmcgui.ListItem(label=channel['title'])

        list_item.setInfo('video', {'title': channel['title'],
                                    'mediatype': 'video'})

        thumb = 'https:{0}'.format(channel['thumbnail'])
        list_item.setArt({'thumb': thumb, 'icon': thumb, 'fanart': thumb})
        list_item.setProperty('IsPlayable', 'true')

        url = get_url(action='play', video=channel['content_url'].strip())
        is_folder = False
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)

    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)


def get_url(**kwargs):
    return '{0}?{1}'.format(_url, urlencode(kwargs))


if __name__ == '__main__':
    main(sys.argv[2][1:])
