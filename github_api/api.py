import requests


def get_api_url(github_repo_url):
    if github_repo_url[-1] == '/':
        github_repo_url = github_repo_url[:-1]
    return f'https://api.github.com/repos/{github_repo_url[len("https://github.com/"):]}'


def get_api_release_url(github_repo_url):
    return get_api_url(github_repo_url) + '/releases'


def is_valid_api(api_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Response content: {response.content}")
        return False
