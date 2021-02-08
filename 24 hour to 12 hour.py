time = input('Time: ')
# time = '18:15'
'06:15'

timeH = time.split(':')[0]
timeM = time.split(':')[1]

if int(timeH) > 12:
    ampm = 'PM'
    if int(timeH) < 20:
        _timeH = int(timeH[1]) - 2
        _timeH = str(_timeH)
        _FtimeH = '0' + _timeH
    else:
        _timeH = int(timeH) - 2
        _FtimeH = str(_timeH)[1]
        if int(_timeH) > 19:
            _FtimeH = '1' + _FtimeH
        else:
            _FtimeH = '0' + _FtimeH
else:
    ampm = 'AM'
    if timeH == '00':
        _FtimeH = '12'
        ampm = 'PM'
    else:
        _FtimeH = timeH

print(_FtimeH + ':' + timeM + ' ' + ampm)
