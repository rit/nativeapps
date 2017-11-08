import sys
import subprocess


for line in sys.stdin:
    src = line.strip()
    dest = src.replace('.png', '.icns')
    subprocess.call(['sips', '-s', 'format', 'icns', src, '--out', dest]) 
