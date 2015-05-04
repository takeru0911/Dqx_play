#coding:utf-8

import MySQLdb
import os
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
            item_id = item["id"]
            files = os.listdir('./' + item_id + '/')
            print item_id
            for fileName in files :
                f = open('./' + str(item_id) + '/' + fileName)
                marFile = f.read()
                f.close()

                marketInfo = json.loads(marFile)

                for market in marketInfo :
                    time = market["time"]
                    time = time.replace('/' ,'')
                    time = time.replace(u'時', '').replace(" ", "")

                    time = time + '0000'
                    star0 = market["star0"]
                    star1 = market["star1"]
                    star2 = market["star2"]
                    star3 = market["star3"]
                    cursor.execute("select id from item where name=\"" + item_name + "\"")

                    results = cursor.fetchall()
                    for res in results :
                        item_id_db = res[0]
                        print item_name + " : " + str(item_id_db)
                        star0["price"]    = star0["price"].replace("--", "").replace(" ","").replace(",", "")
                        star0["exhibits"] = star0["exhibits"].replace("--", "").replace(" ","")
                        star1["price"]    = star1["price"].replace("--", "").replace(" ","").replace(",", "")
                        star1["exhibits"] = star1["exhibits"].replace("--", "").replace(" ","") 
                        star2["price"]    = star2["price"].replace("--", "").replace(" ","").replace(",", "")
                        star2["exhibits"] = star2["exhibits"].replace("--", "").replace(" ","") 
                        star3["price"]    = star3["price"].replace("--", "").replace(" ","").replace(",", "")
                        star3["exhibits"] = star3["exhibits"].replace("--", "").replace(" ","") 

                        print (u"insert into market_item (stars, date, price, exhibits, item_id) value(3, \"" + time + "\", " + star3["price"] + " ," + str(star3["exhibits"]))
                        if star0["price"] != "" and star0["exhibits"] != "" :
                            cursor.execute(u"insert into market_item (stars, date, price, exhibits, item_id) value(0, \"" + time + "\", " + star0["price"] + " ," + star0["exhibits"] + "," + str(item_id_db) + ")")
                            connector.commit()
                        if star1["price"] != "" and star1["exhibits"] != "" :
                            cursor.execute(u"insert into market_item (stars, date, price, exhibits, item_id) value(1, \"" + time + "\", " + star1["price"] + " ," + star1["exhibits"] + "," + str(item_id_db) + ")")
                            connector.commit()
                        if star2["price"] != "" and star2["exhibits"] != "" :
                            cursor.execute(u"insert into market_item (stars, date, price, exhibits, item_id) value(2, \"" + time + "\", " + star2["price"] + " ," + star2["exhibits"] + "," + str(item_id_db) + ")")
                            connector.commit()
                        if star3["price"] != "" and star3["exhibits"] != "" :
                            cursor.execute(u"insert into market_item (stars, date, price, exhibits, item_id) value(3, \"" + time + "\", " + star3["price"] + " ," + star3["exhibits"] + "," + str(item_id_db) + ")")
                            connector.commit()

                            
           
                        


#            
#            result = cursor.fetchall()
#            for data in result:
#                categoryID = data[0]
##                print category
##                print str(categoryID)
##            cursor.execute("insert into item (name, category_id) value(\"" + item_name + "\"," + str(categoryID) +")")
##            connector.commit()
# 
#            for material in item["materials"]:
#                material_name = material["material_name"]
#                numOfRequir = material["material_require"]
#                temp = cursor.execute("select id from material where material_name=\"" + material_name + "\"")
#                result = cursor.fetchall()
#                material_id = 0
#                for numOfExist in result:
##                    if numOfExist[0] == 0:
##                        cursor.execute("insert into material (material_name) value(\"" + material_name + "\")")
##                        connector.commit()
#                    material_id = numOfExist[0]
# 
##                cursor.execute("insert into design (item_id,material_id,num_material) value(" + str(i) + "," + str(material_id) + "," + str(numOfRequir) + ")")
##                connector.commit()
# 
# 
#            i = i + 1
            
        
connector.close()                
                                       
                                      
                                      
                    

                
            

            




                           

