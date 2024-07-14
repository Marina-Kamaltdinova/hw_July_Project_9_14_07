from pathlib import Path

import tests


def resources_path(file_name):
    return str(Path(__file__).parent.parent.joinpath(file_name))


print(resources_path('img.png.png'))
