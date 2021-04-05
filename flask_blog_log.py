# delete site.db

# models.py, class Post, ln 6, 42
tags = db.Column(db.String(201))

# run.py
from flaskblog import create_app, db
from flask_ngrok import run_with_ngrok
from flaskblog import db, login_manager

app = create_app()
run_with_ngrok(app)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run()

# posts/routes.py, function new_post, ln 4, 16 
# delete prev line
post = Post(title=form.title.data, content=form.content.data, author=current_user, tags=form.tags.data)

# posts/forms.py, class PostForm, ln 4, 8
tags = TextAreaField('Tags', validators=[DataRequired()])

# templates/create_post.html, ln 33
'''
            <div class="form-group">
                {{ form.tags.label(class="form-control-label") }}
                {% if form.tags.errors %}
                    {{ form.tags(class="form-control form-control-lg is-invalid") }}
                    <div class="invalid-feedback">
                        {% for error in form.tags.errors %}
                            <span>{{ error }}</span>
                        {% endfor %}
                    </div>
                {% else %}
                    {{ form.tags(class="form-control form-control-lg") }}
                {% endif %}
            </div>
'''

# templates/post.html, ln 17
'''
      <p class="article-tags">{{ post.tags }}</p>
'''

# posts/routes.py, function update_post, ln 9, 40
post.tags = form.content.data

# posts/routes.py, new function tag_find, ln 50
@posts.route("/tagfind/<string:tag>")
def tag_find(tag):
    page = request.args.get('page', 1, type=int)
    search = "%{}%".format(tag)
    posts = Post.query.filter(\
    Post.tags.like(search)).all()
    total_posts = len(posts)
    return render_template('tag_posts.html', posts=posts, tag=tag, lenpost=total_posts)

# posts/routes.py, new function search, ln 69
@posts.route("/search")
def search():
    query = request.args.get('q', 1, type=str)
    search = "%{}%".format(query)
    posts = Post.query.filter(Post.title.like(search) | Post.content.like(search)).all()
    total_posts = len(posts)
    return render_template('tag_posts.html', posts=posts, tag=query, lenpost=total_posts)

# new file templates/tag_posts.html, ln 0
'''
{% extends "layout.html" %}
{% block content %}
    <h1 class="mb-3">{{ tag }} Found In {{ lenpost }} Post(s)</h1>
    {% for post in posts %}
        <article class="media content-section">
          <img class="rounded-circle article-img" src="{{ url_for('static', filename='profile_pics/' + post.author.image_file) }}">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="{{ url_for('users.user_posts', username=post.author.username) }}">{{ post.author.username }}</a>
              <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d') }}</small>
            </div>
            <h2><a class="article-title" href="{{ url_for('posts.post', post_id=post.id) }}">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}
{% endblock content %}
'''

# templates/layout.html, ln 47, delete col-md-4
'''
        <div class="col-md-4">
          <div class="content-section">
            <h3>Our Sidebar</h3>
            <div class="search">
                <form action="/search">
                    <div class="form-group">
                        <input class="form-control form-control-lg" id="searchQ" name="q" type="text" value="" placeholder="Search...">
                        <br>
                        <div class="dropdown">
                          <button class="btn btn-outline-info dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Search Type
                          </button>
                          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <a class="dropdown-item" href="#">Posts</a>
                            <a class="dropdown-item" href="#">Tags</a>
                            <a class="dropdown-item" href="#">User</a>
                          </div>
                        </div>
                        <br>
                        <input class="btn btn-outline-info" id="search" type="submit" value="Search">
                    </div>
                </form>
            </div>

            <p class="text-muted">You can put any information here you'd like.
              </p><ul class="list-group">
                <li class="list-group-item list-group-item-light">Latest Posts</li>
                <li class="list-group-item list-group-item-light">Popular tags: </li>
                <li class="list-group-item list-group-item-light">Account</li>
                <li class="list-group-item list-group-item-light">Courses</li>
              </ul>
            <p></p>
          </div>
        </div>
'''
