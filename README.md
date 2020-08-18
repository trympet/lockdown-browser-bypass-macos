# LockDown Browser Bypass for MacOS
Browse the internet, using a PIP browser window, while using [Respondus LockDown Browser](https://web.respondus.com/he/lockdownbrowser/) or [It's Learning Test Mode Browser](https://support.itslearning.com/en/support/solutions/articles/7000053270-test-mode-browser) (prøvemodus).
## How it works
Unlike many other "hacks", this implementation does not utilize binary patching or other modifications. It simply circumvents the lockdown functionality by making a call to the [window manager](https://en.wikipedia.org/wiki/Window_manager), telling it to put the Helium window on top after LDB has been launched. Now you have a small PIP browser that always stays on top. Also, since Helium is a picture in picture browser, the window doesn't disappear when you click outside of the bounds.

## I'm on Windows!
If you are on Windows, and you have a little programming experience, you can simply fetch the window handle of the application you wish to put on top, and call the [ShowWindow](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow) and [SetWindowPos](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowpos) function, for instance in a PowerShell script. Feel free to send a PR if you have a working implementation on Windows :)

## Prerequisites
1. [Helium](https://github.com/JadenGeller/Helium)
1. Python 3. If you don't have Python 3, (check with `$ which python3`), see [this resource](https://installpython3.com/mac/).

## Installation
1. Clone the repository and install dependencies.  
```
git clone https://github.com/trympet/lockdown-browser-bypass-macos.git ~/Documents/lockdown-browser-bypass &&
cd $_ &&
pip3 install -r requirements.txt &&
chmod +x lockdown-bypass.py
```

## Usage
1. Start Helium   
2. Start the script: `python3 ~/Documents/lockdown-browser-bypass/lockdown-bypass.py`   
3. Click a valid lockdown browser URI to start the lockdown browser session within 10 secs.   
You can use [this site](https://webassign.com/instructors/features/secure-testing/lockdown-browser/) to test it out
