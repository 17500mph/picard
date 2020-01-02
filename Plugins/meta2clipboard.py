# -*- coding: utf-8 -*-

PLUGIN_NAME = "Copy Metadata to Clipboard"
PLUGIN_AUTHOR = "Michael Elsdörfer, Sambhav Kothari"
PLUGIN_DESCRIPTION = "Exports track metadata to the clipboard, so it can be copied into the tracklist field on MusicBrainz"
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["2.0"]


from PyQt5 import QtWidgets
from picard.track import Track
from picard.file import File
from picard.ui.itemviews import BaseAction, register_track_action, register_file_action


class CopyTrackToClipboard(BaseAction):
    NAME = "Copy Track Metadata to Clipboard..."

    def callback(self, objs):
        if len(objs) != 1 or not isinstance(objs[0], Track):
            return
        cluster = objs[0]

        artists = set()
        for i, file in enumerate(cluster.files):
            artists.add(file.metadata["artist"])

        tracks = []
        for i, file in enumerate(cluster.files):
            try:
                i = int(file.metadata["tracknumber"])
            except:
                i += 1

            if len(artists) > 1:
                tracks.append((i, "%s. %s - %s (%s)" % (
                    i,
                    file.metadata["title"],
                    file.metadata["artist"],
                    format_time(file.metadata.length))))
            else:
                tracks.append((i, "%s. %s (%s)" % (
                    i,
                    file.metadata["title"],
                    format_time(file.metadata.length))))

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText("\n".join([x[1] for x in sorted(tracks)]))

class CopyFileToClipboard(BaseAction):
    NAME = "Copy File Metadata to Clipboard..."

    def callback(self, objs):
        if len(objs) != 1 or not isinstance(objs[0], File):
            return
        cluster = objs[0]

        artists = set()
        for i, file in enumerate(cluster.files):
            artists.add(file.metadata["artist"])

        tracks = []
        for i, file in enumerate(cluster.files):
            try:
                i = int(file.metadata["tracknumber"])
            except:
                i += 1

            if len(artists) > 1:
                tracks.append((i, "%s. %s - %s (%s)" % (
                    i,
                    file.metadata["title"],
                    file.metadata["artist"],
                    format_time(file.metadata.length))))
            else:
                tracks.append((i, "%s. %s (%s)" % (
                    i,
                    file.metadata["title"],
                    format_time(file.metadata.length))))

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText("\n".join([x[1] for x in sorted(tracks)]))


register_track_action(CopyTrackToClipboard())
register_file_action(CopyTrackToClipboard())
