import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Exploring  Chef Habitat!', 'Chef Habitat is a patented automation tool that enables companies to apply a consistent approach to application definition, packaging and delivery across all applications and environments')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Docker Vs Chef Habitat', 'Docker is used for quickly provisioning new servers, and Chef is used for rolling out the small, detailed changes to existing machines, a task for which Docker may be ill-suited')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('ChefConf 21 - Chef DevOps Conference', 'An opportunity to learn about infrastructure management, continuous delivery, and compliance automation from the leading DevOps people in the industry')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Automate for Good Hackathon', 'This hackathon invites you to showcase the power of DevOps to the world, and make the world a better place while doing it')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Chef Infrastructure Management', 'Chef Infrastructure Management enables DevOps teams to model and deploy secure and scalable infrastructure automation across any cloud, VM, or physical infrastructure.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Chef Automate', 'Chef Automate is an enterprise platform that allows developers, operations and security engineers to collaborate effortlessly on delivering application & infrastructure changes at the speed of business.')
            )

connection.commit()
connection.close()
