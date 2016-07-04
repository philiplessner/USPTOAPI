import sys
import ui
import console
import clipboard


@ui.in_background
def httperror_dialog(e):
    error = e.args[0]
    button = console.alert('HTTP Error\n', error, 'Copy to Clipboard')
    if button == 1:
        clipboard.set(error)
        

@ui.in_background
def novaluesreturned_dialog(payload):
    button = console.alert('No Values Were Returned For Query\n', 
                           payload, 
                           'Copy to Clipboard')
    if button == 1:
        clipboard.set(payload)
        

@ui.in_background
def noqueryfields_dialog():
    button = console.alert('Query Must Have At Least One Field', 
                           '', 
                           'OK',
                           hide_cancel_button=True)
    sys.exit(1)
