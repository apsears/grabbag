import sqlite3

def test_fail():
	assert 1==2

def test_success():
	assert 1==1

def test_connection():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('CREATE TABLE test(id int);')
	c.commit()
	c.close()
	assert 1==1
