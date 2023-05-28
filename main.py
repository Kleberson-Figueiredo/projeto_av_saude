from models.usuario import User
from models.Peso_semanal import peso_semanal
import datetime

data_hj = datetime.date.today()
print(data_hj)
#peso_semanal.insert("033","2023-05-25","70")
#User.insert_user("kleberson","033","1.75","65")
peso_semanal.update("033","2023-05-23","75")
#data_bd = peso_semanal.ListarUltimaData()[0][1]
# print(data_bd)
# data_calc = str(data_bd).replace("-","")
# data_real = str(data_hj).replace("-","")
# result = (int(data_calc) - int(20230514)) + 1
# print(result)
