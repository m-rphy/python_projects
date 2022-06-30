#!/bin/sh



# Author : WIlliam Murphy
# Date   : 03May22

# This shell script makes a request to physics 129L course web pages and 
# returns when the latest update occured on the anoucemnets page.

# This shell script implements the commands - 'wget', 'grep', 'sed'


wget -O- web.physics.ucsb.edu/~phys129/lipman/ | grep -h "Latest update" | sed -e 's/<span class="greenss">//' -e 's/&nbsp;/ /' -e 's/<\/span><\/p>//'


