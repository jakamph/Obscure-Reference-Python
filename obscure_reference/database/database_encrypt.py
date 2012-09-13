##This module contains the class definition for encrypting and decrypting
# data to go to the database.
#
# Author: Jason Kamphaugh
#
# Date: Sep 12, 2012

import copy
import bz2

class Database_Encrypt:
   """This class allows access to functions to encrypt and decrypt strings
   based on a provided salt."""
   
   def __init__( self ):
      """The constructor of the object."""

      #nothing to see here. move along
      None

   #__init__
   
   def Encrypt( self,
                string_to_encrypt,
                salt ):
      """This method will take the string provided, combine it with the salt
      and return the encrypted string to the user."""
      
      # Parameters
      #
      #  self: The Database_Encrypt instance
      #
      #  string_to_encrypt: The string that the user wants to be encrypted.
      #
      #  salt: The salting to add to the encryption
      #
      # Return:
      #  A string that has been encrypted using the string_to_encrypt and
      #  the salt.
      #
      
      salt_string = copy.copy( salt )
      
      #if we've not been given a string to use in our salting
      if type( salt_string ) != str:
         #convert it to a string for our use
         salt_string = `salt_string`      
      #end if salt_string isn't a string 
      
      #compress the string using the salting
      return bz2.compress( salt_string + \
                           string_to_encrypt + \
                           salt_string )
      
   #end Encrypt
   
   def Decrypt( self,
                string_to_decrypt,
                salt ):
      """This method will take the string provided, combine it with the salt
      and return the encrypted string to the user."""

      # Parameters
      #
      #  self: The Database_Encrypt instance
      #
      #  string_to_decrypt: The string that the user wants to be decrypted.
      #
      #  salt: The salting to remove from the decryption
      #
      # Return:
      #  A string that has been decrypted using the string_to_decrypt and
      #  removing the salt.
      #
      
      salt_string = copy.copy( salt )
      
      if type( salt_string ) <> str:
         salt_string = `salt_string`
      #end if salt string wasn't a string
      
      #decrypt the string
      decrypted_string = bz2.decompress( string_to_decrypt )

      #remove the salt from the beginning and the end
      decrypted_string = \
         decrypted_string.lstrip( salt_string ).rstrip( salt_string )
      
   #end Decrypt
   
#end Database_Encrypt