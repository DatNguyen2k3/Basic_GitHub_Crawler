from django.shortcuts import render
import requests
import markdown
from . import api


# Create your views here.
def search_view(request):
    # No request for get release
    if request.method != 'POST':
        return render(request, 'github_api/search.html')

    # Get api release url
    context = {}
    github_url = request.POST.get('search')
    api_release_url = api.get_api_release_url(github_url)

    # Invalid GitHub link
    if not api.is_valid_api(api_release_url):
        context['is_valid'] = False
        context['error_message'] = 'Invalid GitHub link'
        return render(request, 'github_api/search.html', context)

    # Valid GitHub link
    # Get data from GitHub API
    response = requests.get(api_release_url)
    api_data = response.json()

    # No release found
    if not api_data:
        context['is_have_release'] = False
        context['error_message'] = 'No release found'
        return render(request, 'github_api/search.html', context)

    # Release found, show releases
    context['is_have_release'] = True
    releases = []
    context['releases'] = releases

    # TODO: add data in releases
    for release in api_data:
        release_dict = {
            'version': release['tag_name'],
            'author': release['author']['login'],
            'date': f'Created at: {release["created_at"][:10]}\nPublished at: {release["published_at"][:10]}',
            'content': markdown.markdown(release['body'])
        }
        releases.append(release_dict)

    context['releases'] = releases
    return render(request, 'github_api/search.html', context=context)
