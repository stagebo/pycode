import psycopg2

conn = psycopg2.connect(database="pcnp", user="postgres", password="", host="", port="5432")
print("Opened database successfully")

def excute(sql):
    cur = conn.cursor()
    cur.execute(sql)
    print("Table created successfully")
    conn.commit()


def query(sql):
    cur = conn.cursor()
    cur.execute(sql)
    ret = []
    for row in cur:
        ret.append(row)
    conn.commit()

    return ret
#  主键添加
sc = "fhyc_business"
sc = "xzh_business"
sc = "zhl_business"
sql = "select tablename from pg_tables where schemaname = '%s'"%sc
ret = query(sql)
err = []
sqls = []
for row in ret:
    tn = row[0]
    if tn[-4:]!='_exp':
        continue
    tn = tn[:-4]
    print(tn)
    sql = "select f_name,f_pkey from %s.%s_exp"%(sc,tn)
    exp = query(sql)
    pk = []
    for e in exp:
        # print(e)
        if str(e[1]).isdigit() and int(e[1]) == 1:
            pk.append(e[0])
    has_pk = len(pk)
    pk.append('f_sid')
    print('pkeys:',','.join(pk))

    if has_pk:
        sql = """
        ALTER TABLE %s.%s DROP CONSTRAINT %s_pkey;ALTER TABLE %s.%s ADD PRIMARY KEY (%s);
        """%(sc,tn,tn,sc,tn,','.join(pk))
        sqls.append(sql)
        try:
            print(excute(sql))
        except:
            print(sql)
            err.append(tn)
    else :
        sql = """
             ALTER TABLE %s.%s ADD PRIMARY KEY (%s);
              """ % ( sc, tn, ','.join(pk))
    # sql = """"""
    print(sql)
print(err)
for s in sqls:
    print(s)
    # print(excute(sql))
# data_s = """tae_pw_zhbledger@tae_pw_zhbledger@tae_pw_chxdz|(f_dydj>10 and f_kglx=’断路器’)@tae_pw_kx_lineledger@tae_pw_kx_lineequipment@tae_pw_pdsh@tae_pw_xb@tae_pw_pdbyq_pdbyqtjb@tae_pw_pdbyq_pdbyqtjb |f_ssshb=’’）@tae_pw_chxdz|（f_dydj<=10 and f_kglx=’断路器’）@tae_pw_chxdz|（f_dydj<=10 and f_kglx=’负荷开关’）@tae_pw_kg_dlqtjb@tae_pw_kg_fhkgtjb@"""
# d1 = data_s.split('@')
# sql_list = []
# for d in d1:
#     tablename = d.split('|')[0]
#     condition = d.split('|')[1] if(len(d.split('|'))>1) else None
#     if not tablename:
#         continue
#     # print(tablename,'     ',condition)
#     if condition:
#         cond = '"filter": "%s",'%condition
#         json_str = '{%s "ispage": "true", "pagesize": "10", "mergetype": "0", "fixleftcolnums": "0", "rowspancolnums": ""}'%cond
#     else :
#         json_str =  '{"ispage": "true", "pagesize": "10", "mergetype": "0", "fixleftcolnums": "0", "rowspancolnums": ""}'
#     sql = """
#     insert into system.t_table_meta  (f_system_id,f_tablename,f_meta)  values   ('%s','%s','%s');
#     """%(1,tablename,json_str)
#     print(sql)
#     sql_list.append(sql)

# excute(''.join(sql_list))
#
# data_s = """tae_base_bdzhyxshj@tae_base_byqyxshj@tae_base_zhyxlyxshj@tae_base_gdnl@tae_base_gdzhl@tae_base_dwxl@tae_base_bdzhgchzj@tae_base_xlgchzj@tae_base_pdshshzj"""
# data_s = """tae_base_jjshhxx@tae_base_dlgxxx@tae_base_bdzhyxshj@tae_base_byqyxshj@tae_base_zhyxlyxshj@tae_base_gdnl@tae_base_gdzhl@tae_base_dwxl@tae_base_bdzhgchzj@tae_base_xlgchzj@tae_base_pdshshzj"""
# data_s = 'tae_base_jjshhxx@tae_base_dlgxxx@tae_base_fdshb'
# d1 = data_s.split('@')
# sql_list = []
# for d in d1:
#     tablename = d.split('|')[0]
#     condition = d.split('|')[1] if(len(d.split('|'))>1) else None
#     if not tablename:
#         continue
#     # print(tablename,'     ',condition)
#     if condition:
#         cond = '"filter": "%s",'%condition
#         json_str = '{%s "ispage": "true", "pagesize": "10", "mergetype": "0", "fixleftcolnums": "0", "rowspancolnums": ""}'%cond
#     else :
#         json_str =  '{"ispage": "true", "pagesize": "10", "mergetype": "0", "fixleftcolnums": "0", "rowspancolnums": ""}'
#     sql = """
#     insert into system.t_table_meta  (f_system_id,f_tablename,f_meta)  values   ('%s','%s','%s');
#     """%(5,tablename,json_str)
#     print(sql)
#     sql_list.append(sql)
# print(len(sql_list))
# excute(''.join(sql_list))

