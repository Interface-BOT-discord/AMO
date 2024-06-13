import sqlite3 as sq


def add_morph(data: dict):
    with sq.connect('data.db') as conn:
        conn.cursor().execute(
            f'''
            INSERT INTO morphs (id, morph, people, inspector, structure, status)
            VALUES ('{data['id']}', '{data['morph']}', '{data['people']}', '{data['inspector']}', '{data['structure']}',
             '{data['status']}')
            '''
        )


"""
DON'T TOUCH

data = {
    'id': 'dev',
    'morph': '/:morph me none\n/:ntag me DEVELOPER\n',
    'people': '1017341027654324234',
    'inspector': '1017341027654324234',
    'structure': 'developers',
    'status': 'active'
}
"""
