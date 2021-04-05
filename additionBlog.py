# delete site.db

# models.py, class Post, ln 6
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

# posts/routes.py, function new_post, ln 4
post = Post(title=form.title.data, content=form.content.data, author=current_user, tags=form.tags.data)

# posts/forms.py, class PostForm, ln 4
tags = TextAreaField('Tags', validators=[DataRequired()])

# templates/create_post.html, ln 34
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

# templates/post.html, ln 18
'''
      <p class="article-tags">{{ post.tags }}</p>
'''

# posts/routes.py, function update_post, ln 9
post.tags = form.content.data

# posts/routes.py, function tag_find, ln 80
@posts.route("/tagfind/<string:tag>")
def tag_find(tag):
    page = request.args.get('page', 1, type=int)
    search = "%{}%".format(tag)
    posts = Post.query.filter(\
    Post.tags.like(search)).all()
    total_posts = len(posts)
    return render_template('tag_posts.html', posts=posts, tag=tag, lenpost=total_posts)

# new_file=templates/tag_posts.html, ln 0
'''
{% extends "layout.html" %}
{% block content %}
    <h1 class="mb-3">{{ tag }} Found In {{ lenpost }} Posts</h1>
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
