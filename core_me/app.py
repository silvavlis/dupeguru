# Copyright 2016 Hardcoded Software (http://www.hardcoded.net)
#
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/gpl-3.0.html

from core.app import DupeGuru as DupeGuruBase
from . import prioritize
from . import __appname__
from . import scanner, fs
from .result_table import ResultTable

class DupeGuru(DupeGuruBase):
    NAME = __appname__
    METADATA_TO_READ = [
        'size', 'mtime', 'duration', 'bitrate', 'samplerate', 'title', 'artist',
        'album', 'genre', 'year', 'track', 'comment'
    ]
    SCANNER_CLASS = scanner.ScannerME

    def __init__(self, view):
        DupeGuruBase.__init__(self, view)
        self.fileclasses = [fs.MusicFile]

    def _get_dupe_sort_key(self, dupe, get_group, key, delta):
        if key == 'folder_path':
            dupe_folder_path = getattr(dupe, 'display_folder_path', dupe.folder_path)
            return str(dupe_folder_path).lower()
        return DupeGuruBase._get_dupe_sort_key(self, dupe, get_group, key, delta)

    def _get_group_sort_key(self, group, key):
        if key == 'folder_path':
            dupe_folder_path = getattr(group.ref, 'display_folder_path', group.ref.folder_path)
            return str(dupe_folder_path).lower()
        return DupeGuruBase._get_group_sort_key(self, group, key)

    def _prioritization_categories(self):
        return prioritize.all_categories()

    def _create_result_table(self):
        return ResultTable(self)
