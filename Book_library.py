# A library management module
# Developed by Simsarul haq vengasseri


# A class BookManager

class BooksManager(object):

		
	# constructor
	def __init__(self):

		# Book list is initialized with an empty library
		self.book_list = []

		#Following examples explains, how to add books to the library
		#adding two books in the form of a dictionary
		
		#self.book_list.append(
			#{
			#	"title": "ALC Title",
			#	"auther": "sar",
			#	"copies" : 5,
			#}
		#)
		#self.book_list.append(
			#{
			#	"title": "CAO Title",
			#	"auther": "sim",
			#	"copies" : 0,
			#}
		#) 
	
	# This method returns a list of all books	
	def get_all_books(self):
		return self.book_list

	# This method used to add books to the book library
	def add_book(self, title, auther, count):
		#code to add book
		self.book_list.append(
			{
				"title": title,
				"auther": auther,
				"copies" : count,
			}
		)

	# This method prints the details of the available books
	def print_available_books(self):
		for item in self.book_list:
			if item["copies"] > 0:
				print item

	# This method retruns all available books in book library
	def get_available_books(self):
		return [item for item in self.book_list if item["copies"] > 0]

	# This method removes a given count of a given book from book library
	def delete_book(self,title,auther,delete_count):
		for item in self.book_list:
			if item["title"] == title and item["auther"] == auther:
				if item["copies"] > 0 and item["copies"] >= delete_count:
					item["copies"] = item["copies"] - delete_count
				elif item["copies"] > 0 and item["copies"] < delete_count:
					print "Only " + "%d"%(item["copies"]) + " can be deleted." + "Deleting all available books"
					item["copies"] = 0;

				else:
					print "No books available" 
			else:
				print "Requested book not available in library"

	# This method returns the total count of all avaialable books
	def total_count(self):
		self.total=0
		for item in self.book_list:
			self.total = self.total + item["copies"]
		return self.total

	
	# Check if a requested book is available in the book library 
	def is_available(self,title,auther):
		for item in self.book_list:
			if item["title"] == title and item["auther"] == auther:
				if item["copies"] > 0:
					return "Yes"
		return "No"
					 	
