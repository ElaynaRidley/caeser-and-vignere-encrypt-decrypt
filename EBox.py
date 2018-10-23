class EBox:
	'''This class encrypts and decrypts messages using a password.
	Users can specify if they want to encrypt or with Vignere of Caeser algorithms.
	If they choose Vignere, they can choose to work at level 0 (simpler) or level 1 (more complex).'''

	ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	def __init__(self):
		'''__init__ has the following variables.
		mode determines encryption or decryption.
		level can be 0 or 1.
		pos is the position
		password is the word used for encryption/decryption.
		numChars is the number of characters encrypted/decrypted.
		offset is the amount of offset used.
		debug is if debug mode is on or off.
		algo is the algorith: caeser or vignere.
		'''
		self.mode = "encrypt"
		self.level = 0
		self.pos = 0
		self.password =  ""
		self.numChars = 0
		self.offset = 0
		self._debug = False
		self.algo = "Vignere"


	def set_password(self, password):
		'''The password the user enters is set here. This returns that password'''
		self.password = password
		return self.password

	def reset(self, mode, level):
		'''This sets the mode, and level to the user's choice.
		It also resets pos and numChars to 0.'''

		self.numChars = 0
		self.pos = 0
		self.mode = mode
		self.level = level

	def restart(self):
		'''This sets the mode and level to the user's choice.
		It also resets pos and numChars to 0'''

		self.numChars = 0
		self.pos = 0
		self.mode = "encrypt"
		self.level = 0
		

	def algorithm(self, algo):
		'''This sets the self.algo to caeser or vignere'''
		self.algo = algo

	def encrypt(self, line):
		'''If the user chose Vignere and level 0
		this calls _chyptChar and adds the characters from there into a string and sets the pos to 0 once it's the same length as the password.
		If they chose Vignere and level 1
		this calls _cryptChar and adds the characters from there into a string and pos is set to += 1 once it reaches the length of the password.
		If the users chose Caesar
		this users the first letter of the password as the pw.
		It adds index of pw to one character at a time from the message and puts them into a string.
		This outputs an encrytped message
		'''
		clean = EBox._clean_line(line)
		self.pos = 0
		upassword = EBox.set_password(self, self.password).upper()
		if self.algo == "Vignere":
			crypted = ""
			for ch in clean:
				if self.pos == len(upassword):
					self.pos = 0
				crypted += EBox.ALPHABET[EBox._cryptChar(self, ch)]
				if self.level == 0:
					self.pos += 1
				if self.level == 1:
					self.pos += 1
				self.numChars += 1
			return crypted
		elif self.algo == "Caesar":
			pw = EBox.ALPHABET.find(upassword[0])
			encrypted = ""
			for ch in clean:
				encrypted += EBox.ALPHABET[(pw + EBox.ALPHABET.find(ch)) % len(EBox.ALPHABET)]
			return encrypted


	def _cryptChar(self, ch):
		'''If the mode is decrypt
		It loops through the password for the length of the message
		and subtracts the index of one character from one index of the password.
		If the mode is encrypt
		it loops through the password for the number of characters in the message
		and adds the index of one character and one index of the password
		This returns one encrypted or decrypted character at a time'''

		if self.mode == "decrypt":
			upassword = self.password.upper()
			chind = EBox.ALPHABET.find(ch)
			done = (chind - EBox.ALPHABET.find(upassword[self.pos])) % len(EBox.ALPHABET)
		else:
			upassword = self.password.upper()
			chind = EBox.ALPHABET.find(ch)
			done = (EBox.ALPHABET.find(upassword[self.pos]) + chind) % len(EBox.ALPHABET)
		
		return done


	def decrypt(self, line):
		'''If the user chose Vignere and level 0
		this calls _chyptChar and adds the characters from there into a string and sets the pos to 0 once it's the same length as the password.
		If they chose Vignere and level 1
		this calls _cryptChar and adds the characters from there into a string and pos is set to += 1 once it reaches the length of the password.
		If the users chose Caesar
		this users the first letter of the password as the pw.
		It subtracts index of pw from one character at a time of the message and puts them into a string.
		This outputs a decrytped message
		'''
		clean = EBox._clean_line(line)
		self.pos = 0
		upassword = EBox.set_password(self, self.password).upper()
		if self.algo == "Vignere":
			crypted = ''
			for ch in clean:
				if self.pos == len(upassword):
					self.pos = 0
				crypted += EBox.ALPHABET[EBox._cryptChar(self, ch)]
				if self.level == 0:
					self.pos += 1
				if self.level == 1:
					self.pos +=1
				self.numChars += 1
			return crypted
		elif self.algo == "Caesar":
			pw = EBox.ALPHABET.find(upassword[0])
			decrypted = ""
			for ch in clean:
				decrypted += EBox.ALPHABET[(EBox.ALPHABET.find(ch) - pw) % len(EBox.ALPHABET)]
			return decrypted                

	def get_status(self):
		'''This returns the current status.
		It returns the current mode, level, password, position, and number of characters.'''
		return (self.mode, self.level, len(self.password), self.pos, self.numChars)

	def _clean_line(line):
		'''This uppercases the message
		and removes any character from it that isn't in ALPHABET'''
		clean = ""
		line = line.upper()
		for ch in line:
			if ch in EBox.ALPHABET:
				clean += ch
		return clean




