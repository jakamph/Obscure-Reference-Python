##
# This file contains the information for an individual player
#
# Author: Jason Kamphaugh
#
# Date: March 1, 2012
#

import obscure_reference.common.string_definitions as string_definitions

class Player:

    def __init__( self,
                  raw_data ):
        """This is the constructor for the Player object."""
        #pull the data out and store it locally
        self._raw_data = raw_data
    #end __init__

    def Get_Raw_Data( self ):
        """This method will retrieve the raw data that was used to
        initialize this player object."""

        return self._raw_data

    #end Get_Raw_Data

#end class Player