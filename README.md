# LockDown Browser Bypass for MacOS
Browse the internet, using a PIP browser window, while using [Respondus LockDown Browser](https://web.respondus.com/he/lockdownbrowser/) or [It's Learning Test Mode Browser](https://support.itslearning.com/en/support/solutions/articles/7000053270-test-mode-browser) (prøvemodus).
## Prerequisites
1. [Helium](https://github.com/JadenGeller/Helium)
2. Python 3. If you don't have Python 3, (check with `$ which python3`), see [this resouce](https://installpython3.com/mac/).

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
