#!/usr/bin/env python3
# A buggy web service in need of a database.
import psycopg2
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <!-- post content will go here -->
    %s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''
br = "<br>"


# here we use our query and we use join here to be able to print it
@app.route('/', methods=['GET'])
# this function has our three queries
def main():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("SELECT * FROM m_articles ORDER BY koko DESC LIMIT 3;")
    art = c.fetchall()

    answers = "".join(POST % (title, koko) for title, koko in art)
    answers += br
    answers += br
    answers += br
    c.execute("SELECT * FROM m_authors ORDER BY koko DESC ;")
    aut = c.fetchall()
    answers += "".join(POST % (name, koko) for name, koko in aut)
    answers += br
    answers += br
    answers += br

    c.execute(
        "SELECT date , cast(errors as decimal)"
        "/cast(total_requests as decimal) *"
        " 100 as per FROM dates_errors  ORDER BY per DESC LIMIT 1 ;")
    er = c.fetchall()
    answers += "".join(POST % (date, per) for date, per in er)
    db.close()
    h = HTML_WRAP % answers
    return h


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
