import web

db_host = 'er7lx9km02rjyf3n.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'hcm0uiqmrof3g1pg'
db_user = 'gmjfll6hcslk4rmp'
db_pw = 'ezmstkegey308k99'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )