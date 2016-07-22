database = 'database.txt';

def searchDatabase(query):
	print('Looking for ' + query  + ' in ' + database);
	file = open(database, 'r');
	result = 'Sorry, ' + query + ' was not found in our database!';
	for line in file:
		if '~' + query in line.lower():
			result = line;
			break;
	file.close();
	return result;


def addToDictionary(word):
	if (checkDatabase(word)):
		print('Sorry, that word appears to already have a definition!');
		print(searchDatabase(word));
		return;
	print('What is the definition for ' + word + '?');
	userInput = input();
	entry = '~' + word + ' ' + userInput;
	print('Ok, ' + entry);
	file = open('database.txt', 'a');
	file.write(entry + '\n');

def checkDatabase(query):
	print('Looking for ' + query  + ' in ' + database);
	file = open(database, 'r');
	for line in file:
		if '~' + query in line.lower():
			file.close();
			return 1;
	file.close();
	return 0;

def printLogo():
	file = open('logo.txt', 'r');
	logo = '';
	for line in file:
		logo = logo + line;
	print(logo);
	file.close();

print('Welcome to Kyle Sandstrom\'s dictionary program!');
printLogo();
print('Please type a query or type \'~\' before a word to add it to the dictionary.');
userInput = input();
if (userInput[0] == '~'):
	word = userInput[1:];
	addToDictionary(word);
else:
	result = searchDatabase(userInput);
	print(result);
