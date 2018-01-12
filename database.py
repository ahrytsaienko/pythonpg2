import psycopg2
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user='postgres',
                                            password='postgres',
                                            database='learning',
                                            host='localhost')
