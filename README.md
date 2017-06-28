# inter-base-calculator

A calculator capable of taking input and displaying output in different number bases, with access to all of Python3's numerical operators. Written in Python, with a Tkinter GUI.

## Getting Started

This project consists of a single module.
* `Inter-baseCalculator.py` - The collection of methods to convert between number bases, and a GUI to easily access them.

### Prerequisites

To run inter-base-calculator, the host machine must have the following installed:
* `Python3` - The programming language in which inter-base-calculator was written. Available [here](https://www.python.org/).
* `Tkinter` - The Python library required for the inter-base-calculator user interface.\*

\*Included with the standard Python3 installation on Windows and MacOS, requires separate installation on Linux. For Debian-based systems, this is achieved through the following command:
`apt-get install python3-tk`

### Running

The tool may be started by running the script as follows:
`python3 Inter-baseCalculator.py` 

### Use

Before entering an expression in either text box, select the number base for each from the corresponding drop-down box and tick (or un-tick) either checkbox for auto-update.

The input expression will be evaluated in the base chosen for that text box. The result is then converted into the base of the other text box and displayed accordingly (if auto-update is enabled for that box). Manual text box updates may be triggered by clicking the "Update" button for the corresponding text box.

Note: the symbols used for every base are defined by the string `ALPHANUMCHARS`. By default, this uses 0-9 then A-Z and finally a-z. If higher bases are required, symbols may be added to this string.


### Example

With the left drop-down box set to `Base 2`, right to `Base 16`, and auto-update enabled for both text boxes, entering  
`1010 << 10`  
in the left text box yields  
`28`  
in the right. Changing this to  
`28 + 2`  
alters the left text box contents to  
`101010`  
changing the left's base to `Base 10` shows the value  
`42`  
on the left as expected.

## Authors

* **Marc Katzef** - [mkatzef](https://github.com/mkatzef)
