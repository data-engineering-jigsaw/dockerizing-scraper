from src.models.position import Position

def test_init_position():
    position = Position(*['8cba12eacacdf624', 'Data Engineer', [70, 73], 'Ana-Data Consulting Inc', 'New York', 'NY'])
    assert position.__dict__ == {'id': '8cba12eacacdf624', 'title': 'Data Engineer', 'min_salary': 70, 'max_salary': 73, 'city': 'Ana-Data Consulting Inc', 'state': 'New York', 'company_name': 'NY'}
    