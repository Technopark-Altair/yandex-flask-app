from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data import db_session
from data.users import User


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'about', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('about')
        self.parser.add_argument('email', required=True, type=str)
        self.parser.add_argument('password', required=True, type=str)
        self.parser.add_argument('password_again', required=True, type=str)

    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('id', 'name', 'about', 'email')) for item in user]})

    def post(self):
        args = self.parser.parse_args()
        if args.get('password') != args.get('password_again'):
            return abort(400, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == args.get('email')).first():
            return abort(400, message="Такой пользователь уже есть")
        user = User(
            name=args['name'],
            about=args['about'],
            email=args['email']
        )
        user.set_password(args.get('password'))
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})