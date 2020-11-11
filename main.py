from data_classes.point_type import PointType
from data_classes.object_type import ObjectType
from data_classes.drone import Drone
from data_classes.role import Role
from data_classes.route import Route
from data_classes.point import Point
from data_classes.point_on_route import PointOnRoute
from data_classes.account import Account
from data_classes.user import User
from data_classes.flight_schedule import FlightSchedule
from data_classes.flight import Flight
from data_classes.log import Log
from data_classes.flaw import Flaw
from data_classes.object import Object

from utilities.db_connection import conn, cursor
from utilities.db_conn_utilities import drop_database, get_all_index
from values import SCRIPT_FILENAME
import os

def generate():
    PointType.generate_all(cursor)
    conn.commit()
    ObjectType.generate_all(cursor)
    conn.commit()
    Drone.generate_all(cursor)
    conn.commit()
    Role.generate_all(cursor)
    conn.commit()
    Route.generate_all(cursor)
    conn.commit()
    Point.generate_all(cursor)
    conn.commit()
    # PointOnRoute.generate_all(cursor)
    # conn.commit()

    Account.generate_all(cursor)
    conn.commit()
    User.generate_all(cursor)

    conn.commit()
    FlightSchedule.generate_all(cursor)
    conn.commit()
    Flight.generate_all(cursor)
    conn.commit()

    Flaw.generate_all(cursor)
    conn.commit()

    Object.generate_all(cursor)
    conn.commit()


if __name__ == "__main__":
    if os.path.exists(SCRIPT_FILENAME):
        os.remove(SCRIPT_FILENAME)
    # drop_database(cursor)
    # generate()
    print(get_all_index(cursor, 'flight'))
    conn.commit()
    conn.close()

