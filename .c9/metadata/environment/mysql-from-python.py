{"filter":false,"title":"mysql-from-python.py","tooltip":"/mysql-from-python.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":716}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":[" "],"id":717},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":[" "]}],[{"start":{"row":16,"column":6},"end":{"row":17,"column":25},"action":"remove","lines":["cursor.execute(\"DELETE FROM friends WHERE name in ('jim', 'bob')\")","      connection.commit()"],"id":718},{"start":{"row":16,"column":6},"end":{"row":19,"column":74},"action":"insert","lines":["rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","        cursor.executemany(\"INSERT INTO Friends VALUES (%s,%s,%s);\", rows)"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":719}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":[" "],"id":720}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":[" "],"id":721}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":[" "],"id":722},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":[" "],"id":723}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":[" "],"id":724}],[{"start":{"row":17,"column":51},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":725},{"start":{"row":18,"column":0},"end":{"row":18,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":51},"action":"insert","lines":["(\"jim\", 56, \"1955-05-09 13:12:45\"),"],"id":726}],[{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"insert","lines":[","],"id":727}],[{"start":{"row":20,"column":61},"end":{"row":20,"column":62},"action":"insert","lines":["%"],"id":728}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["s"],"id":729}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"remove","lines":["F"],"id":730}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["s"],"id":731}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"remove","lines":["s"],"id":732}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["f"],"id":733}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["m"],"id":734},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"remove","lines":["i"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":["j"]}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["j"],"id":735}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":["j"],"id":736}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["b"],"id":737},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["o"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["b"]}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"remove","lines":["d"],"id":738},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"remove","lines":["e"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"remove","lines":["r"]}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"remove","lines":["f"],"id":739}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["f"],"id":740},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["r"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["e"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":51},"action":"remove","lines":["(\"bob\", 56, \"1955-05-09 13:12:45\"),"],"id":741},{"start":{"row":18,"column":12},"end":{"row":18,"column":16},"action":"remove","lines":["    "]},{"start":{"row":18,"column":8},"end":{"row":18,"column":12},"action":"remove","lines":["    "]},{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":742},{"start":{"row":17,"column":51},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"remove","lines":["s"],"id":743},{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"remove","lines":["%"]}],[{"start":{"row":16,"column":6},"end":{"row":19,"column":71},"action":"remove","lines":["rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","    cursor.executemany(\"INSERT INTO friends VALUES (%s,%s,%s,);\", rows)"],"id":744},{"start":{"row":16,"column":6},"end":{"row":19,"column":74},"action":"insert","lines":["rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","        cursor.executemany(\"INSERT INTO Friends VALUES (%s,%s,%s);\", rows)"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":745}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":[" "],"id":746}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":[" "],"id":747}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"remove","lines":["F"],"id":748}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["f"],"id":749}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":750},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["#"],"id":751}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":[" "],"id":752},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["R"]}],[{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["u"],"id":753},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":[" "],"id":754},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":755},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["q"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["e"],"id":756}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["r"],"id":757}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["y"],"id":758}],[{"start":{"row":21,"column":8},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":759},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":81},"action":"insert","lines":["# Close the connection, regardless of whether or not the above was successful"],"id":760}],[{"start":{"row":20,"column":72},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":761},{"start":{"row":21,"column":0},"end":{"row":21,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":25},"action":"insert","lines":["connection.commit()"],"id":762}],[{"start":{"row":18,"column":51},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":763},{"start":{"row":19,"column":0},"end":{"row":19,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":51},"action":"insert","lines":["(\"jim\", 56, \"1955-05-09 13:12:45\"),"],"id":764}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"remove","lines":["m"],"id":765},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"remove","lines":["i"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"remove","lines":["j"]}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["f"],"id":766},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["r"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["d"],"id":767}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"remove","lines":["6"],"id":768},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"remove","lines":["5"]}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["1"],"id":769},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["0"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["0"]}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":50},"action":"remove","lines":["1955-05-09 13:12:45"],"id":770},{"start":{"row":19,"column":31},"end":{"row":19,"column":50},"action":"insert","lines":["1911-09-12 01:01:01"]}],[{"start":{"row":21,"column":62},"end":{"row":21,"column":63},"action":"insert","lines":[","],"id":771}],[{"start":{"row":21,"column":63},"end":{"row":21,"column":65},"action":"insert","lines":["%s"],"id":772}],[{"start":{"row":21,"column":64},"end":{"row":21,"column":65},"action":"remove","lines":["s"],"id":773},{"start":{"row":21,"column":63},"end":{"row":21,"column":64},"action":"remove","lines":["%"]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":53},"action":"remove","lines":["(\"fred\", 100, \"1911-09-12 01:01:01\"),"],"id":774},{"start":{"row":19,"column":12},"end":{"row":19,"column":16},"action":"remove","lines":["    "]},{"start":{"row":19,"column":8},"end":{"row":19,"column":12},"action":"remove","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "],"id":775},{"start":{"row":18,"column":51},"end":{"row":19,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":6},"end":{"row":21,"column":25},"action":"remove","lines":["rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","      cursor.executemany(\"INSERT INTO friends VALUES (%s,%s,%s,);\", rows)","      connection.commit()"],"id":776},{"start":{"row":17,"column":6},"end":{"row":21,"column":27},"action":"insert","lines":["rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","        cursor.executemany(\"INSERT INTO Friends VALUES (%s,%s,%s);\", rows)","        connection.commit()"]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":777}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":[" "],"id":778}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"remove","lines":[" "],"id":779},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"remove","lines":[" "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":[" "],"id":780}],[{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"remove","lines":[" "],"id":781},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"remove","lines":["F"],"id":782}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["f"],"id":783}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":16},"action":"remove","lines":["    "],"id":784}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":[" "],"id":785},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":[" "]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":[" "]}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"remove","lines":[" "],"id":786}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":16},"action":"remove","lines":["    "],"id":787}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":[" "],"id":788},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":[" "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":789}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":[" "],"id":790}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":791}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":[" "],"id":792}],[{"start":{"row":0,"column":0},"end":{"row":24,"column":19},"action":"remove","lines":["import os","import datetime","import pymysql","","# Get the username from the Cloud9 workspace","# (modify this variable if running on another environment)","username = os.getenv('C9_USER')","","# Connect to the database","connection = pymysql.connect(host='localhost',","                             user=username,","                             password='',","                             db='Chinook')","","try:","    # Run a query","    with connection.cursor() as cursor:","      rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","              (\"jim\", 56, \"1955-05-09 13:12:45\"),","              (\"fred\", 100, \"1911-09-12 01:01:01\")]","    cursor.executemany(\"INSERT INTO friends VALUES (%s,%s,%s);\", rows)","    connection.commit()","finally:"," # Close the connection, regardless of whether or not the above was successful"," connection.close()"],"id":793},{"start":{"row":0,"column":0},"end":{"row":22,"column":22},"action":"insert","lines":["import os","import datetime","import pymysql","","# Get the username from the Cloud9 workspace","# (modify this variable if running on another environment)","username = os.getenv('C9_USER')","","# Connect to the database","connection = pymysql.connect(host='localhost',","                             user=username,","                             password='',","                             db='Chinook')","","try:","    with connection.cursor() as cursor:","        rows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","        cursor.executemany(\"INSERT INTO Friends VALUES (%s,%s,%s);\", rows)","        connection.commit()","finally:","    connection.close()"]}],[{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"remove","lines":["F"],"id":794}],[{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["f"],"id":795}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":796},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["#"],"id":797}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":[" "],"id":798},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["R"]}],[{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["u"],"id":799},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":[" "],"id":800},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":801},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["q"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["a"],"id":802}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["a"],"id":803}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["e"],"id":804},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["r"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["y"]}],[{"start":{"row":22,"column":8},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":805},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":81},"action":"insert","lines":["# Close the connection, regardless of whether or not the above was successful"],"id":806}],[{"start":{"row":17,"column":9},"end":{"row":20,"column":74},"action":"remove","lines":["ows = [(\"bob\", 21, \"1990-02-06 23:04:56\"),","                (\"jim\", 56, \"1955-05-09 13:12:45\"),","                (\"fred\", 100, \"1911-09-12 01:01:01\")]","        cursor.executemany(\"INSERT INTO friends VALUES (%s,%s,%s);\", rows)"],"id":807},{"start":{"row":17,"column":9},"end":{"row":17,"column":86},"action":"insert","lines":["# Close the connection, regardless of whether or not the above was successful"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":86},"action":"remove","lines":["r# Close the connection, regardless of whether or not the above was successful"],"id":808},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["v"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["v"],"id":809}],[{"start":{"row":17,"column":8},"end":{"row":22,"column":26},"action":"insert","lines":["list_of_names = ['fred', 'Fred']","        # Prepare a string with same number of placeholders as in list_of_names","        format_strings = ','.join(['%s'] * len(list_of_names))","        cursor.execute(","            \"DELETE FROM Friends WHERE name in ({});\".format(format_strings),","            list_of_names)"],"id":810}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["F"],"id":811}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["f"],"id":812}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"remove","lines":["d"],"id":813},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["e"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"remove","lines":["r"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"remove","lines":["f"]}],[{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["b"],"id":814},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["o"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["b"]}],[{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"remove","lines":["d"],"id":815},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"remove","lines":["e"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":["r"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":["F"]}],[{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["j"],"id":816},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["i"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["m"]}]]},"ace":{"folds":[],"scrolltop":45,"scrollleft":0,"selection":{"start":{"row":17,"column":36},"end":{"row":17,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1565534261474,"hash":"f7b3edad34f7a3923520a0692efbea865be49a9f"}