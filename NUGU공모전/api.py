import json
import pymysql

def result(req):
    brand = req['action']['parameters']['brand']['value']
    if brand == "CU":
        brand = "cu"
    elif brand == "EMART":
        brand = "emart"
    product = req['action']['parameters']['product']['value']

    conn = pymysql.connect(host='localhost', user='nuguplay', password='kjcloud', db='nuguplay', charset='utf8')
    curs = conn.cursor()
    sql = "select * from " + brand + "_data where product like \"%" + product + "%\" order by price asc, sale asc limit 3;"
    value = ""
    curs.execute(sql)
    rows = curs.fetchall()
    if len(rows) == 0:
        value = "�����Ͻ� ��ǰ�� ���� ������ �����ϴ�"
    for i in range(0, len(rows)):
        if rows[i][1] == 1:
            value = value + str(rows[i][0]) + "��ǰ�� �� �÷��� �� ���� �� " + str(rows[i][2]) + "���� �Ǹ����Դϴ�"
        elif rows[i][1] == 2:
            value = value + str(rows[i][0]) + "��ǰ�� �� �÷��� �� ���� �� " + str(rows[i][2]) + "���� �Ǹ����Դϴ�"
        elif rows[i][1] == 3:
            value = value + str(rows[i][0]) + "��ǰ�� ���� �÷��� �� ���� �� " + str(rows[i][2]) + "���� �Ǹ����Դϴ�"
        elif rows[i][1] == 4:
            value = value + str(rows[i][0]) + "��ǰ�� �� �÷��� �� ���� �� " + str(rows[i][2]) + "���� �Ǹ����Դϴ�"
        if i == len(rows)-1:
            value = value + " �̻��Դϴ�"
        else:
            value = value + " �׸��� "

    resp = {
        'version': '2.0',
        'resultCode': 'OK',
        'output': {
            'info': value
        }
    }
    conn.close()
    return json.dumps(resp, ensure_ascii=False, indent=4)