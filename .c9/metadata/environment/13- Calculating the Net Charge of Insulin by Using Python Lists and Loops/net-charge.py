{"filter":false,"title":"net-charge.py","tooltip":"/13- Calculating the Net Charge of Insulin by Using Python Lists and Loops/net-charge.py","undoManager":{"mark":34,"position":34,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":29},"action":"insert","lines":["# Python3.6  ","# Coding: utf-8  ","# Store the human preproinsulin sequence in a variable called preproinsulin:  ","preproInsulin = \"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn\"  ","# Store the remaining sequence elements of human insulin in variables:  ","lsInsulin = \"malwmrllpllallalwgpdpaaa\"  ","bInsulin = \"fvnqhlcgshlvealylvcgergffytpkt\"  ","aInsulin = \"giveqcctsicslyqlenycn\"  ","cInsulin = \"rreaedlqvgqvelgggpgagslqplalegslqkr\"  ","insulin = bInsulin + aInsulin"],"id":2}],[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}",""],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":6}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":45},"action":"insert","lines":["Assigning variables, lists, and dictionaries"],"id":7}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":16,"column":1},"end":{"row":16,"column":54},"action":"insert","lines":["Using count() to count the numbers of each amino acid"],"id":9}],[{"start":{"row":16,"column":54},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":80},"action":"insert","lines":["seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})"],"id":11}],[{"start":{"row":17,"column":80},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":19,"column":1},"end":{"row":20,"column":0},"action":"insert","lines":["Writing the net charge formula",""],"id":13}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":14}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":17},"action":"insert","lines":["while (pH <= 14):"],"id":17}],[{"start":{"row":21,"column":17},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":26,"column":43},"action":"insert","lines":["netCharge = (","    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \\","    for x in ['k','h','r']}.values()))","    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \\","    for x in ['y','c','d','e']}.values())))"],"id":19}],[{"start":{"row":26,"column":43},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":31},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":6},"action":"insert","lines":["pH = 0"],"id":22}],[{"start":{"row":27,"column":43},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":42},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":24}],[{"start":{"row":29,"column":42},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":10},"action":"insert","lines":["pH +=1"],"id":26}],[{"start":{"row":29,"column":4},"end":{"row":30,"column":10},"action":"remove","lines":["print('{0:.2f}'.format(pH), netCharge)","    pH +=1"],"id":27}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":28},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"remove","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":43},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":27,"column":43},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":30}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":31}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":10},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)","    pH +=1"],"id":32}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "],"id":33}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["",""],"id":34}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":35}],[{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":42},"end":{"row":30,"column":0},"action":"remove","lines":["",""],"id":37}],[{"start":{"row":29,"column":42},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":31,"column":0},"end":{"row":31,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1661944773038,"hash":"166fada574406d34ca7de43767f470ecf4f79376"}