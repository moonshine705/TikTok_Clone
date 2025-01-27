from flask import Blueprint, request, jsonify
from .models import db, Video, Comment

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_video():
    data = request.json
    new_video = Video(title=data['title'], url=data['url'])
    db.session.add(new_video)
    db.session.commit()
    return jsonify({"message": "Video uploaded!"}), 201

@main.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return jsonify([
        {"id": video.id, "title": video.title, "url": video.url, "likes": video.likes} 
        for video in videos
    ])

@main.route('/like/<int:video_id>', methods=['POST'])
def like_video(video_id):
    video = Video.query.get(video_id)
    if video:
        video.likes += 1
        db.session.commit()
        return jsonify({"message": "Video liked!"})
    return jsonify({"error": "Video not found"}), 404
