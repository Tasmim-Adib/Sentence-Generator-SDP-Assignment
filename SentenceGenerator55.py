from abc import ABC, abstractmethod
import random

class Operation():

	word = ""
	vocabulary = []
	sentence = ""

	@abstractmethod
	def addToVocabulary(self,word):
		pass
	
	@abstractmethod
	def generateSentence(self):
		pass

class RSG(Operation):
	def addToVocabulary(self, word):
		self.word = word.lower()
		txt_file = open("RSG.txt","a")  
		txt_file.write(self.word + "\n") 	#add the word in a file 
		txt_file.close()

	def generateSentence(self):
		txt_file = open("RSG.txt","r")
		for line in txt_file:
			self.vocabulary.append(line.strip("\n")) 	#take every word and add in array
		word_size = len(self.vocabulary)		#size of the array
			
		cnt = random.randint(0, word_size)  #how many random integer will be generated
		
		for i in range(0,cnt):
			x = random.randint(0, word_size-1)  #generate random integer and access the word
			self.sentence += self.vocabulary[x]
			self.sentence += " "
		print("Your Random Sentence is : " + self.sentence)
		print("-------Thank you-------")

class SSG(Operation):

	def addToVocabulary(self,word):
		self.word = word.lower()
		txt_file = open("SSG.txt","a")  
		txt_file.write(self.word + "\n") 	#add the word in a file 
		txt_file.close()

	def generateSentence(self):
		txt_file = open("SSG.txt","r")
		for line in txt_file:
			self.vocabulary.append(line.strip("\n")) 	#take every word and add in array
		word_size = len(self.vocabulary)		#size of the array
			
		cnt = random.randint(0, word_size)  #how many random integer will be generated
		
		for i in range(0,cnt):
			x = random.randint(0, word_size-1)  #generate random integer and access the word
			self.sentence += self.vocabulary[x]
			self.sentence += " "
		words = self.sentence.split(" ")
		words.sort()
		newSentence = " ".join(words)
		print("Your Random Sentence is : " + newSentence)
		print("-------Thank you-------")


class OSG(Operation):
	def addToVocabulary(self, word):
		self.word = word
		self.sentence += self.word
		self.sentence += " "
		self.word = word.upper()[::-1]
		txt_file = open("OSG.txt","a")  
		txt_file.write(self.word + "\n") 	#add the word in a file 
		txt_file.close()

	def generateSentence(self):
		print("Your Sentence is : " + self.sentence)
		print("-------Thank you-------")
		


class Context():
	operation : Operation

	def __init__(self, operation):
		self.operation = operation

	def executeInsertion(self, word):
		self.operation.addToVocabulary(word)

	def executeGenerator(self):
		self.operation.generateSentence()



run = True
print("-------Choose any Process-------")
print("1. Random Sentence Generator - RSG")
print("2. Sorted Sentence Generator - SSG")
print("3. Ordered Sentence Generator - OSG")
print("4. Exit")

choice = int(input("Enter choice : "))
rsgGenerator = Context(RSG())
osgGenerator = Context(OSG())
ssgGenerator = Context(SSG())
if(choice == 1):
	while(run):
		print("-----You have choosed RSG-----")
		print("1. Give new Word")
		print("2. Generate Sentence")
		print("3. Exit")

		nextChoice = int(input("Enter your choice : "))

		if(nextChoice == 1):
			newWord = input("Give a word : ")
			print("Thanks for your contribution.")
			rsgGenerator.executeInsertion(newWord)
			run = True

		elif(nextChoice == 2):
			rsgGenerator.executeGenerator()
			run = False

		elif(nextChoice == 3):
			print("Thank you")
			run = False

		else:
			print("Sorry please enter valid number !!")
			run = True

elif(choice == 2):
	while(run):
		print("-----You have choosed SSG-----")
		print("1. Give new Word")
		print("2. Generate Sentence")
		print("3. Exit")

		nextChoice = int(input("Enter your choice : "))

		if(nextChoice == 1):
			newWord = input("Give a word : ")
			print("Thanks for your contribution.")
			
			ssgGenerator.executeInsertion(newWord)
			run = True

		elif(nextChoice == 2):
			ssgGenerator.executeGenerator()
			run = False

		elif(nextChoice == 3):
			print("Thank you")
			run = False

		else:
			print("Sorry please enter valid number !!")
			run = True

elif(choice == 3):
	while(run):
		print("-----You have choosed OSG-----")
		print("1. Give new Word")
		print("2. Generate Sentence")
		print("3. Exit")

		nextChoice = int(input("Enter your choice : "))

		if(nextChoice == 1):
			newWord = input("Give a word : ")
			print("Thanks for your contribution.")
			osgGenerator.executeInsertion(newWord)
			run = True

		elif(nextChoice == 2):
			osgGenerator.executeGenerator()
			run = False

		elif(nextChoice == 3):
			print("Thank you")
			run = False

		else:
			print("Sorry please enter valid number !!")
			run = True

elif(choice == 4):
	print("Program terminated. Thank you !!!")

else:
	print("Wrong Selection. Please Insert a valid Choice. Thank you !!!")