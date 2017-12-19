# rpitx_ook
Generates OOK *.ft files for rpitx using amplitude shift keying.

A while ago I was trying to send an OOK key over 315MHz using F5OEO's RPITX software (https://github.com/F5OEO/rpitx), but the construction of FT files proved difficult. This file can be used to generate the appropriate FT files if you feed it the appropriate timing (in uS) for the long and short pulses and their respective 'low'-times, transmission gap length and number of repetitions.  
