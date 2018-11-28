#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     java_jdbc_template
    Author:         wyb
    Date:          2018/10/30 0030
    Description:   java jdbc 模板
"""

import pymysql
import configparser
import sys
import os
sys.path.append('../')
import mysqldba
cf = configparser.ConfigParser()
cf.read("../application.conf", encoding='utf-8')

# dbname = "examsystem"
# dbname = "booksystem"
# dbname = "expresssystem"
dbname = "reportsystem"
dbname = "sportsystem"

mysqldba.opencf(cf, dbname)
packagename = "com.web.sys"

def get_struct(tablename,db):
    sql = '''select column_name as column_name
    ,data_type as data_type
    ,character_maximum_length as character_maximum_length
    ,is_nullable as is_nullable
    ,column_comment as column_comment
            from information_schema.columns
            where table_schema = '%s'
            and table_name = '%s' ; '''%(db,tablename)
    # print(sql)
    all = mysqldba.fetch_all(sql)
    return all

def show_table_status():
    sql = "show table STATUS;"
    statuses = mysqldba.fetch_all(sql)
    ret = {}
    for row in statuses:
        ret[row['Name']] = row
    return ret

def f2upper(s):
    return s[0].upper()+s[1:]

def get_java_type(dt):
    jt = None
    if dt in ['varchar','text']:
        jt = 'String'
    elif dt in ['datetime','date','timestamp']:
        jt = 'Date'
    elif dt in ['int','smallint']:
        jt = 'int'
    elif dt in ['bigint']:
        jt = "long"
    elif dt in ['double','float','decimal']:
        jt = 'double'
    elif dt in ["blob","longblob"]:
        jt = "Byte[]"
    else:
        raise Exception("type [%s] not found"%dt)
    return jt


def make_bean(tablename,dbname,file=None):
    classname = f2upper(tablename)
    structs = get_struct(tablename,dbname)
    code = f"""package {packagename}.model;
import {packagename}.model.BaseModel;

import java.util.Date;

public class {classname} extends BaseModel{{   """
    fields_code = []
    get_set_code = []
    fields_json = []
    is_start = True
    for row in structs:
        print(row)
        cn = row['column_name']
        dt = row['data_type']
        cml = row['character_maximum_length']
        jt = get_java_type(dt)
        is_nullable = row['is_nullable']
        com = "可空" if is_nullable == "YES" else "不可空"
        if not jt:
            continue
        fields_code.append("""
    // %s
    private %s %s;"""%(com, jt, cn))
        get_set_code.append("""
    public %s get%s(){ return %s;}        """%(jt,f2upper(cn),cn))
        get_set_code.append(""" 
    public void set%s(%s %s){ this.%s = %s;  }
        """%(f2upper(cn),jt,cn,cn,cn))
        if is_start:
            fields_json.append("""
            sb.append("\\"%s\\":\\""+ this.get%s() +"\\"");"""%(cn,f2upper(cn)))
            is_start = False
        fields_json.append("""
            sb.append(",\\"%s\\":\\""+ this.get%s() +"\\"");""" % (cn, f2upper(cn)))
    code += ''.join(fields_code)

    code += """
    
    public %s(){}    
    """%classname

    code += ''.join(get_set_code)
    code += """
    """
    code += """
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("{");    """
    code += ''.join(fields_json)
    code += """
        sb.append("}");
        return sb.toString();
    }  """
    code += """
}    """
    if file:
        file.write(code)
    return code


def make_dao(db,tablename,file):
    code = ""
    classname = f2upper(tablename)

    code += f"""package {packagename}.dao;

import {packagename}.model.{classname};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import com.web.sys.utils.T;
import java.util.List;
import java.util.ArrayList;
@Repository
public class {classname}DAO {{

