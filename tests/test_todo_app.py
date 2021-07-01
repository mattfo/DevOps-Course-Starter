from config import DOING, DONE
from todo_app.data import session_items as session

def test_complete_doing_list_simple():

    # Arrange
    items_in_doing = [{'id': '60aae7e68ae1e01db6226b86', 'status': 'Not Started', 'title': 'Learn JSON'},
                      {'id': '60cdfc1746d7211010266ff7', 'status': 'Not Started', 'title': 'Learn XML'}]
    
    # Act
    items = session.get_items(DOING)
    
    # Assert
    print(" ")
    print(" ")
    print ('items_in_doing:')
    print(items_in_doing)
    
    print(" ")
    print ('items:')
    print(items)
    
    assert items_in_doing == items
    

def test_learn_postman_is_in_done_():
    
    # Arrange
    item_test_done = 'Learn Postman'
    item_found = 'False'
    array_sub = 1

    # Act
    items = session.get_items(DONE)
    
   
    #for i in session.array_count:
    while array_sub < session.array_count:
        session.add_item 1 to array_sub
        print('id')
        print(i['id'])
        print('name')
        print(i['name'])
        if i['name'] == 'Learn Postman':
            item_found = 'True'
    
    assert item_found == 'True'
    


def test_doing_list_model():
    
    # Arrange
    items_in_doing = [{'id': '60aae7e68ae1e01db6226b86', 'status': 'Not Started', 'title': 'Learn JSON'},
                      {'id': '60cdfc1746d7211010266ff7', 'status': 'Not Started', 'title': 'Learn XML'}]
    
    # Act
    # I guess I don't really understand this ViewModel stuff
    items = session.get_items(DOING)
    item_view_model = session.ViewModel(items)
    
    # Assert
    print(" ")
    print(" ")
    print ('items_in_doing:')
    print(items_in_doing)
  
    print(" ")
    print ('item_view_model:')
    print(item_view_model)
    
    assert items_in_doing == item_view_model





    
