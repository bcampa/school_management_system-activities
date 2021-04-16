from config import app, rpc_config
from flask import jsonify, request
from nameko.standalone.rpc import ClusterRpcProxy


# routes

@app.route("/")
def home():
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        return cluster_rpc.activity_service.hello_world()

@app.route("/api/activity", methods=["GET"])
def activity_list():
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        return jsonify(cluster_rpc.activity_service.get_activities())

@app.route("/api/activity/<activity_id>", methods=["GET"])
def activity_detail(activity_id):
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        return jsonify(cluster_rpc.activity_service.get_activity(activity_id))

# @app.route("/api/activity/<activity_id>/conclude", methods=["GET"])
# def conclude_activity(activity_id):
#     with ClusterRpcProxy(rpc_config) as cluster_rpc:
#         return jsonify(cluster_rpc.activity_service.conclude_activity(activity_id))

@app.route("/api/activity/<activity_id>/concluded", methods=["PUT"])
def score_activity(activity_id):
    concluded = int(request.form["concluded"])
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        response = cluster_rpc.activity_service.set_activity_conclusion(activity_id, concluded)
        return jsonify(response)

# @app.route("/api/activity/<activity_id>/score/<score>", methods=["GET"])
# def score_activity(activity_id, score):
#     with ClusterRpcProxy(rpc_config) as cluster_rpc:
#         return jsonify(cluster_rpc.activity_service.score_activity(activity_id, score))

@app.route("/api/activity/<activity_id>/score", methods=["PUT"])
def update_activity_conclusion(activity_id):
    score = int(request.form["score"])
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        response = cluster_rpc.activity_service.score_activity(activity_id, score)
        return jsonify(response)

@app.route("/api/activity", methods=["POST"])
def create_activity():
    new_data = {
        "classcode" : request.form["classcode"],
        "student_id" : int(request.form["student_id"])
    }
    with ClusterRpcProxy(rpc_config) as cluster_rpc:
        return jsonify(cluster_rpc.activity_service.add_activity(new_data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12300, debug=True)
