# -*- coding:utf-8 -*-

import app.models.db as db
import app.models.pager as pager

class Mistake:

    def load(self, page):

        define_page = 10
        start = (page - 1) * define_page

        result = {}

        sql = "select count(id) as all_count from mistake"
        db.con.execute(sql)
        result = db.con.fetchone()

        result["pagination"] = pager.Pagination(page, define_page, result["all_count"])

        sql = "select * from mistake order by kana"
        sql += ' limit %s, %s'
        db.con.execute(sql, (start, define_page))
        result["mistakes"] = db.con.fetchall()

        return result


    def edit(self, id):

        sql = "select * from mistake where id = %s"
        db.con.execute(sql, (id,))
        return db.con.fetchone()


    # idがあったらdelフラグありで削除、無しで更新、idがなかったら新規追加
    def done(self, params):

        if params["id"]:

            if params["del"]:
                sql = "delete from mistake where id = %s"
                db.con.execute(sql, (params["id"]))
            else:
                sql = "update mistake set "
                sql += " num=%s"
                sql += ",name=%s"
                sql += ",kana=%s"
                sql += ",regdate=CURRENT_TIMESTAMP"
                sql += " where id = %s"
                db.con.execute(sql, (
                                    params["num"],
                                    params["name"],
                                    params["kana"],
                                    params["id"]
                                    ))

        else:

            sql = "insert into mistake (num, name, kana, regdate) values (%s, %s, %s, CURRENT_TIMESTAMP)"
            db.con.execute(sql, (
                                params["num"],
                                params["name"],
                                params["kana"],
                                ))

        db.dbhandle.commit()
        return

