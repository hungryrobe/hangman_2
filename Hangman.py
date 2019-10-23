import os

myWord = 'griffin'

misses = 0
myWord = list(myWord)

Hman = ['''

 +---+
   	 |
	 |
	 |
	  
	  ''','''

 +---+
 0	 |
 	 |
 	 |

 	  ''','''

 +---+
 0	 |
 |	 |
	 |
      
      ''','''

 +---+
 0	 |
 |	 |
/	 |

 	  ''','''

 +---+
 0	 |
 |	 |
/ \\ |

	  ''','''

 +---+
 0	 |
 |\\ |
/ \\ |

 	  ''','''

 +---+
 0	 |
/|\\ |
/ \\ |

 	  '''
]




while misses > 7:
	pGuess = input('Guess a letter: ')
	print(Hman[misses])
	if pGuess in myword:
		print('Yep')
		myWord.append(pGuess)
	else:
		misses = misses + 1



