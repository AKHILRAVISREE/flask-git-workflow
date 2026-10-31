@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')

        if not item_name or not item_description:
            return "Item Name and Description are required.", 400

        todo_document = {
            "item_name": item_name,
            "item_description": item_description
        }

        # Assuming 'collection' is already initialized from your MongoDB setup
        # collection.insert_one(todo_document)
        
        return "To-Do item stored successfully in MongoDB!"
    except Exception as e:
        return f"Error: {str(e)}", 500