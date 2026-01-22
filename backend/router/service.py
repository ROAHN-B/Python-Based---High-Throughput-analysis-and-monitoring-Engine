from backend.config.sql_config import connect_sql
from mysql.connector import Error
from fastapi import APIRouter

router = APIRouter()

@router.post("/create/user") #API end point
def create_user(name,age,email):
    try:
        db=connect_sql()
        cursor = db.cursor(dictionary=True)
        query = "insert into usertable (name,age,email) values(%s,%s,%s)"
        cursor.execute(query,(name,age,email))
        db.commit()
        cursor.close()
        db.close()
        return {"Message":"User added to database succesfully"}
    except Error as e:
        print("Error : ", e)


@router.get("/get/user/info")
def get_user(id):
    db=connect_sql()
    cursor=db.cursor(dictionary=True)
    query="select name,age,email from usertable where id = %s "
    cursor.execute(query,(id,))
    user=cursor.fetchone()
    db.close()
    cursor.close()
    return {"message":"USer found!!","data":user}

@router.put("/update/user")
def update_user(id,name,age,email):
    db=connect_sql()
    cursor=db.cursor(dictionary=True)
    query="update usertable set name=%s,age=%s,email=%s where id=%s"
    cursor.execute(query,(name,age,email,id))
    db.commit()
    db.close()
    cursor.close()
    return {"Message":"User updated seccesfully!!"}

@router.delete("/delete/user/info")
def delete_user(id):
    db=connect_sql()
    cursor=db.cursor(dictionary=True)
    query="delete from  usertable where id=%s"
    cursor.execute(query,(id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"user deleted succesfully!!"}

