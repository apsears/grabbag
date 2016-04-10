import sqlite3


def test_success():
	assert 1==1

def test_connection():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('DROP TABLE IF EXISTS test;')
	c.execute('CREATE TABLE test(id int);')
	conn.commit()
	c.close()
	assert 1==1
