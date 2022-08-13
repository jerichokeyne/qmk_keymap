import requests
import typer
import tempfile
import zipfile
from pathlib import Path
import subprocess
import serial.tools.list_ports
from rich import print
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from glob import glob

app = typer.Typer()


def get_latest_build(git_token: str):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'token {git_token}',
    }
    url = "https://api.github.com/repos/shadowwolf899/qmk_keymap/actions/artifacts/328824271/zip"
    r = requests.get(url, headers=headers)
    f_name = None
    for f in r.headers['Content-Disposition'].split(';'):
        if f.strip().startswith("filename="):
            f_name = f.split('=')[1]
            break
    return f_name, r._content


def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    ret = []
    for port, desc, _ in sorted(ports):
        if desc == 'ttyS0':
            continue
        ret.append(port)
    return ret


@app.command()
def flash(hex_file: Path = typer.Option(None), serial_port: Path = typer.Option(None), git_token: str = typer.Option(None)):
    if serial_port is None:
        ports = get_serial_ports()
        if len(ports) == 0:
            print(':x: [bold red]No serial ports found[/bold red]')
            return False
        elif len(ports) > 1:
            serial_port = Prompt.ask("Pick a serial port", choices=ports)
        else:
            serial_port = ports[0]
    tmp_dir = None
    if hex_file is None:
        if git_token is None:
            print(':x: [bold red]You must provide a git token to download new builds[/bold red]')
            return False
        with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), transient=True) as progress:
            progress.add_task(description="Get latest build info", total=None)
            f_name, zip_data = get_latest_build(git_token)
            if f_name is None:
                print(':x: [bold red]No build was found[/bold red]')
                return False
            progress.add_task(description="Saving latest build", total=None)
            tmp_dir = tempfile.TemporaryDirectory()
            out_path = Path(f'{tmp_dir.name}/{f_name}')
            out_path.write_bytes(zip_data)
            progress.add_task(description="Extracting latest build", total=None)
            with zipfile.ZipFile(out_path, 'r') as zip_ref:
                zip_ref.extractall(tmp_dir.name)
            files = glob(f"{tmp_dir.name}/*.hex")
            if len(files) == 0:
                print(':x: [bold red]No hex files found[/bold red]')
                return False
            elif len(files) > 1:
                hex_file = Prompt.ask("Pick a hex file", choices=files)
            else:
                hex_file = files[0]

    subprocess.run(['avrdude', '-c', 'avr109', '-p', 'm32u4', '-P', serial_port, '-U', f"flash:w:{hex_file}:i"])
if __name__ == '__main__':
    app()
