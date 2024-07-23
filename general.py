import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Directory "+directory)
        os.makedirs(directory)

def create_data_files(project_name,base_url):
    queue=project_name+'/queue.txt'
    crawled=project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,base_url)

    
    if not os.path.isfile(crawled):
        write_file(crawled,'')


def write_file(path,data):
    with open(path, 'w') as f:
        f.write(data)

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

def delete_file_contents(path):
    open(path,'w').close()


def file_to_set(filename):
    results=set()
    with open(filename,'rt') as file:
        for line in file:
            results.add(line.replace('\n',''))
    return results


def set_to_file(links,file):
    with open(file,'w') as f:
        for link in sorted(links):
            f.write(link+'\n')



