#!/usr/bin/env python3
import os,sys,re,yaml,jinja2,shutil
def expandreferences(resource, content):
    if type(content)==type(dict()):
        for k in content:
            v=content[k]
            if type(v)==type(''):
                if v in resource:
                    content[k]=resource[v]
            else:
                expandreferences(resource, v)
    elif type(content)==type(list()):
        for i,v in enumerate(content):
            if type(v)==type(''):
                if v in resource:
                    content[i]=resource[v]
            else:
                expandreferences(resource, v)

if __name__=='__main__':
    with open('servers.yaml','r+') as f:
        servers = yaml.load(f)
    for project in sys.argv[1:2]:
        initpy=os.path.join(project,'__init__.py')
        open(initpy,'a').close()
        jEnv = jinja2.Environment(
                loader=jinja2.PackageLoader(project,'templates'),
                autoescape=jinja2.select_autoescape(['html','xml'])
        )
        with open(os.path.join(project,'config.yaml')) as c:
            instances = yaml.load(c)
        for k in instances:
            instance=instances[k]
            expandreferences(servers,instance)
            instance['name'] = k
            destination=os.path.join(project,instance['name'])
            try:
                shutil.rmtree(destination)
            except FileNotFoundError:
                pass
            os.mkdir(destination)
            for templatename in jEnv.list_templates():
                template = jEnv.get_template(templatename)
                template.stream(instance).dump(os.path.join(destination,templatename))
        pycache=os.path.join(project,'__pycache__')
        try:
            shutil.rmtree(pycache)
        except FileNotFoundError:
            pass
        try:
            os.remove(initpy)
        except FileNotFoundError:
            pass
