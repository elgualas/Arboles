import os 
import datetime
import pandas as pd
from sqlalchemy import create_engine

start_time=datetime.datetime.now()
print('Begin',start_time)
num=0
engine=create_engine('mysql+pymysql://root:chrono69@localhost:3306/arboles?charset=utf8mb4')
path=r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads'
files=os.listdir(path)

for i in files:
    data=pd.read_excel(os.path.join(path,i),header=0)
    data.to_sql(name='arbol',con=engine,index=False,if_exists='append')
    num+=1
    print('Imported: ',i)

end_time=datetime.datetime.now()
print('End: ',end_time)
total_time=end_time-start_time
print('total time:', total_time)
print('total numbre of imported files:', num)



