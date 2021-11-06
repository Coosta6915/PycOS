# ===== theme =====

BACKGROUND_COLOUR = (255, 0, 0) # colour in rgb
# background colour
# allowed values: tuple ranging from (0, 0, 0) to (255, 255, 255)
# recommended values: any
# default: (255, 0, 0)

TEXT_COLOUR = (255, 255, 255) # colour in rgb
# text colour
# allowed values: tuple ranging from (0, 0, 0) to (255, 255, 255)
# recommended values: any
# default value: (255, 255, 255)

SEPARATOR_COLOUR = (255, 85, 85) # colour in rgb
# separator colour
# allowed values: tuple ranging from (0, 0, 0) to (255, 255, 255)
# recommended values: any
# default value: (255, 85, 85)



# ===== general =====

DEFAULT_DISPLAY_BRIGHTNESS = 0.8 # percantage (0.8 becomes 80%)
# default brightness of the display
# allowed values: float ranging from 0.0 to 1.0
# recommended values: 0.3 - 1.0
# default value: 0.8



# ===== advanced =====

REFRESH_DELAY = 250 # time in milliseconds
# how long the device waits before accepting input after the refresh() function is called
# allowed values: any positive integer
# recommended values: 100 - 500 (lower values improves responsiveness but can incorrectly register button presses)
# default value: 250
