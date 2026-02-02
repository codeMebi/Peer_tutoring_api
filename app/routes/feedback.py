from flask import Blueprint, request, jsonify
from ..models import Feedback
from ..database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

feedback_bp = Blueprint("feedback", __name__)

# Submit feedback
@feedback_bp.route("/submit", methods=["POST"])
@jwt_required()
def submit_feedback():
    data = request.get_json()
    feedback = Feedback(
        from_user_id=get_jwt_identity(),
        to_user_id=data["to_user_id"],
        session_id=data.get("session_id"),
        rating=data["rating"],
        comment=data.get("comment")
    )
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback submitted"})
