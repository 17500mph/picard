# -*- coding: utf-8 -*-

PLUGIN_NAME = "Copy Metadata to Clipboard"
PLUGIN_AUTHOR = "Michael Elsdörfer, Sambhav Kothari"
PLUGIN_DESCRIPTION = "Exports a cluster's tracks to the clipboard, so it can be copied into the tracklist field on MusicBrainz"
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["2.0"]


from PyQt5 import QtWidgets
from picard.cluster import Cluster
from picard.util import format_time
from picard.ui.itemviews import BaseAction, register_cluster_action


class CopyMetadataToClipboard(BaseAction):
    NAME = "Copy Metadata to Clipboard..."

    def callback(self, obj):
        clipboard = QtGui.QApplication.clipboard()
        clip = ""
        files = self.tagger.unmatched_files.files
        for index in range(len(files)):
            clip += "%s %s - %s (%s)" % (files[index].metadata["tracknumber"] if files[index].metadata["tracknumber"], files[index].metadata["artist"], files[index].metadata["title"], files[index].metadata["~length"])

        clipboard.setText(clip)


register_cluster_action(CopyMetadataToClipboard())

