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
import values


def generate():
    PointType.generate_all()
    ObjectType.generate_all()
    Drone.generate_all()
    Role.generate_all()

    # Route.generate_all()
    # Point.generate_all()
    # PointOnRoute.generate_all()

    Account.generate_all()
    User.generate_all()

    # FlightSchedule.generate_all()
    # Flight.generate_all()
    # Log.generate_all()
    # Flaw.generate_all()

    # Object.generate_all()


if __name__ == "__main__":
    generate()
