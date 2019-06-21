import read
import numpy as np

def findName(name):
    data = read.readNames('nicknames.txt') 
    for d in data:
        if d['name'] == name: #nicknameが存在するかをチェック、もしあったらidを返す
            return d['id']
    return None


def bfs(graph, start, end):
    searchedList = []  # 探索済みリスト
    data = {start: []} 
    queue = [start]  # キュー
    while queue:
        current = queue.pop(0)  # 現在位置
        if current == end:
            return len(data[current]) #ステップ数
        if current not in searchedList:
            searchedList.append(current)
            queue += graph[current]
            for id in graph[current]:
                if not id in data.keys():
                    data[id] = data[current] + [current]


def main():
    startName = input('Enter your account name: ')
    endName = input('Who is the person you are looking for?: ')

    start = findName(startName)
    end = findName(endName)

    if start is None:
        print('%s was not found…' % startName)
        exit()
    elif end is None:
        print('%s was not found…' % endName)
        exit()
    else:
        print('OK.')
        
    linkData = read.readLinks('links.txt')
    graph = read.graph(linkData)
    step = bfs(graph, start, end)

    if step == 1:
        print('%s need %d step to reach out to %s.' % (startName, step, endName))
    elif step != None:
        print('%s need %d steps to reach out to %s.' % (startName, step, endName))
    else: 
        print('%s cannot reach out to %s' % (startName, endName))


if __name__ == "__main__":
    main()
