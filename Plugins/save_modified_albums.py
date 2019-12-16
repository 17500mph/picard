PLUGIN_NAME = 'Save Modified Albums'
PLUGIN_AUTHOR = 'ichneumon, hrglgrmpf'
PLUGIN_DESCRIPTION = '''Save all modified albums from the selection.'''
PLUGIN_VERSION = '0.2'
PLUGIN_API_VERSIONS = ['0.15', '2.0']
PLUGIN_LICENSE = "GPL-2.0"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from picard.album import Album
from picard.ui.itemviews import BaseAction, register_album_action

class SaveModifiedAlbums(BaseAction):
    NAME = 'Save Modified Albums'

    def __init__(self):
        super(save_and_rewrite_header, self).__init__()
        register_file_action(self)
        register_track_action(self)
        register_album_action(self)
        register_cluster_action(self)
        register_clusterlist_action(self)

    def callback(self, objs):
        for album in objs:
            if (isinstance(album, Album) and album.get_num_unmatched_files() != 0
              	
        def save(pf):
            metadata = Metadata()
            metadata.copy(pf.metadata)
            mf = MFile(pf.filename)
            if mf is not None:
                mf.delete()
            return pf._save_and_rename(pf.filename, metadata)
        for f in self.tagger.get_files_from_objects(obj, save=True):
            f.set_pending()
            thread.run_task(partial(save, f), f._saving_finished,
                            priority=2, thread_pool=f.tagger.save_thread_pool)



register_album_action(SaveModifiedAlbums())
