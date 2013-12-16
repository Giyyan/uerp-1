# -*- encoding: utf-8 -*-
import base64
import os
import psycopg2
import pytils

directory = '/home/andrey/projects/uerp/uerp/media/avatar'
conn_string = "host='217.12.219.143' dbname='zombieland' user='wichita' password='vjq1gfhjkm'"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print(os.path.exists(directory))
print(os.path.isdir(directory))
print(directory)


def create_file(employee_id, employee_name, photo):
    name = pytils.translit.slugify(employee_name)
    filename = "%s/%s" % (directory, name)
    open(filename, 'wb').write(base64.b64decode(bytes(photo)))
    cursor.execute("UPDATE hr_employee SET avatar=%s WHERE id=%s", (filename, employee_id))
    conn.commit()
    return True


# cursor.execute("SELECT e.id, r.name, e.photo FROM hr_employee e LEFT JOIN resource_resource r on (r.id=e.resource_id) WHERE e.photo IS NOT NULL;")
# for record in cursor.fetchall():
#     create_file(*record)

cursor.execute("SELECT e.id, r.name FROM hr_employee e LEFT JOIN resource_resource r on (r.id=e.resource_id) WHERE e.photo IS NOT NULL;")
for record in cursor.fetchall():
    name = pytils.translit.slugify(record[1])
    file = "avatar/%s" % name
    print(record[0], record[1], name, file, os.path.exists(file))
    cursor.execute("UPDATE hr_employee SET avatar=%s WHERE id=%s", (file, record[0]))
    conn.commit()


cursor.close()
conn.close()
