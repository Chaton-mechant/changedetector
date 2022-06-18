import time
import os
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pyfiglet import Figlet
from ._purcent import Loader as __Loader


os.system('cls' if os.name == 'nt' else 'clear')
f = Figlet(font='banner3-D', width=80)
print(f.renderText('Change'))
print(f.renderText('Detect'))
global language
language = input("Enter the language you want to use: ( ruby | python | c++ ) ").lower()
if language in ["python", "py", "python3"]:
    CMD = 'py'
elif language in ["ruby", "rb"]:
    CMD = 'ruby'
elif language in ["c++", "cpp"]:
    CMD = input("Enter the compiler you want to use: ( g++ | clang++ | ...) ")
    OPTION = input("Enter compilation options you want to use: (None)").split(" ")
    if OPTION in ["none", "", " "]:
        OPTION = [""]
    OUTPUT_ATTRIBUTE = input("Enter the output attribute you want to use: (-o)")
    if OUTPUT_ATTRIBUTE in ["", " "]:
        OUTPUT_ATTRIBUTE = "-o"
    OUTPUT_FILE = input("Enter the output file you want to use: (out.exe)").lower()
    if OUTPUT_FILE in ["", " "]:
        OUTPUT_FILE = "out.exe"
else:
    print("❌ Wrong language")
    sys.exit()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE = input(f"Enter the file you want to watch the base directory\n|-> {BASE_DIR}\... \n")
THE_FILE = os.path.join(BASE_DIR, f'{FILE}')
# Check if the file's path is valid
if not os.path.isfile(THE_FILE) or THE_FILE == " " or THE_FILE == "":
    print("❌ File not found")
    sys.exit()

if language in ["c++", "cpp"]:
    COMMAND_LIST = [CMD]
    COMMAND_LIST.extend(iter(OPTION))
    COMMAND_LIST.append(THE_FILE)
    COMMAND_LIST.append(OUTPUT_ATTRIBUTE)
    COMMAND_LIST.append(OUTPUT_FILE)


def __language_output():
    h = __Loader()
    h.run()
    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    if language in ["ruby", "rb"]:
        __ruby_output()
    elif language in ["python", "py", "python3"]:
        __python_output()
    elif language in ["c++", "cpp"]:
        __cpp_output()

def __cpp_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('C++'))
    print(f"{THE_FILE}")

def __python_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('Python'))
    print(f"{THE_FILE}")


def __ruby_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('Ruby'))
    print(f"{THE_FILE}")

__language_output()

class _Watcher:
    DIRECTORY_TO_WATCH = BASE_DIR

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = _Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception:
            self.observer.stop()
            print ("❌ Exiting program...")

        self.observer.join()


class _Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"+ Received created event - {event.src_path}.")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if event.src_path == THE_FILE:
                print("OUTPUT")
                print("═══════════════════════════════════════════════════════════")
                if language not in ["cpp", "c++", "c"]:
                    now = time.perf_counter()
                    subprocess.call([CMD, f'{THE_FILE}'])
                    end = time.perf_counter()
                else:
                    now = time.perf_counter()
                    subprocess.call(COMMAND_LIST)
                    end = time.perf_counter()
                    print("COMPLILATON COMPLETED")
                print("═══════════════════════════════════════════════════════════")
                print(f"{end - now}s")
                # get the time of execution

                print(" ")
                print("---")
                print("✅ Listening for changes...")
            elif event.src_path == f'{BASE_DIR}\detectchange.py':
                print("❗RESTART THE PROGRAM FOR APPLY CHANGES❗")
            else:
                print(f"+ Received modified event - {event.src_path}.")
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print(f"- Received deleted event - {event.src_path}.")


def activate() -> None:
    """
    Detect change in the Root directory and execute the program chosen.
    ```python
    from changedetector import detectchange
    detectchange.activate()
    ```
    """
    w = _Watcher()
    print(" ")
    print("👀 Watching...")
    print(" ")
    w.run()

