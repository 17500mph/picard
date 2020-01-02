# -*- coding: utf-8 -*-

PLUGIN_NAME = "Copy Metadata to Clipboard"
PLUGIN_AUTHOR = "Michael Elsdörfer, Sambhav Kothari"
PLUGIN_DESCRIPTION = "Exports Metadata to the clipboard."
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["2.0"]


from PyQt5 import QtWidgets
from picard.cluster import Cluster
from picard.util import format_time
from picard.ui.itemviews import BaseAction, register_cluster_action


class CopyClusterToClipboard(BaseAction):
    NAME = "Copy Metadata (tracks2clipboard) to Clipboard..."

    def callback(self, obj):
        clipboard = QtWidgets.QApplication.clipboard()
        clip = ""
        files = self.tagger.unmatched_files.files
        for index in range(len(files)):
            clip += "%s %s - %s (%s)" % (files[index].metadata["tracknumber"],
                                         files[index].metadata["artist"], files[index].metadata["title"],
                                         files[index].metadata["~length"])
            clip += '\n'
        clipboard.setText(clip)


register_cluster_action(CopyClusterToClipboard())