    @Autowired
    private JdbcTemplate jdbcTemplate;
    """


    structs = get_struct(tablename, dbname)
    # print(structs)
    idtype = None
    fields = []
    not_null_fields = []
    for row in structs:
        cn = row['column_name']
        dt = row['data_type']
        cml = row['character_maximum_length']
        jt = get_java_type(dt)
        is_nullable = row['is_nullable']

        if cn == 'id':
            idtype = jt

        if not jt:
            continue
        fields.append(cn)
        if is_nullable.upper() == "NO":
            not_null_fields.append(cn)

    #     print(idtype, cn, jt)
    # print(idtype,tablename)
    assert idtype is not None

    condition_temp = """
          if(!T.isNullOrWhite(%s.get%s())){
              notNulls.add("%s=?");
              params.add(%s.get%s());
          }"""
    insert_condition_temp = """
          if(!T.isNullOrWhite(%s.get%s())){
              notNulls.add("%s");
              notNQ.add("?");
              params.add(%s.get%s());
          }"""
    conditions = []
    insert_conditions = []
    for field in fields:
        if field in not_null_fields or field == "id":
            insert_conditions.append(insert_condition_temp % (tablename, f2upper(field), field, tablename, f2upper(field)) + "else return false;")

        else:
            insert_conditions.append(insert_condition_temp % (tablename, f2upper(field), field, tablename, f2upper(field)))

        if field == "id":
            continue
        conditions.append(condition_temp%(tablename,f2upper(field),field,tablename,f2upper(field)))


    code += f"""
    
    private String find{classname}ByID = "select {','.join(fields)} from {tablename} where id = ?";"""

    code += f"""
    private String update{classname}ByID = "update {tablename} set { ','.join([ '%s = ?'%i for i in fields if i != 'id' ]) } where id = ?";"""
    code += f""" 
    private String delete{classname}ByID = "delete from {tablename} where id = ?";  """
    code += f""" 
    private String find{classname}List = "select {','.join(fields)} from {tablename}"; """

    code += f"""
    
    public boolean insert{classname}({classname} {tablename}) {{
        List<String> notNulls = new ArrayList<>();
        List<Object> params = new ArrayList<>();
        List<String> notNQ = new ArrayList<>();
        {''.join(insert_conditions)}
        String sql = String.format("insert into {tablename} (%s) values(%s)",String.join(",",notNulls),String.join(",",notNQ));
        int ret = jdbcTemplate.update(sql,params.toArray());
        if(ret != 1){{
            return false;
        }}
        return true;
    }}

    public boolean update{classname}({classname} {tablename}){{
        int ret = jdbcTemplate.update(update{classname}ByID, {','.join(['%s.get%s()'%(tablename,f2upper(i)) for i in fields if i != 'id'])},{tablename}.getId());
        if(ret != 1){{
            return false;
        }}
        return true;
    }}
    
    public boolean update{classname}NotNull({classname} {tablename}){{
        StringBuilder sqlb = new StringBuilder("update {tablename} set ");
        boolean needUpdate = false;
        List<String> notNulls = new ArrayList<>();
        List<Object> params = new ArrayList<>();
        {''.join(conditions)}
        if(notNulls.size() < 1){{
            return true;
        }}
        sqlb.append("".join(",",notNulls));
        sqlb.append(" where id = ? ");
        params.add({tablename}.getId());
        String sql = sqlb.toString();
        int ret = jdbcTemplate.update(sql, params.toArray());
        if(ret != 1){{
            return false;
        }}
        return true;
    }}
    
    public boolean delete{classname}ByID({idtype} id){{
        int ret = jdbcTemplate.update(delete{classname}ByID, id);
        if(ret != 1){{
            return false;
        }}
        return true;
    }}

    public {classname} find{classname}ByID(String id) {{
        List<{classname}> list = jdbcTemplate.query(find{classname}ByID, new Object[]{{id}}, new BeanPropertyRowMapper({classname}.class));
        if(list!=null && list.size()>0){{
            {classname} {tablename} = list.get(0);
            return {tablename};
        }}else{{
            return null;
        }}
    }}

    public List<{classname}> find{classname}List() {{
        List<{classname}> list = jdbcTemplate.query(find{classname}List, new Object[]{{}}, new BeanPropertyRowMapper({classname}.class));
        return list;
    }}
   public int count{classname}(){{
        return (int) jdbcTemplate.queryForObject("select count(*) from {tablename}", int.class);
    }}
}}
    """
    if file:
        file.write(code)
    return code

def make_service(db,tablename,file):
    classname = f2upper(tablename)

    structs = get_struct(tablename, dbname)
    idtype = None
    fields = []
    not_null_fields = []
    for row in structs:
        cn = row['column_name']
        dt = row['data_type']
        cml = row['character_maximum_length']
        is_nullable = row['is_nullable']
        jt = get_java_type(dt)

        if cn == 'id':
            idtype = jt
        if not jt:
            continue
        fields.append(cn)
        if is_nullable.upper() == "NO":
            not_null_fields.append(cn)
    assert idtype is not None
    cdtmp = """
    if(T.isNullOrWhite(%s.get%s())){
            return R.ret(R.ERR,"%s 不能为空！");
        }"""
    nt_cds = []
    for ncn in not_null_fields:
        nt_cds.append(cdtmp%(tablename,f2upper(ncn),ncn))

    code = f"""package {packagename}.service;

