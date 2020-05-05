import unittest
from app import index

def test_index():
	assert index() == "This is a template"

if __name__ =="__main__":
	test_index()
	print("Everything passed")	
