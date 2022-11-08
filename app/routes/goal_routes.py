from flask import Blueprint,request,jsonify,abort, make_response
import requests, json
from app import db
from app.models.task import Task
from app.models.goal import Goal
from sqlalchemy import asc
from sqlalchemy import desc
from datetime import date

goal_bp = Blueprint("goal_bp", __name__, url_prefix ="/goals")

# def post_message_to_slack(text):
#     return requests.post('https://slack.com/api/chat.postMessage', {
#         'channel': 'Goal-notifications',
#         'text': text
#         # 'icon_emoji': slack_icon_emoji,
#         # 'username': slack_user_name,
#         # 'blocks': json.dumps(blocks) if blocks else None
#     }).json()	

def get_one_goal_or_abort(goal_id):
    try:
        goal_id = int(goal_id)
    except ValueError:
        response_str = f"Invalid goal_id: {goal_id} ID must be Integer"
        abort(make_response(jsonify({"message: response_str"}), 400))

    matching_goal = Goal.query.get(goal_id)

    if not matching_goal:
        response_str = f"Goal with id {goal_id} not found in database"
        abort(make_response(jsonify({"message": response_str}),404))

    return matching_goal


@goal_bp.route("", methods=["POST"])
def create_Goal():
    
    request_body = request.get_json() # when we are requesting something like sending something extra
    if "title" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

    new_Goal = Goal(
        title = request_body["title"]
        
    )
    db.session.add(new_Goal)
    db.session.commit()

    Goal_dict = {"id": new_Goal.goal_id,
    "title": new_Goal.title
    }

    return jsonify({"goal":Goal_dict}), 201

# @goal_bp.route("", methods = ["GET"])
# def get_Goal_all():
#     title_query = request.args.get("sort") #this will give asc
#     if title_query is not None and title_query=="asc":
#         Goals = Goal.query.order_by(Goal.title).all()
#     elif title_query is not None and title_query=="desc":
#         Goals = Goal.query.order_by(Goal.title.desc()).all()
#     elif title_query is None:
#         Goals = Goal.query.all()
    
#     response= []
    
#     for Goal in Goals:
#         is_completed = True
#         if Goal.completed_at is None:
#             is_completed = False
#         Goal_dict = {
#             "id": Goal.goal_id,
#             "title": Goal.title,
#             "description": Goal.description,
#             "is_complete": is_completed
            
#         }

#         response.append(Goal_dict)
#     return jsonify(response), 200

# @goal_bp.route("/<goal_id>", methods =["GET"])
# def get_one_Goal(goal_id):
#     Goals = Goal.query.all()
#     try:
#         goal_id = int(goal_id)
#     except ValueError:
#         response_str = f"Invalid goal_id: {goal_id} ID must be integer"
#         return jsonify({"message": response_str}), 400

#     for Goal in Goals:
#         if goal_id == Goal.goal_id:
#             is_completed = True
#             if Goal.completed_at is None:
#                 is_completed = False
#             Goal_dict = {
#                 "id": Goal.goal_id,
#                 "title": Goal.title,
#                 "description": Goal.description,
#                 "is_complete": is_completed
#             }
#             return jsonify({"Goal": Goal_dict}), 200
#     response_message = f"Could not find Goal with ID {goal_id}"
#     return jsonify({"message": response_message}), 404

# @goal_bp.route("/<goal_id>", methods = ["PUT"])
# def update_Goal(goal_id):
#     goal = get_one_goal_or_abort(goal_id) # we are getting a validated Goal id here
#     request_body = request.get_json() #converts json into dictionary

#     is_completed = True
#     if Goal.completed_at is None:
#         is_completed=False
#     Goal.title = request_body["title"]
#     db.session.commit()

#     Goal_dict = {"id": Goal.goal_id,
#     "title": Goal.title
#     # "description": Goal.description,
#     # "is_complete": is_completed
#     }

#     return jsonify({"Goal":Goal_dict}), 200

# @goal_bp.route("/<goal_id>/mark_complete", methods = ["PATCH"])
# def update_Goal_completed_at(goal_id):
#     goal = get_one_goal_or_abort(goal_id) #validated goal_id = 1
#     if Goal.completed_at is None:
#         Goal.completed_at = date.today()
#     is_completed = True
#     db.session.commit()
#     post_message_to_slack("Someone just completed the Goal "+Goal.title)
#     Goal_dict = {
#         "id": Goal.goal_id,
#         "title": Goal.title,
#         "description": Goal.description,
#         "is_complete": is_completed
#     }
#     return jsonify({"Goal":Goal_dict}),200
#     # lessons- 1) Always chk blueprint. Path will start after that
#     #2) call request body only if there are extra params other than url directly

# @goal_bp.route("/<goal_id>/mark_incomplete", methods = ["PATCH"])
# def update_Goal_mark_incomplete_on_completed_Goal(goal_id):
#     goal = get_one_goal_or_abort(goal_id) #validated goal_id = 1
#     Goal.completed_at = None
#     is_completed = False
#     db.session.commit()
#     Goal_dict = {
#         "id": Goal.goal_id,
#         "title": Goal.title,
#         "description": Goal.description,
#         "is_complete": is_completed
#     }
#     return jsonify({"Goal":Goal_dict}),200
#     # lessons- 1) Always chk blueprint. Path will start after that
#     #2) call request body only if there are extra params other than url directly

    

# @goal_bp.route("<goal_id>", methods=["DELETE"])
# def delete_one_Goal(goal_id):
#     chosen_goal=goal = get_one_goal_or_abort(goal_id)

#     db.session.delete(chosen_goal)
#     db.session.commit()
#     return jsonify({"details": f'Goal {goal_id} "Go on my daily walk 🏞" successfully deleted'}),200