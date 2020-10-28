# Decrypt any Caeser cipher
Caeser cipher is an encryption technique, whereby the sender shifts each character a certain number of spaces in the alphabet. For example, a Caeser cipher shift of 3 positions applied to the word "hello" returns "khoor". This is easy to decrypt if the receiver knows the number of positions each character has been shifted. In this module, I define a function that can decrypt a message without knowing how many positions each character has been shifted. This is achieved by trial and error, and checking each shift for if the decoded words are common English words. For a message of more than a few words, there is likely to be at least a few common English words, which allows the function to recognise if the message has been successfully decoded. 

The decryption function in the Python module is `decipher_by_word_length(encrypted_message: str)`


**Note:** For very short messages, there may not be any common English words, which reduces the ability of this module to decode the message. To improve this, you could add a large word bank file, which contains more words. The current file has 1000 English words. Additionaly, you could make it work for another language by substituting the words file for a file containing common words in the desired language.
