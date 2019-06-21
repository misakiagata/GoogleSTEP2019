def readNames(filename):
    nameData = [] # 辞書のリスト
    nameFile = open(filename, "r")
    for line in nameFile:
        if line.split():
            nameData.append({ "id": int(line.split()[0]), "name": line.split()[1] }) #id:Name
    return nameData


def readLinks(filename):
    linkData = [] # 辞書のリスト
    linkFile = open(filename, "r") 
    for line in linkFile:
        if line.split():
            linkData.append({ "from": int(line.split()[0]), "to": int(line.split()[1]) }) #from:to
    return linkData


def graph(linkData): 
    graph = {} 
    to = [linkData[0]['to']]
    for i in range(1, len(linkData)):
        if linkData[i-1]['from'] == linkData[i]['from']: 
            to.append(linkData[i]['to']) #fromがフォローしている全userをlistにまとめる
        else:
            to = [linkData[i]['to']] #1人目がフォローしているuserがいなくなったら次
        graph[linkData[i]['from']] = to
    return graph
