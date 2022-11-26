import sqlite3 as sql

def db_start():
    global base, cur
    base = sql.connect('ITclub.db')
    cur = base.cursor()
    cur.execute("select * from SKILLS")
    base.commit()
    skills_dict = {}
    for i in cur.fetchall():
        skills_dict[i[1]] = i[0]
    return skills_dict

def check_user(id):
    cur.execute("SELECT EXISTS(select * from USER where id=?)", (id,))
    return bool(cur.fetchone()[0])

def push_user(id, name, des, tg, has_team, skills, SKILLS):
    # skills = ['C++', 'Java']
    global cur, base
    user = (id, name, des, tg, int(has_team))
    cur.execute("INSERT INTO USER VALUES(?, ?, ?, ?, ?);", user)
    for i in skills:
        user_skill = (id, SKILLS[i])
        cur.execute("INSERT INTO user_skill VALUES(?, ?);", user_skill)
    base.commit()

SKILLS = db_start()
push_user(12643, "Vlad", "cool gay", "@Vladik", True, ['C++', 'Kotlin', 'PHP'], SKILLS)