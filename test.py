from github import Github

# Github username
# username = "Armornik"
username = "MVIG-SJTU"

GITHUB_TOKEN = '6e0030c79dc13b3be1b0cdc6b5082c443f7caac3'

# get pygithub object
g = Github(GITHUB_TOKEN)
# g = Github()

# get data user by username
user = g.get_user(username)
# pprint(dir(user.get_repos().get_page))


def repository_info(repository):
    # check have repository closed pull
    if repository.get_pulls(state='closed').totalCount:

        # repository full name
        print("Full name:", repository.full_name)

        # link to the project on GitHub
        print("Link on GitHub:", repository.clone_url)

        # number of stars
        print("Number of stars:", repository.stargazers_count)
        print("Number of pulls_closed:", repository.get_pulls(state='closed').totalCount)

        # links to merged pool - requests from the user and number of comments
        for repos in repository.get_pulls(state='closed'):
            print("Links to merged pool-requests:", repos.html_url)
            print("Number of comments:", repos.comments)

        # links to not merged pool-requests from the user
        for repos in repository.get_pulls():
            print("Links to open requests:", repos.html_url)
            print("Number of comments:", repos.comments)


# get public repository by username and print info
for repo in user.get_repos():
    repository_info(repo)
