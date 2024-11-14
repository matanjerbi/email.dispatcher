from flask import Blueprint, request, jsonify
from app.services.mongo_service import save_to_mongodb
from app.services.kafka_service import send_to_kafka
from app.services.content_analyzer import analyze_content

bp = Blueprint('message_receiver', __name__, url_prefix='/api')


# הסר את השורה הזו - היא גורמת לשגיאה!
# bp.register_blueprint(bp)  <- מחק את זה!

@bp.route('/email', methods=['POST'])
def receive_email():
    data = request.get_json()

    if not data or 'sentences' not in data:
        return jsonify({
            'error': 'Invalid data format. Must include sentences field'
        }), 400
    # שמירה במונגו
    save_to_mongodb(data)

    # בדיקה אם יש תוכן חשוד
    analysis_result = analyze_content(data['sentences'])

    # שליחה לקפקא
    if analysis_result['is_suspicious']:
        if 'hostage' in analysis_result['type']:
            send_to_kafka('messages.hostage', data)
        elif 'explosive' in analysis_result['type']:
            send_to_kafka('messages.explosive', data)

    return jsonify({'message': 'Received'}), 200