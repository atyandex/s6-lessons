import vertica_python

conn_info = {'host': 'vertica.tgcloudenv.ru', 
             'port': '5433',
             'user': 'stv2024050741',       
             'password': 'iwbpVXz59UhI5F9',
             'database': 'dwh',
             # Вначале он нам понадобится, а дальше — решите позже сами
            'autocommit': True
}


N = 10000
batch = 5

with vertica_python.connect(**conn_info) as conn:
    curs = conn.cursor()
    insert_stmt = 'INSERT INTO BAD_IDEA VALUES ({},\'a\');'
    
    for i in range(0, N, batch):
        # будем отправлять сразу по несколько команд
        curs.execute(
            '\n'.join(
                [insert_stmt.format(i + j) for j in range(batch)])
        )
        
    curs.commit()
            