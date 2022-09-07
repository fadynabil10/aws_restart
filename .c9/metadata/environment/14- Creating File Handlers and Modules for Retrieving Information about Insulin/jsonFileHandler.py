{"filter":false,"title":"jsonFileHandler.py","tooltip":"/14- Creating File Handlers and Modules for Retrieving Information about Insulin/jsonFileHandler.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":7,"column":0},"end":{"row":14,"column":15},"action":"remove","lines":["def readJsonFile(fileName):","    data = \"\"","    try:","        with open('files/insulin.json') as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"],"id":2},{"start":{"row":7,"column":0},"end":{"row":11,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"]}],[{"start":{"row":11,"column":15},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":4},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":14,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data",""],"id":7}],[{"start":{"row":7,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data","    "],"id":8},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["","    "],"id":9}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":26},"action":"remove","lines":["fileName"],"id":13},{"start":{"row":10,"column":18},"end":{"row":10,"column":38},"action":"insert","lines":["'files/insulin.json'"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":29},"end":{"row":13,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1662322893904,"hash":"b24a7adf74a98bb3a1b0e98a69dca75848723695"}