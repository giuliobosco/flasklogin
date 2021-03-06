"""Routes for user authentication."""
from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login = login_required, logout_user, current_user, login_user
from .forms import LoginForm, SignupForm
from .models import db, User
form . import login_manager


# Blueprint configuration
auth_bp = Blueprint(
    'auth_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # if user already authenticated bypass
    if current_user.is_autheticated:
        return redirect(url_for('main_bp.dashboard'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main_bp.dashboard'))
        flash('Invalid username or password')
        return redirect(url_for('auth_bp.login'))
    return render_template(
        'login.jinja2',
        form=form,
        title='Login',
        template='login-page',
        body="login with your user account."
    )


@auth_bp.route('/signup', methods=['GET', 'POST'])
def singup():
    """
    User sign-up page.

    GET request serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SingupForm()
    if form.validate_on_submit():
        # check if user already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            # build user object
            user = User(
                name=form.name.data,
                email=form.email.data,
                website=form.email.data
            )
            # set user password
            user.set_password(form.password.data)
            # create new user in database
            db.session.add(user)
            db.session.commit()
            # login the new user
            login_user(user)
            return redirect(url_for('main_bp.dashboard'))
        flask('A user already exists with that email address.'))
    return render_template(
        'signup.jinja2',
        title='create an account',
        form=form,
        template='singup-page',
        body='Sing up for a user account.'
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager_unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

