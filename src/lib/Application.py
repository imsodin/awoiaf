import os
import io
import ConfigParser
import traceback
from pprint import pprint
import sys



class RootDirException(Exception):
    """Summary"""
    pass

class Application(object):
    """Contatin application-wide parameters

    Attributes:
        args (TYPE): Description
    """
    def __init__(self, arg=None):
        """Application setup"""
        # encoding=utf8
        reload(sys)
        sys.setdefaultencoding('utf8')

        super(Application, self).__init__()
        global settings
        self.settings = {
            'debug': 1,
            'rootdir': '',
            'datadir': '',
            'data_folders':['Charachters', 'Houses', 'Culture', 'History'],
            'data_types': ['info', 'text', 'nlp'],
            'storage_folder': {},
        }

        # Get config options
        try:
            # guess installation folder
            _cur_path =  os.path.dirname(__file__)
            self.settings['rootdir'] = os.path.realpath(_cur_path+'/../..')
            # assign data dir
            self.settings['datadir'] =  '/'.join([self.settings['rootdir'],'Data'])
            if not os.path.exists(self.settings['datadir']):
                os.makedirs(self.settings['datadir'])

            for dir_path in [self.settings['rootdir'], self.settings['datadir']]:
                if not dir_path or not os.path.isdir(dir_path):
                    raise RootDirException()
        except Exception, e:
            traceback.print_exc()

        # create folder sctructure for data storage
        for _dir_name in self.settings['data_folders']:
            _tmp_dir = '/'.join([self.settings['datadir'], _dir_name])
            if not os.path.isdir(_tmp_dir):
                os.mkdir(_tmp_dir)
            for _sub_dir in self.settings['data_types']:
                _tmp_sub_dir = '/'.join([_tmp_dir, _sub_dir])
                if not os.path.isdir(_tmp_sub_dir):
                    os.mkdir(_tmp_sub_dir)
                    print 'created:' + _tmp_sub_dir
                _temp_key = _dir_name+"_"+_sub_dir
                self.settings['storage_folder'][_temp_key] = _tmp_sub_dir


    def storeFile(self, file_path, content):
            f = io.open(file_path, 'w', encoding='utf8')
            f.write(unicode(content))
            f.close()
            sys.stderr.write(file_path+'\n')
