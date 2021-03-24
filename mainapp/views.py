from django.shortcuts import render
from django.conf import settings

from github import Github

from mainapp.models import SearchUser
from mainapp.utils import repository_info

# get pygithub object
pygithub_object = Github(settings.GITHUB_TOKEN)


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchUser(request.POST)

        # checking for an empty field
        if request.POST['username']:
            # checking for the existence of a user in GitHub
            try:
                # get data user by username
                user = pygithub_object.get_user(request.POST['username'])

                # get info about repositories
                github_repositories = user.get_repos()
                repositories = []

                for repo in github_repositories:
                    # check have repository closed pull
                    if repo.get_pulls(state="closed").totalCount:
                        print(type(repo))
                        repositories.append(repository_info(repo))
                context = {'repositories': repositories}
                return render(request, 'mainapp/result_search.html', context)
            except Exception as e:
                print(e)
                context = {'error': f'User {request.POST["username"]} not exists'}
            return render(request, 'mainapp/result_search.html', context)
    else:
        form = SearchUser()
    return render(request, 'mainapp/index.html', {'form': form})

