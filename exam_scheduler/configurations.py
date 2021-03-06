import os

from srblib import abs_path
from srblib import SrbJson

config_file_path = abs_path('~/.config/exam_scheduler/config.json')
default_output_xlsx_path = abs_path('./output.xls')

_default_room_list = None
_default_teachers_list = None
_default_schedule_list = None

if os.path.exists(abs_path('input/')):
    for fname in os.listdir(abs_path('input/')):
        fname = 'input/' + fname
        if not _default_room_list and 'room_list' in fname:
            _default_room_list = abs_path(fname)
        elif not _default_teachers_list and 'teachers_list' in fname:
            _default_teachers_list = abs_path(fname)
        elif not _default_schedule_list and 'schedule_list' in fname:
            _default_schedule_list = abs_path(fname)

for fname in os.listdir(abs_path('./')):
    if not _default_room_list and 'room_list' in fname:
        _default_room_list = abs_path(fname)
    elif not _default_teachers_list and 'teachers_list' in fname:
        _default_teachers_list = abs_path(fname)
    elif not _default_schedule_list and 'schedule_list' in fname:
        _default_schedule_list = abs_path(fname)

_config_template = \
{
    'room_list':_default_room_list,
    'teachers_list':_default_teachers_list,
    'schedule_list':_default_schedule_list,
}

config_json = SrbJson(config_file_path,_config_template)

for var_name in ['room_list','teachers_list','schedule_list']:
    if config_json[var_name] and not os.path.isfile(config_json[var_name]):
        config_json[var_name] = None
    if not config_json[var_name]:
        config_json[var_name] = _config_template[var_name]
