import os
import io
import json

class IO_json(object):
    def __init__(self, filepath, filename, filesuffix='json'):
        self.filepath = filepath # /path/to/file without the /' at the end
        self.filename = filename # FILE_NAME
        self.filesuffix = filesuffix
        # self.file_io = os.path.join(dir_name, .'.join((base_filename, filename_suffix)))
    def save(self, data):        
        if os.path.isfile('{0}/{1}.{2}'.format(self.filepath,self.filename, self.filesuffix)):
            # Append existing file
            with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename,self.filesuffix), 'a', encoding='utf-8') as f:
                f.write(unicode(json.dumps(data, ensure_ascii= False))) 
               
        else:
# Create new file
            with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), 'w', encoding='utf-8') as f:
                f.write(unicode(json.dumps(data, ensure_ascii= False)))
                # f.write(json.dumps(data, ensure_ascii= False))
        # f.write(json.dumps(data, ensure_ascii= False))
    def load(self):
        with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename,self.filesuffix), encoding='utf-8') as f:
            return f.read()
