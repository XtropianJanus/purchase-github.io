from flask import Flask, request, jsonify
from database import db, Purchase, Recipe, Event, Spoilage, Intertransfer, Project

app = Flask(__name__)

@app.route('/purchase', methods=['POST'])
def create_purchase():
    order_details = request.json.get('order_details')
    new_purchase = Purchase(order_details=order_details)
    db.session.add(new_purchase)
    db.session.commit()
    return jsonify({'message': 'Purchase created!', 'id': new_purchase.id}), 201

@app.route('/purchase', methods=['GET'])
def get_purchases():
    purchases = Purchase.query.all()
    return jsonify([{'id': p.id, 'order_details': p.order_details} for p in purchases])

@app.route('/recipe', methods=['POST'])
def add_recipe():
    details = request.json.get('details')
    new_recipe = Recipe(details=details)
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe added!', 'id': new_recipe.id}), 201

@app.route('/recipe', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{'id': r.id, 'details': r.details} for r in recipes])

@app.route('/event', methods=['POST'])
def create_event():
    details = request.json.get('details')
    new_event = Event(details=details)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created!', 'id': new_event.id}), 201

@app.route('/event', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': e.id, 'details': e.details} for e in events])

@app.route('/spoilage', methods=['POST'])
def track_spoilage():
    item_id = request.json.get('item_id')
    new_spoilage = Spoilage(item_id=item_id)
    db.session.add(new_spoilage)
    db.session.commit()
    return jsonify({'message': 'Spoilage tracked!', 'id': new_spoilage.id}), 201

@app.route('/spoilage', methods=['GET'])
def get_spoilage():
    spoilages = Spoilage.query.all()
    return jsonify([{'id': s.id, 'item_id': s.item_id} for s in spoilages])

@app.route('/intertransfer', methods=['POST'])
def transfer_item():
    item_id = request.json.get('item_id')
    from_location = request.json.get('from_location')
    to_location = request.json.get('to_location')
    new_transfer = Intertransfer(item_id=item_id, from_location=from_location, to_location=to_location)
    db.session.add(new_transfer)
    db.session.commit()
    return jsonify({'message': 'Item transferred!', 'id': new_transfer.id}), 201

@app.route('/intertransfer', methods=['GET'])
def get_intertransfers():
    transfers = Intertransfer.query.all()
    return jsonify([{'id': t.id, 'item_id': t.item_id, 'from_location': t.from_location, 'to_location': t.to_location} for t in transfers])

@app.route('/project', methods=['POST'])
def create_project():
    data = request.json
    new_project = Project(
        project_name=data['project_name'],
        description=data.get('description'),
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        status=data['status']
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created!', 'id': new_project.id}), 201

@app.route('/project', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{'id': p.id, 'project_name': p.project_name, 'description': p.description, 'start_date': p.start_date, 'end_date': p.end_date, 'status': p.status} for p in projects])

@app.route('/project/<int:id>', methods=['PUT'])
def update_project(id):
    data = request.json
    project = Project.query.get_or_404(id)
    project.project_name = data['project_name']
    project.description = data.get('description', project.description)
    project.start_date = data['start_date']
    project.end_date = data.get('end_date', project.end_date)
    project.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Project updated!'}), 200

@app.route('/project/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
