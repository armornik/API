def repository_info(repository):
    info = [f'Full name: {repository.full_name}', f'Link on GitHub: {repository.clone_url}',  # repository full name
            f'Number of stars: {repository.stargazers_count}',  # link to the project on GitHub
            f'Number of pulls_closed: {repository.get_pulls(state="closed").totalCount}']  # number of stars

    # links to merged pool - requests from the user and number of comments
    for request_merged in repository.get_pulls(state='closed'):
        info.append(f'Links to merged pool-requests: {request_merged.html_url}')
        info.append(f'Number of comments: {request_merged.comments}')

    # links to not merged pool-requests from the user
    for request_open in repository.get_pulls():
        info.append(f'Links to open requests: {request_open.html_url}')
        info.append(f'Number of comments: {request_open.comments}')

    return info
