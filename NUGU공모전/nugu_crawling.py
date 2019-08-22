#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame as df

# CU
cu = "https://pyony.com/brands/cu/?page=1&event_type=1&category=&item=100&sort=&q="
# �̸�Ʈ24
emart = "https://pyony.com/brands/emart24/?page=1&event_type=1&category=&item=100&sort=&q="


# ********** ���⸸ �ǵ�� **********
# csv_name ������ ���ϴ� ��ǰ����� ������ �ٲ��ָ��
csv_name = "cu"
# ********** ���⸸ �ǵ�� **********


# ��ǰ��, ���� �׸�, ���� ����Ʈ ����
product_list = []
sale_list = []
price_list = []

# url ����
url_base = eval(csv_name)

# '1+1'��ǰ���� '4+1'��ǰ���� �� ���� �׸� ����
for i in range(1, 5):
    event_type = "type=" + str(i)
    url = url_base.replace("type=1", event_type)
    # �� ���� �׸� ������ �� ũ�Ѹ�
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    # ����ó�� : �� ���� �׸��� ��ǰ�� �ϳ��� ���� ��� �н�
    try:
        page_base = int(bsObject.find("span", {"class":"current"}).text.strip().split(" ")[2]) + 1
    except:
        pass
    # �����Ⱚ �ɷ����� ���� ����
    head = True
    tail = True
    # �� �׸��� ������ ����
    for j in range(1, page_base):
        page = "page=" + str(j)
        url_use = url.replace("page=1", page)
        html = urlopen(url_use)
        bsObject = BeautifulSoup(html, "html.parser")
        # ��ǰ��, ���� �׸� ����Ʈ ä���
        for link in bsObject.find_all('strong'):
            value = link.text.strip()
            if tail:  # value�� "�ֱ� �Խñ�" ~ "���� ������ �����ϱ�"�� �ƴ� ��� True
                if head:
                    head = False
                else:
                    if value == "�ֱ� �Խñ�":
                        tail = False
                    else:
                        # ����Ʈ�� �߰�
                        value = value.replace("HEYROO", "���̷�")
                        value = value.replace("Vplan", "�����÷�")
                        value = value.replace("Dole", "��")
                        value = value.replace("HEYROO", "���̷�")
                        value = value.replace("Vplan", "�����÷�")
                        value = value.replace("Dole", "��")
                        value = value.replace("SPAR", "����")
                        value = value.replace("GRN", "���˾�")
                        value = value.replace("SNJ", "����������")
                        value = value.replace("BIG", "��")
                        value = value.replace("CVS", "�����̿���")
                        value = value.replace("F&G", "��������")
                        value = value.replace("New", "��")
                        value = value.replace("CJ", "������")
                        value = value.replace("SF", "��������")
                        value = value.replace("CM", "��Ƽ����")
                        value = value.replace("cm", "��Ƽ����")
                        value = value.replace("ML", "�и�����")
                        value = value.replace("ml", "�и�����")
                        value = value.replace("GO", "��")
                        value = value.replace("XS", "��������")
                        value = value.replace("UP", "��")
                        value = value.replace("GT", "��Ƽ")
                        value = value.replace("KG", "ų�α׷�")
                        value = value.replace("kg", "ų�α׷�")
                        value = value.replace("O/N", "��������Ʈ")
                        value = value.replace("C", "��")
                        value = value.replace("V", "����")
                        value = value.replace("s", "����")
                        value = value.replace("T", "Ƽ")
                        value = value.replace("B", "��")
                        value = value.replace("X", "����")
                        value = value.replace("M", "����")
                        value = value.replace("m", "����")
                        value = value.replace("G", "�׷�")
                        value = value.replace("g", "�׷�")
                        value = value.replace("L", "����")
                        value = value.replace("P", "��")
                        value = value.replace("N", "����Ʈ")
                        value = value.replace("e", "��")
                        value = value.replace("F", "����")
                        value = value.replace("W", "������")
                        value = value.replace("*", "��")
                        value = value.replace("%", "����")
                        value = value.replace("&", "��")
                        value = value.replace(".", "��")
                        value = value.replace("/", "")
                        value = value.replace("(", "")
                        value = value.replace(")", "")
                        value = value.replace(" ", "")
                        product_list.append(value)
                        sale_list.append(i)
            elif value == "���� ������ �����ϱ�":
                tail = True
                head = True
        # ���� ����Ʈ ä���
        for link in bsObject.find_all("span", {"class":"text-muted small"}):
            value = int(link.text.strip().replace('(', "").replace(',', "").replace('��)', ""))
            # �� ���� ���ϱ�
            if i == 1:
                value = value * 2
            elif i == 2:
                value = value * 3
                if value % 10 == 1:
                    value = value - 1
                elif value % 10 == 9:
                    value = value + 1
            elif i == 3:
                value = value * 4
            elif i == 4:
                value = value * 5
            price_list.append(value)

# ������������ ����
db = df(data={'Product': product_list, 'Sale': sale_list, 'Price': price_list})

# csv ��ȯ
db.to_csv(csv_name + ".csv", mode="w", header=False, index=False, encoding='utf-7')