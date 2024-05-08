from dao.ICourierUserService import *
from entity.model.Courier import *
from util.connectionutil.DBConnection import *

class CourierUserServiceImpl(ICourierUserService, Courier):
    def __init__(self):
        self.connection = DBConnection.getConnection()
        if self.connection is None:
            print('Failed to Connect to the Database')

    def placeOrder(self, courier):
        cur = self.connection.cursor()
        query = 'Insert into Couriers (), Values()'
