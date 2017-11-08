import yaml
from subprocess import call


command = 'nativefier'

with open('app.yml') as f:
    data = yaml.load(f)
    for app in data['apps']:
        call([command,
            '-n', app['name'],
            '-i', app['icon'],
            '-e', data['meta']['electron'],
            app['url'],
            'build'])
