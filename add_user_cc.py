import psycopg2
from config import config


def add_user_cc(email, firstname, lastname, typeid, userpassword, licenseplate, cardnumber, expirationmonth,
                expirationyear, cardfirstname, cardlastname):
    conn = None

    try:

        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute('CALL create_user_with_cc(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
        email, firstname, lastname, typeid, userpassword, licenseplate, cardnumber, expirationmonth, expirationyear,
        cardfirstname, cardlastname))

        conn.commit()

        cur.close()



    except (Exception, psycopg2.DataError) as error:

        print(str(error) + "\nError code: 111")



    finally:

        if conn is not None:
            conn.close()
