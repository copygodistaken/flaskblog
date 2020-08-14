import secrets
import os
from PIL import Image
from flask import url_for, current_app
from flaskblog import mail
from flask_mail import Message


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # unused variable is defined with an '_'
    # this keeps editors from freaking out that the '_' variable wasn't used.
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # give the full path from root ('/') to where the file needs to
    # be stored, including our new filename.
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    # resize image to 125x125
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # save resized image (i)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, then simply ignore this email and no changes will be made.
'''
# uncomment to allow sending of emails, must update email strings located in __init__.py first!
#    mail.send(msg)
