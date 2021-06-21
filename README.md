# Lazy-Meets
A script which automatically leaves a MS Teams meeting when you're not around.

## Usage

Clone the repository and install the one requirement-
``` bash
git clone https://github.com/harshil21/Lazy-Meets && pip install -r requirements.txt
```

Now, make sure that you have already joined a Microsoft Teams meeting. Next, run:

``` bash
cd "Lazy-Meets" && python main.py
```

Congrats! The script will now monitor for changes and automatically leave the meeting when its supposed to!

### How it works

The script observes the meeting list every X seconds to get the number of participants currently in the meeting. If Y number of people left the meeting in a short period of time, it leaves the meeting too. This is helpful if you're AFK or just don't like to attend class :P


## FAQ:

### How is this different from other scripts which claim to do the same thing?

This script allows to you dynamically leave a meeting. Most other scripts only leave at a particular time, which isn't practical since most meetings don't end on the dot. It's also lightweight, and doesn't require computer vision or massive libraries such as selenium.

### Why not just use the Microsoft Teams API?

This uses only a very tiny subset of the API and is hence not worth setting up for such a basic task. It also requires consent of the channel administrator (and we don't want our admins to know about this hehe).

### I keep getting a ValueError!

Make sure that you're using dark mode in the latest version of the Teams app. If problems still occur, write an issue here.


## Testing

This currently only works with dark mode enabled on *Windows*. You're welcome to open a PR supporting light mode / other platforms. Since this is entirely hardcoded, many things can go wrong, so support can be limited.
