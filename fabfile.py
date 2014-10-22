from fabric.colors import cyan, yellow
from fabric.context_managers import hide, cd, prefix, settings
from fabric.contrib.files import upload_template
from fabric.decorators import task
from fabric.operations import local, run, sudo
from fabric.state import *

env.hosts = ['54.69.116.111']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/blog_analytics.pem'
env.shell = '/bin/bash -l -i -c'
# env.warn_only = True

@task
def ubuntu_hello():
    with hide('stdout'):
        output = run('lsb_release -a')
        print(yellow(output))

def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")

@task
def deploy():
    with prefix('workon blog_analytics'):
        with cd('/home/ubuntu/rocketu_blog_analytics'):
            run('git pull origin master')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')

    restart_app()

@task
def setup_nginx(project_name, server_name):
    upload_template("./deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))

@task
def setup_gunicorn(project_name):
    upload_template("./deploy/gunicorn.conf.py",
                    "/home/ubuntu/{}".format(project_name),
                    {'project_name': project_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def setup_supervisor(project_name, virtualenv):
    upload_template("./deploy/supervisor.conf",
                    "/etc/supervisor/conf.d/{}.conf".format(project_name),
                    {'project_name': project_name,
                     'virtualenv': virtualenv},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def hello():
    print(cyan('I\'m alive!'))

@task
def create_file(file_name):
    local('touch ~/projects/devOpsProject/rocketu_blog_analytics/{}.txt'.format(file_name))

@task
def new_directory(path, new_dir):
    local('mkdir ~/{}/{}'.format(path, new_dir))
