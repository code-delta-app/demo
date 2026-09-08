from flask import Flask, jsonify, request

app = Flask(__name__)

JOBS = {}


@app.route("/")
def index():
    return "buildproj control plane"


@app.route("/jobs", methods=["POST"])
def submit_job():
    payload = request.get_json(silent=True) or {}
    job_id = str(len(JOBS) + 1)
    JOBS[job_id] = {"state": "queued", "spec": payload}
    return jsonify({"id": job_id}), 202


@app.route("/jobs/<job_id>")
def job_status(job_id):
    job = JOBS.get(job_id)
    if job is None:
        return jsonify({"error": "no such job"}), 404
    return jsonify(job)


@app.route("/health")
def health():
    return jsonify({"status": "up", "jobs": len(JOBS)})


@app.route("/jobs/<job_id>", methods=["DELETE"])
def cancel_job(job_id):
    job = JOBS.get(job_id)
    if job is None:
        return jsonify({"error": "no such job"}), 404
    if job["state"] in ("done", "failed"):
        return jsonify({"error": "already finished"}), 409
    job["state"] = "cancelled"
    return jsonify(job)
