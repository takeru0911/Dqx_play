#coding:utf-8

import MySQLdb
import simplejson as json

connector = MySQLdb.connect(host='localhost', db='dqx', user='takeru', passwd='takeru911', charset='utf8')
cursor = connector.cursor()

i = 1
for cat in range(1, 9) :
    if cat == 6 or cat == 7 :
        continue

    for level in ["1", "31"]:
        print str(cat) + "_" + level + ".json"
        f = open(str(cat) + "_" + level + ".json", "r")
        
        fileContent = f.read()
        f.close()


        formatedContent = json.loads(fileContent)

        for item in formatedContent :
            cursor.execute("SET NAMES utf8") 
            category = item["kind_name"]
            item_name = item["item_name"]
            temp = cursor.execute("select id from category where category_name=\"" + category + "\"")
            
            result = cursor.fetchall()
            for data in result:
                categoryID = data[0]
#                print category
#                print str(categoryID)
#            cursor.execute("insert into item (name, category_id) value(\"" + item_name + "\"," + str(categoryID) +")")
#            connector.commit()

            for material in item["materials"]:
                material_name = material["material_name"]
                numOfRequir = material["material_require"]
                temp = cursor.execute("select id from material where material_name=\"" + material_name + "\"")
                result = cursor.fetchall()
                material_id = 0
                for numOfExist in result:
#                    if numOfExist[0] == 0:
#                        cursor.execute("insert into material (material_name) value(\"" + material_name + "\")")
#                        connector.commit()
                    material_id = numOfExist[0]

#                cursor.execute("insert into design (item_id,material_id,num_material) value(" + str(i) + "," + str(material_id) + "," + str(numOfRequir) + ")")
#                connector.commit()


            i = i + 1
            item_id = item["item_id"]
        
connector.close()                
                                       
                                      
                                      
                    

                
            

            




                           

