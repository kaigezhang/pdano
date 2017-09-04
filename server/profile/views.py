# coding: utf-8

from flask import Blueprint
from flask_apispec import marshal_with
from flask_jwt import current_identity, jwt_required
from server.user.models import User
from server.utils import jwt_optional

from server.exceptions import InvalidUsage
from .serializers import profile_schema

blueprint = Blueprint('profiles', __name__)


@blueprint.route('/api/profiles/<username>', methods=('GET',))
@jwt_optional()
@marshal_with(profile_schema)
def get_profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise InvalidUsage.user_not_found()
    return user.profile


@blueprint.route('/api/profiles/<username>/follow', methods=('POST',))
@jwt_required()
@marshal_with(profile_schema)
def follow_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise InvalidUsage.user_not_found()
    current_identity.profile.follow(user.profile)
    current_identity.profile.save()
    return user.profile


@blueprint.route('/api/profiles/<username>/follow', methods=('DELETE',))
@jwt_required()
@marshal_with(profile_schema)
def unfollow_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise InvalidUsage.user_not_found()
    current_identity.profile.unfollow(user.profile)
    current_identity.profile.save()
    return user.profile
