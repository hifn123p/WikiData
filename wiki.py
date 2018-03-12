from bz2 import BZ2File
import json
from pymysql import Error as error
import pymysql

path = 'D:\Database\wikidata-latest-all.json.bz2'


def get_cn_al(dic):
    if 'zh-hans' in dic:
        return dic.get('zh-hans')
    elif 'zh' in dic:
        return dic.get('zh')
    elif 'zh-cn' in dic:
        return dic.get('zh-cn')
    else:
        return None


def get_value(dic):
    if 'zh-hans' in dic:
        return dic.get('zh-hans').get('value')
    elif 'zh' in dic:
        return dic.get('zh').get('value')
    elif 'zh-cn' in dic:
        return dic.get('zh-cn').get('value')
    else:
        return None


def get_en_value(dic):
    if 'en' in dic:
        return dic.get('en').get('value')
    else:
        return None


def get_list_value(list):
    res = ""
    if list:
        for i in list:
            res = res + i.get('value') + '\n'
        return res
    else:
        return None


def get_data_value(value):
    if isinstance(value, str):
        return value
    elif isinstance(value, dict):
        if 'id' in value:
            return value.get('id')
        elif 'time' in value:
            return value.get('time')


def get_qua_data(dic):
    if dic.get('qualifiers'):
        q = dic.get('qualifiers-order')  # qualitifiers id列表
        return q
    else:
        return None


def get_ref_data(dic):
    if dic.get('references'):
        return dic.get('references')
    else:
        return None


def get_qr_value(dic):
    if "datavalue" in dic:
        return dic.get('datavalue')
    else:
        return None


if __name__ == '__main__':

    con = pymysql.connect('localhost', 'root', '183145', 'wikidata', charset='utf8')
    cur = con.cursor()
    r_file = BZ2File(path)
    for line in r_file:
        i = 0
        for line in r_file:
            if line[0] == '[':
                continue
            elif line[0] == ']':
                break
            else:
                line = line[:-2]
                json_data = json.loads(line)
                id = json_data.get('id')
                en = get_en_value(json_data.get('labels'))
                zh_cn = get_value(json_data.get('labels'))
                descriptions = get_value(json_data.get('descriptions'))
                aliases = get_list_value(json_data.get('aliases').get('en'))
                if aliases:
                    aliases = aliases.replace("'", "~")
                else:
                    aliases = get_list_value(get_cn_al(json_data.get('aliases')))
                    if aliases:
                        aliases = aliases.replace("'", "`")
                if en:
                    en = en.replace("'", "`")
                if zh_cn:
                    zh_cn = zh_cn.replace("'", "`")
                if descriptions:
                    descriptions = descriptions.replace("'", "`")
                    descriptions = descriptions.replace("\\", "")
                else:
                    descriptions = get_en_value(json_data.get('descriptions'))
                    if descriptions:
                        descriptions = descriptions.replace("'", "`")
                        descriptions = descriptions.replace("\\", "")

                print('-------------------table1')
                print(id, ':', id)
                print(en)
                print(zh_cn)
                print('+++++++')
                print(descriptions)
                print('------')
                print(aliases)
                try:
                    sql = "insert into entity(id,en,cn,descriptions,aliases) values('%s','%s','%s','%s','%s');" % (
                        id, en, zh_cn, descriptions, aliases)
                    cur.execute(sql)
                    con.commit()
                except pymysql.err.InternalError:
                    None
                propertys = json_data['claims']  # 字典类型,进入到claims中的p_id列表
                for p_id in propertys:  # 遍历所有的p_id
                    values = propertys.get(p_id)  # 进入到property的values列表类型，多个value
                    for v in values:  # 遍历value
                        valu = get_qr_value(v.get('mainsnak'))
                        if valu:
                            value = valu.get('value')  # value为字符串或者字典
                            value_type = valu.get('type')  # 得到value的类型
                            val = get_data_value(value)  # 获取到具体value
                        else:
                            val = None
                            value_type = None
                        qualifiers_list = get_qua_data(v)  # 返回的是字典中的key列表
                        references_list = get_ref_data(v)  # 返回的是列表
                        try:
                            if not qualifiers_list and not references_list:
                                sql1 = "insert into mainsnaks(id,property,value,value_type) values('%s','%s','%s','%s');" % (
                                    id, p_id, val, value_type)
                                cur.execute(sql1)
                                con.commit()

                            if references_list:
                                for ref_list in references_list:  # 遍历references列表
                                    ref_id = ref_list.get('snaks-order')  # 得到，reference需要的snaks的key，列表
                                    for r_id in ref_id:  # 从列表中取出key
                                        ref_data = get_qr_value(ref_list.get('snaks').get(r_id)[0])
                                        if ref_data:
                                            ref = ref_data.get('value')
                                            refer = get_data_value(ref)  # value多个类型
                                            refer_type = ref_data.get('type')
                                        else:
                                            refer = None
                                            refer_type = None
                                        print('table2------')
                                        print(id)
                                        print(p_id)
                                        print(val)
                                        print(value_type)
                                        print(r_id)
                                        print(refer)
                                        print(refer_type)
                                        print("-------------table2")
                                        sql1 = "insert into refer(id,property,value,value_type,snaks_order,ref_value,ref_value_type) values('%s','%s','%s','%s','%s','%s','%s');" % (
                                            id, p_id, val, value_type, r_id, refer, refer_type)
                                        cur.execute(sql1)
                                        con.commit()

                            if qualifiers_list:
                                for qua_id in qualifiers_list:  # 遍历key
                                    qua_lists = v.get('qualifiers').get(qua_id)  # 得到列表
                                    for qua_list in qua_lists:
                                        qualities = get_qr_value(qua_list)
                                        if qualities:
                                            qual = qualities.get('value')
                                            qua_value = get_data_value(qual)  # value多个类型
                                            qua_type = qualities.get('type')
                                        else:
                                            qua_value = None
                                            qua_type = None
                                        print('table3------')
                                        print(id)
                                        print(p_id)
                                        print(val)
                                        print(value_type)
                                        print(qua_id)
                                        print(qua_value)
                                        print(qua_type)
                                        print("-------------table3")
                                        print(p_id, val, qua_value)
                                        sql = "insert into qualifers(id,property,value,value_type,qual_order,qual_value,qual_value_type) values('%s','%s','%s','%s','%s','%s','%s');" % (
                                            id, p_id, val, value_type, qua_id, qua_value, qua_type)
                                        cur.execute(sql)
                                        con.commit()
                        except error:
                            None

        i += 1
    # con.close()
    r_file.close()