import {packagename}.dao.{classname}DAO;
import {packagename}.model.{classname};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class  {classname}Service extends BaseService{{

    @Autowired
    private {classname}DAO {tablename}DAO;

    public boolean insert{classname}({classname} {tablename}) {{ return {tablename}DAO.insert{classname}({tablename});  }}

    public boolean update{classname}({classname} {tablename}){{ return {tablename}DAO.update{classname}({tablename});  }}

    public boolean update{classname}NotNull({classname} {tablename}){{ return {tablename}DAO.update{classname}NotNull({tablename}); }}

    public boolean delete{classname}ByID(String id){{ return {tablename}DAO.delete{classname}ByID(id); }}

    public {classname} find{classname}ByID(String id) {{ return {tablename}DAO.find{classname}ByID(id); }}

    public List<{classname}> find{classname}List() {{ return {tablename}DAO.find{classname}List(); }}
    
    public int count{classname}(){{ return {tablename}DAO.count{classname}();    }}
}}
   """
    if file:
        file.write(code)
    return code


def make_controller(db, tablename, file):
    classname = f2upper(tablename)

    structs = get_struct(tablename, dbname)
    idtype = None
    fields = []
    not_null_fields = []
    for row in structs:
        cn = row['column_name']
        dt = row['data_type']
        cml = row['character_maximum_length']
        is_nullable = row['is_nullable']
        jt = get_java_type(dt)

        if cn == 'id':
            idtype = jt
        if not jt:
            continue
        fields.append(cn)
        if is_nullable.upper() == "NO" and cn != 'id':
            not_null_fields.append(cn)
    assert idtype is not None


    cdtmp = """
        if(T.isNullOrWhite(%s.get%s())){
            return R.ret(R.ERR,"%s 不能为空！");
        }"""
    nt_cds = []
    for ncn in not_null_fields:
        nt_cds.append(cdtmp % (tablename, f2upper(ncn), ncn))
    code = f"""package {packagename}.controller;

import {packagename}.utils.R;
import {packagename}.utils.T;
import {packagename}.model.{classname};
import {packagename}.service.{classname}Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.*;

@Controller
@RequestMapping("/api/{tablename}")
public class {classname}Controller {{


    @Autowired
    {classname}Service {tablename}Service;

    @RequestMapping(value = "/add",method = RequestMethod.POST)
    public @ResponseBody Object add({classname} {tablename}) {{
        {''.join(nt_cds)}

        {tablename}.setId(UUID.randomUUID().toString());
        boolean flag = {tablename}Service.insert{classname}({tablename});
        if(!flag){{
            return R.ret(R.ERR);
        }}
        return R.ret(R.OK, {tablename});
    }}
    @RequestMapping(value = "/remove",method = RequestMethod.POST)
    public @ResponseBody Object delete(String id) {{
        if(T.isNullOrWhite(id)){{
            return R.ret(R.ERR,"id 不能为空！");
        }}
        boolean flag = {tablename}Service.delete{classname}ByID(id);
        if(!flag){{
            return R.ret(R.ERR);
        }}
        return R.ret(R.OK);
    }}

    @RequestMapping(value = "/modify",method = RequestMethod.POST)
    public @ResponseBody Object modify({classname} {tablename}) {{
        if(T.isNullOrWhite({tablename}.getId())){{
            return R.ret(R.ERR,"id 不能为空");
        }}       
        {classname} t{tablename} = {tablename}Service.find{classname}ByID({tablename}.getId());
        if(t{tablename} == null){{
            return R.ret(R.ERR,"查无数据");
        }}
        boolean flag = {tablename}Service.update{classname}NotNull({tablename});
        if(!flag){{
            return R.ret(R.ERR);
        }}
        return R.ret(R.OK);
    }}

    @RequestMapping(value = "/get",method = RequestMethod.GET)
    public @ResponseBody Object get({classname} {tablename}) {{
        if(T.isNullOrWhite({tablename}.getId())){{
            return R.ret(R.ERR,"id 不能为空");
        }}
        {classname} t{tablename} = {tablename}Service.find{classname}ByID({tablename}.getId());
        if(t{tablename} == null){{
            return R.ret(R.ERR,"{tablename} 不存在");
        }}

        return R.ret(R.OK,t{tablename});
    }}
    