#
# data = """经济社会信息|tae_base_jjshhxx@电力供需信息|tae_base_dlgxxx@变电站运行数据|tae_base_bdzhyxshj@变压器运行数据|tae_base_byqyxshj@中压线路运行数据|tae_base_zhyxlyxshj@供电能力|tae_base_gdnl@供电质量|tae_base_gdzhl@电网效率|tae_base_dwxl@变电工程造价|tae_base_bdzhgchzj@线路工程造价|tae_base_xlgchzj@配电设施造价|tae_base_pdshshzj@"""
#
# l = data.split('@')
# sqllist = ''
# for d in l:
#
#     x = d.split('|')
#     if len(x) < 2:
#         continue
#     cname = x[0]
#     name = x[1]
#     print(name,cname)
#     sql = """
#     insert into system.t_tables (f_tablename,f_cname,f_online,f_beneed,f_groupindex,f_groupname)
#     values
#     ('%s','%s','%s','%s','%s','%s') on conflict do nothing;
#     """%(name,cname,1,1,7,'基础数据')
#     sqllist += sql
#
# excute(sqllist)

# sql = """
#
#                 insert into fhyc_view.t_layers_info
#                 ( f_lon_min,f_lat_min,f_lon_max,f_lat_max,f_geom_type,f_sid,f_layer_name )
#                 select
#
#                 min(ret.lon::varchar::float) as f_lon_min
#                 ,min(ret.lat::varchar::float) as f_lat_min
#                 ,max(ret.lon::varchar::float) as f_lon_max
#                 ,max(ret.lat::varchar::float) as f_lat_max
#                 ,ret.geomType::varchar as f_geom_type
#                 ,ret.sid as f_sid
#
#                 ,'%s' as f_layer_name
#                  from(
#                 select
#                   CASE WHEN  (wkb_geometry::json  -> 'type' ) :: VARCHAR = '"Point"'
#                   THEN wkb_geometry::json -> 'coordinates'-> 0
#                   WHEN (  wkb_geometry::json -> 'type' ) :: VARCHAR = '"MultiPolygon"'
#                   THEN json_array_elements(json_array_elements(json_array_elements(wkb_geometry::json-> 'coordinates')))->0
#                   WHEN (  wkb_geometry::json -> 'type' ) :: VARCHAR = '"LineString"'
#                   THEN (json_array_elements(wkb_geometry::json-> 'coordinates'))->0
#                   ELSE json_array_elements(json_array_elements(wkb_geometry::json-> 'coordinates'))-> 0
#                   END AS lon
#                   , CASE WHEN(wkb_geometry::json-> 'type') :: VARCHAR = '"Point"'
#                   THEN  wkb_geometry::json-> 'coordinates'-> 1
#                   WHEN (wkb_geometry::json -> 'type' ) :: VARCHAR = '"MultiPolygon"'
#                   THEN json_array_elements(json_array_elements(json_array_elements(wkb_geometry::json-> 'coordinates')))->1
#                   WHEN (  wkb_geometry::json -> 'type' ) :: VARCHAR = '"LineString"'
#                   THEN (json_array_elements(wkb_geometry::json-> 'coordinates'))->1
#                   ELSE json_array_elements(json_array_elements(wkb_geometry::json-> 'coordinates'))-> 1
#                   END AS lat
#                 , wkb_geometry::json->'type' AS geomType
#                 ,wkb_geometry::json as geo
#
#                 ,* from fhyc_view.%s where sid = 'S65010200000000000000000002') as ret
#                 group by ret.geomType::varchar,ret.sid
# """
#
# table_list = []
# sql_table = "select tablename from pg_tables where schemaname='fhyc_view' and tablename <> 't_layers_info';"
# ret = query(sql_table)
# for row in ret:
#     table_list.append(row[0])
# for table in table_list:
#     sql_item = sql % (table,table)
#     print(table)
#     excute(sql_item)