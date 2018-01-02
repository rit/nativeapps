import yaml
from subprocess import call


command = 'nativefier'

with open('app.yml') as f:
    data = yaml.load(f)
    electron = data['meta']['electron']
    for app in data['apps']:
        name = app['name']
        icon = "./icons/{}.icns".format(name)
        call([command,
            '-n', name,
            '-i', icon,
            '-e', electron,
            app['url'],
            'build'])
