##
# This file contains the class for containing information about a single
# transaction.
#
# Author: Jason Kamphaugh
#
# Date: September 24, 2012
#

class Transaction:

   #.......................................................................   
   def __init__( self,
                 offering_manager,
                 offered_players,
                 dropped_players,
                 receiving_manager,
                 requested_players,
                 transaction_id,
                 raw_data = None ):
      """This method is the constructor for the new object."""
      
      #save off the data
      self._offering_manager = offering_manager
      self._offered_players = offered_players
      self._dropped_players = dropped_players
      self._receiving_manager = receiving_manager
      self._requested_players = requested_players
      self._transaction_id = transaction_id
      self._raw_data = raw_data 

   #end __init__

   #.......................................................................
   def Get_Offering_Manager( self ):
      """This method will retrieve the offering manager that was provided at
      initialization."""
      
      return self._offering_manager

   #end Get_Offering_Manager


   #.......................................................................
   def Get_Offered_Players( self ):
      """This method will retrieve the offered players that was provided at
      initialization."""
      
      return self._offered_players

   #end Get_Offered_Players


   #.......................................................................
   def Get_Dropped_Players( self ):
      """This method will retrieve the dropped players that was provided at
      initialization."""
      
      return self._dropped_players

   #end Get_Dropped_Players


   #.......................................................................
   def Get_Receiving_Manager( self ):
      """This method will retrieve the receiving manager that was provided at
      initialization."""
      
      return self._receiving_manager

   #end Get_Receiving_Manager


   #.......................................................................
   def Get_Requested_Players( self ):
      """This method will retrieve the requested players that was provided at
      initialization."""
      
      return self._requested_players

   #end Get_Requested_Players


   #.......................................................................
   def Get_Transaction_Id( self ):
      """This method will retrieve the transaction ID that was provided at
      initialization."""
      
      return self._transaction_id

   #end Get_Transaction_Id


   #.......................................................................
   def Get_Raw_Data( self ):
      """This method will retrieve the raw data that was provided at
      initialization."""
      
      return self._raw_data

   #end Get_Raw_Data

#end Transaction