    @RequestMapping(value="/list",method = RequestMethod.GET)
    public @ResponseBody Object list() {{
        return R.ret(R.OK, {tablename}Service.find{classname}List());
    }}

    @RequestMapping(value="/count",method = RequestMethod.GET)
    public @ResponseBody Object count() {{
        int count = {tablename}Service.count{classname}();
        Map<String,Object> ret = new HashMap<>();
        ret.put("count",count);
        return R.ret(R.OK, ret);
    }}

     //配置404页面
     @RequestMapping("*")
     public String notFind(){{
        return "404";
     }}


}}
    """
    if file:
        file.write(code)
    return code

docs = []
def make_doc(db,tablename):
    global docs, tables_comments
    classname = f2upper(tablename)

    structs = get_struct(tablename, db)
    idtype = None
    fields = []
    not_null_fields = []
    params = []
    table_comment = tables_comments[tablename]['Comment']
    for row in structs:
        cn = row['column_name']
        dt = row['data_type']
        cml = row['character_maximum_length']
        is_nullable = row['is_nullable']
        jt = get_java_type(dt)

        if cn == 'id':
            idtype = jt
        if not jt:
            continue
        fields.append(cn)
        is_null_text = "不可为空" if is_nullable.upper() == "NO"else "可空"
        params.append((cn,jt,is_null_text))
    assert idtype is not None

    pt = """
                * %s     %s     %s"""
    ptl = [pt % i for i in params if i != "id"]

    ptu = [pt % (i[0], i[1], '可空') for i in params if i != "id"]
    ptu.insert(0, "                    * id    String   不可为空")

    doc_tmp = f"""
----
## 添加 {table_comment}
        * 地址：/api/{tablename}/add
        * 类型：POST
        * 参数：
        {''.join(ptl)}
        * 返回值：基本格式


---

## 删除 {table_comment}
        * 地址：/api/{tablename}/delete
        * 类型：POST
        * 参数：
        {pt%('id',idtype,'不可为空')}
        * 返回值：基本格式

----

## 查询 {table_comment}
        * 地址：/api/{tablename}/list
        * 类型：GET
        * 参数：无
        * 返回值：基本格式

----

## 修改 {table_comment}
        * 地址：/api/{tablename}/modify
        * 类型：POST
        * 参数：
        {pt % ('id', 'int', '不可为空')}
        * 返回值：基本格式

----

## 查询 {table_comment}
        * 地址：/api/{tablename}/get
        * 类型：GET
        * 参数：
        {pt%('id',idtype,'不可为空')}
        * 返回值：
                * data {tablename} 对象属性

---

## 计数 {table_comment}
        * 地址：/api/{tablename}/count
        * 类型：GET
        * 参数：无
        * 返回值：
            * data {table_comment} 对象属性
    """


    docs.append(doc_tmp)

tables_comments = show_table_status()
print(tables_comments)
if __name__ == "__main__":



    tables = [
        # 'book',
        # 'booktype',
        # 'lendrecord',
        # 'moneyrecord',
        # 'publish',
        # 'role',
        # 'ruser',
        # 'user',
        # 'wuser',
        # 'user_role',
        # "attachment",
        # "order",
        # "station",
        # "user_tclass"
        # "area",
        # "report",
        # "informant",
        # "informanter",
        # "informantee",
        # "repeat",
        "orders",
        "project",
        "comment",
    ]
    for t in tables:
        # dir = "src\\main\\java\\com\\web\\sys\\"
        # doc_dir = "src\\main\\resources\\templates\\doc\\base.html"
        # dir = 'src\\main\\java\\com\\web\\sys\\'

        dir = ""
        mf = dir + "model\\"+f2upper(t)+".java"
        sf = dir + "service\\"+f2upper(t)+"Service.java"
        df = dir + "dao\\"+f2upper(t)+"DAO.java"
        cf = dir + "controller\\" + f2upper(t)+"Controller.java"
        encode = "GBK"
        with open(mf,'w',encoding=encode) as file:
            make_bean(t,dbname,file)
        with open(df,'w',encoding=encode) as file:
            make_dao(dbname,t,file)
        with open(sf,'w',encoding=encode) as file:
            make_service(dbname,t,file)
        with open(cf,'w',encoding=encode) as file:
            make_controller(dbname,t,file)
        # make_doc(dbname,t)
        print(t,dir)
    print(''.join(docs))
    # with open(doc_dir,'w',encoding="utf-8") as file:
    #     file.write(''.join(docs))
    # print(make_bean('user','sys'))
