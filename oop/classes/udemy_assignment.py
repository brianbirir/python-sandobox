import abc
import datetime


class WriteFile:

    __meta_class__ = abc.ABCMeta

    def __init__(self, content_file):
        self.content_file = content_file

    @abc.abstractmethod
    def write(self, content):
        return

    def write_line(self, content):
        with open(self.content_file, 'a+') as f:
            f.write(content + '\n')


class LogFile(WriteFile):

    def write(self, content):
        dt = datetime.datetime.now()
        date_str = dt.strftime('%Y-%m-d %H:%M')
        self.write_line('{0}    {1}'.format(date_str, content))


class DelimFile(WriteFile):

    def __init__(self, content_file, delimiter):
        super().__init__(content_file)
        self.delimiter = delimiter

    def write(self, content):
        line = self.delimiter.join(content)
        self.write_line(line)
