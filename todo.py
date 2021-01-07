import sys
vec = sys.argv
from datetime import datetime
import os
def add(item):
    count = 0
    if os.path.exists('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt'):
        with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','r') as file:
            lines = file.readlines()
        for line in lines:
            if line == item+'\n':
                count += 1
        if count !=1:    
            with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','a') as file:
                file.write(item+'\n')
        print('Added todo: "{}"'.format(item))
    else:
        with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','a') as file:
            lines = file.write(item+'\n')
        print('Added todo: "{}"'.format(item))
def ls():
    with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','r') as file:
        lines = file.readlines()
    lines.reverse()
    if len(lines)!=0:
        count = len(lines)
        for line in lines:
            line = line.strip('\n')
            print('[{}] {}'.format(count,line))
            count -= 1

    else:
        print('There are no pending todos!')
def delete(number):
    if number=='0':
        print("Error: todo #{} does not exist. Nothing deleted.".format(int(number)))
    else:
        with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','r') as file:
            lines = file.readlines()
        try:
            print(number)
            print(lines)
            if len(lines)>=int(number):
                lines.pop(int(number)-1)
                with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','w') as file:
                    for line in lines:
                        file.write(line)
                print('Deleted todo #'+number)
            else:
                print("Error: todo #{} does not exist. Nothing deleted.".format(int(number)))
        except:
            print("Error: todo #{} does not exist. Nothing deleted.".format(int(number)))

def done(number):
    if number == '0':
        print('Error: todo #{} does not exist.'.format(int(number)))
    else:
        date = datetime.today().strftime('%Y-%m-%d')
        with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','r') as file:
            lines = file.readlines()
        lines.reverse()
        try:
            done = lines.pop(int(number)-1)
            if os.path.exists('C:\\Users\\user\\OneDrive\\Desktop\\done.txt'):
                with open('C:\\Users\\user\\OneDrive\\Desktop\\done.txt','r') as file:
                    li = file.readlines()
                if 'x '+date+' '+done not in li:
                    with open('C:\\Users\\user\\OneDrive\\Desktop\\done.txt','a') as file:
                        file.write('x '+date+' '+done)
                print('Marked todo #'+number+' as done.')
            else:
                with open('C:\\Users\\user\\OneDrive\\Desktop\\done.txt','a') as file:
                    file.write('x '+date+' '+done)
            print('Marked todo #'+number+' as done.' )
            with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','w') as file:
                for line in reversed(lines):
                    if line != done:
                        file.write(line)
        except:
            print('todo #'+number+' does not exist.')

def report():
    with open('C:\\Users\\user\\OneDrive\\Desktop\\todo.txt','r') as file:
        lines = file.readlines()
    c1 = len(lines)
    with open('C:\\Users\\user\\OneDrive\\Desktop\\done.txt','r') as file:
        l = file.readlines()
    c2 = len(l)
    print('{} Pending : {} Completed : {}'.format(datetime.today().strftime('%Y-%m-%d'),c1,c2))

if __name__ == "__main__":
    if len(vec)==1 or vec[1]=='help' or vec[1] == '':
        a = """Usage :-\n ./todo add "todo item"  # Add a new todo\n ./todo ls               # Show remaining todos\n ./todo del NUMBER       # Delete a todo\n ./todo done NUMBER      # Complete a todo\n ./todo help             # Show usage\n ./todo report           # Statistics """
        print(a)
    elif len(vec)>1:    
        if vec[1] == 'add':
            if len(vec) ==3:
                add(vec[2])
            else:
                print('Error: Missing todo string. Nothing added!')
        if vec[1] == 'ls':
            ls()
        if vec[1] == 'del':
            if len(vec) == 3:
                delete(vec[2])
            else    :
                print('Error: Missing NUMBER for deleting todo.')
        if vec[1] == 'done':
            try:
                done(vec[2])
            except:
                print('Error: Missing NUMBER for marking todo as done.')
        if vec[1] == 'report':
            report()