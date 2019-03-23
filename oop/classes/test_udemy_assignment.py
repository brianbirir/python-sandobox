from oop.classes.udemy_assignment import LogFile, DelimFile

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])
